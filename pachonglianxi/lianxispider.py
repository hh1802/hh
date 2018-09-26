# import urllib.request
# import requests
# header ={
#     'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
# }
# proxy = {
#     'http': '120.25.253.234:812',
#     'https':'163.125.222.244:8123'
# }
#
# data = {'name':'tom','age':'22'}
#
# response = requests.post('http://httpbin.org/post', data=data)
# # data = {'name':'tom','age':'22'}
# # reponse = requests.get('http://www.baidu.com',allow_redirects=True, proxies=proxy,data=data)
# print(response.text)
# # r =requests.head('http://httpbin.org/get')
# # response = requests.get('http://httpbin.org/get?name=gemey&age=22')
# # print(response.text)
# # print(r)
# # print(reponse.url)
# # print(reponse.headers)
# # print(reponse.status_code)
# # print(reponse.cookies)
# # print(reponse.history)
# # # print(reponse.text)
# # print(reponse)
#
#
# # res = urllib.request.Request('https://www.baidu.com',headers=header)
# # r = urllib.request.urlopen(res)
# #
# # print(r.read().decode('utf-8'))
#
#
# import requests
# session = requests.Session()
# session.get('http://httpbin.org/cookies/set/number/12345')
# response = session.get('http://httpbin.org/cookies')
# print(response.text)




import tessercor


