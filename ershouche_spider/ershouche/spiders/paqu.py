import re

import scrapy
from scrapy import Request
from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from ershouche.items import ErshoucheItem

#用rules正则匹配的话，没有出现在页面上的页码，匹配不到
# class carspider(CrawlSpider):
#     name = 'renrenche'
#     domain = 'https://www.renrenche.com'
#     start_urls = 'https://www.renrenche.com/cd/dazhong/p1}'
#     # rules = [
#     #     Rule(LinkExtractor(allow=r'https://www.renrenche.com/cd/dazhong/p.*'), callback='parseq')
#     # ]
#
#
#     #
#     # def start_requests(self):
#     #     for i in range(1,91):
#     #         yield Request(self.start_urls.format(n=i), callback=self.parse)
#     def start_requests(self):
#         yield Request(self.start_urls)
#
#
#     def parse(self, response):
#         res = Selector(response)
#         hrefs = res.xpath('//*[@id="search_list_wrapper"]/div/div/div[1]/ul/li/a/@href').extract()
#         list_href = []
#         for href in hrefs:
#             if len(href) > 21:
#                 list_href.append(href)
#                 yield Request(self.domain + href,
#                               callback=self.parse_car,
#                               meta={'res':res})
#
#
#     def parse_car(self, response):
#         sel = Selector(response)
#         carinfo = sel.xpath('//*[@id="basic"]/div[2]/div[2]/div[1]')
#         if carinfo.xpath('./div/h1/text()').extract():
#             title = carinfo.xpath('./div/h1/text()').extract()[0]
#             price = carinfo.xpath('./div[3]/div[1]/p/text()').extract()[0] + '万'
#             souhu = carinfo.xpath('./div[3]/div[3]/p[2]/text()').extract()
#             yuegong = carinfo.xpath('./div[3]/div[3]/p[3]/text()').extract()
#             lichen = carinfo.xpath('./div[4]/ul/li[1]/div/p/strong/text()').extract()[0]
#             cheling = carinfo.xpath('./div[4]/ul/li[2]/div//p/strong/text()').extract()
#             chepaididian = carinfo.xpath('./div[4]/ul/li[3]/div/p/strong/text()').extract()[0]
#             item = ErshoucheItem()
#             item['title'] = title
#             item['price'] = price
#             item['souhu'] = souhu
#             item['yuegong'] = yuegong
#             item['lichen'] = lichen
#             item['cheling'] = cheling
#             item['chepaididian'] = chepaididian
#             yield item
#
#             res2 = response.meta.get('res')
#             li_list = res2.xpath('//ul[@class="row-fluid list-row js-car-list"]/li')
#             if li_list:
#                 page = response.meta.get('page', 2)
#                 url = response.url
#                 url = re.sub(r'p\d+','',url)
#                 car_url = url + 'p{page}/'
#                 yield Request(car_url.format(page=page), meta={'page':page+1}, callback=self.parse)
#
import re
from scrapy_redis.spiders import RedisSpider
from scrapy import Selector, Request

# from renrenchesipder.items import MasterItem


class RenRenCheSipder(RedisSpider):
    name = 'renrenche'

    # 网站域名
    domain_url = 'https://www.renrenche.com'
    # 设置过滤爬取的域名
    allowed_domains = ['www.renrenche.com']

    def start_requests(self):
        yield Request(self.domain_url)

    # 解析所有城市
    def parse(self, response):
        res = Selector(response)
        city_url_list = res.xpath('//div[@class="area-city-letter"]/div/a[@class="province-item "]/@href')
        for city_url in city_url_list:
            city = city_url.extract()
            yield Request(self.domain_url + city, callback=self.parse_brand)

    # 解析所有的品牌
    def parse_brand(self, response):
        res = Selector(response)
        brand_url_list = res.xpath('//*[@id="brand_more_content"]/div/p/span/a')
        for a in brand_url_list:
            band_url = a.xpath('./@href').extract()[0]
            yield Request(self.domain_url + band_url, callback=self.parse_page_url)

    # 解析某个品牌下面的具体某辆车的页面
    def parse_page_url(self, response):
        # 实例化管道
        item = ErshoucheItem()
        res = Selector(response)
        # 获取到页面的所有li的信息 用于下面的页码的判断
        li_list = res.xpath('//ul[@class="row-fluid list-row js-car-list"]/li')
        # 判断页面
        # 判断页面是否有li标签
        if li_list:
            for c in li_list:
                # 获取页面的每个车的url 并且过滤掉有广告的那个a标签
                one_car_url = c.xpath('./a[@class="thumbnail"]/@href').extract()
                # 判断是否有这个url
                if one_car_url:
                    url = self.domain_url + one_car_url[0]
                    yield Request(url=url,callback=self.parse_car)

            # 下一页信息
            page = response.meta.get('page', 2)
            #
            url = response.url
            # 替换掉上面的结果出现../p1/p2/这样的结果我们只需要一个页面参数
            url = re.sub(r'p\d+', '', url)
            # 产生新的页面url
            car_info_url = url + 'p{page}/'
            # 回调 获取下一页
            yield Request(car_info_url.format(page=page), meta={'page': page + 1}, callback=self.parse_page_url)

    def parse_car(self, response):
        sel = Selector(response)
        carinfo = sel.xpath('//*[@id="basic"]/div[2]/div[2]/div[1]')
        if carinfo.xpath('./div/h1/text()').extract():
            title = carinfo.xpath('./div/h1/text()').extract()[0]
            price = carinfo.xpath('./div[3]/div[1]/p/text()').extract()[0] + '万'
            souhu = carinfo.xpath('./div[3]/div[3]/p[2]/text()').extract()
            yuegong = carinfo.xpath('./div[3]/div[3]/p[3]/text()').extract()
            lichen = carinfo.xpath('./div[4]/ul/li[1]/div/p/strong/text()').extract()[0]
            cheling = carinfo.xpath('./div[4]/ul/li[2]/div//p/strong/text()').extract()
            chepaididian = carinfo.xpath('./div[4]/ul/li[3]/div/p/strong/text()').extract()[0]
            item = ErshoucheItem()
            item['title'] = title
            item['price'] = price
            item['souhu'] = souhu
            item['yuegong'] = yuegong
            item['lichen'] = lichen
            item['cheling'] = cheling
            item['chepaididian'] = chepaididian
            yield item