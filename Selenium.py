# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 08:35:08 2022

@author: trobi
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#driver = webdriver.Chrome('C:\\Program Files\\Python310\\chromedriver.exe')

driver.get('https://www.goat.com/sneakers')
#driver.get('https://www.google.com/')
'''from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")'''

print(driver.find_element(by =By.XPATH,value='//*[@id="grid-body"]/div/div[1]/div[6]/a/div[1]/div[2]/div/div/span').text)
#print(driver.find_element(by = By.XPATH,value = '//*[@id="grid-body"]/div/div[1]/div[2]/a/div[1]/div[2]').get_attribute("textContent"))

print(driver.find_element(by = By.XPATH,value = '//*[@id="grid-body"]/div/div[1]/div[2]/a/div[1]/div[2]').text)
#print(price)

#driver.find_element(by = By.XPATH,value = '//*[@id="__next"]/div/header[1]/header/nav/ul/li[1]/div/a').click()
'''
for i in range(1,30):
    print(driver.find_element(by = By.XPATH,value ='//*[@id="grid-body"]/div/div[1]/div['+str(i)+']/a/div[1]/div[2]/div').text)
'''