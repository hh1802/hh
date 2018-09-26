import urllib.request
from urllib import parse

def baidu_api(search):
    url = 'https://www.baidu.com/s?' + search
    header = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'

    }
    res = urllib.request.Request(url=url, headers=header)
    r = urllib.request.urlopen(res)
    print(r.read().decode('utf-8'))

if __name__ == '__main__':
    search = input('请输入搜索的数据')
    wd = parse.urlencode({'wd':search})
    baidu_api(wd)
