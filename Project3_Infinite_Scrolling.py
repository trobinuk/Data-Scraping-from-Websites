# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 10:38:39 2022

@author: trobi
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import requests

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.nike.com/w/sale-3yaep')


last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    print('The last height is '+str(last_height)+'  '+str(new_height),' is the new_height')
    if last_height == new_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source,'lxml')

prod_list = soup.find_all('div',class_='product-card__body')
#                                      product-card css-1v1uza4 css-z5nr6i css-11ziap1 css-14d76vy css-dpr2cn product-grid__card 
#product-card product-grid__card  css-1ipmndw
df = pd.DataFrame({'Link':[''],'Name':[''],'Subtitle':[''],'Sale_price':[''],'Price':['']})
for product in prod_list:
    try:
        link = product.find('a',class_='product-card__link-overlay').get('href')
        name = product.find('div',class_='product-card__title').text
        subtitle = product.find('div',class_='product-card__subtitle').text
        sale_price = product.find('div',class_='product-price is--current-price css-s56yt7').text #product-price is--current-price css-1ydfahe
        price = product.find('div',class_='product-price is--striked-out').text
        print(link,name,subtitle,price,sale_price)
        #print(product.find('a',class_='product-card__link-overlay').get('href'))
        df = df.append({'Link':link,'Name':name,'Subtitle':subtitle
                        ,'Sale_price':sale_price
                        ,'Price':price
                        },
                       ignore_index=True)
    except:
        pass
    
#print(soup)

#print(len(prod_list))





    




