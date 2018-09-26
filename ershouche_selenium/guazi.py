from selenium import webdriver
import time

chromdriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromdriver)
browser.get('https://www.guazi.com/cd/dazhong/')
list_href = browser.find_element_by_xpath('/html/body/div[4]/ul/li[1]/a/@href')
hrefs = []
for href in list_href:
    print(hrefs.append(href))

