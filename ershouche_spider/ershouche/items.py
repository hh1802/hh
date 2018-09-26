# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ErshoucheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    souhu = scrapy.Field()
    yuegong = scrapy.Field()
    lichen = scrapy.Field()
    cheling = scrapy.Field()
    chepaididian = scrapy.Field()
    url = scrapy.Field()
