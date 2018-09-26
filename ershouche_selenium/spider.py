from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromdriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromdriver)
timeout = 40
browser.set_page_load_timeout(timeout)
wait = WebDriverWait(browser, timeout)
browser.get('https://www.guazi.com/cd/dazhong/')

list_href = wait.until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/ul/li[1]/a/@href')))
print(list_href)


browser.close()
