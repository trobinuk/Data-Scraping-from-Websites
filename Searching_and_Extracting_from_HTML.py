# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 09:19:29 2022

@author: trobi
"""

import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')

soup.header

#find
soup.find('header')

#print(soup.find('div',{'class':'container'}))

#print(soup.find('h4',{'class':'pull-right price'}))

#print(soup.find('h4',class_ = 'pull-right price'))

#find_all() 

#print(soup.find_all('h4',class_ = 'pull-right price'))

#[print(x) for x in soup.find_all('h4',class_ = 'pull-right price')]

#print(soup.find_all('a',class_ = 'title')[6:])

#[print(review) for review in soup.find_all('p',class_="pull-right")]

#Part-2 find_all()

#print(soup.find_all(['h4','p']))

#print(soup.find_all(id = True))

#print(soup.find_all(string = 'Iphone'))

#print(soup.find_all(string = ['Iphone','Nokia X']))

import re

#print(soup.find_all(string = re.compile('Iph')))

#print(soup.find_all(string = re.compile('Nok')))

#print(soup.find_all(class_ = re.compile('pull')))

#print(soup.find_all('p',class_ = re.compile('pull')))

#print(soup.find_all('p',class_ = re.compile('pull'),limit = 3))

#part-3 find_all()
'''
titles = soup.find_all('a',class_ = 'title')

prices = soup.find_all('h4',class_ = 'pull-right price')

reviews = soup.find_all('p',class_ = re.compile('pull'))

descriptions = soup.find_all('p',class_ = 'description')

print(titles)

title_list = []
price_list = []
review_list = []
description_list = []

for title in titles:
    title_list.append(title.text)
    
for price in prices:
    price_list.append(price.text)
    
for review in reviews:
    review_list.append(review.text)
    
for description in descriptions:
    description_list.append(description.text)
    
print(title_list)
print(price_list)
print(review_list)
print(description_list)

import pandas as pd

table = pd.DataFrame({'title':title_list,'price':price_list,
                      'review':review_list,'description':description_list})
print(table.head)'''

#Nested HTML Tags

#print(soup.find_all('div',class_ = 'col-sm-4 col-lg-4 col-md-4')[2])

#box = soup.find_all('div',class_ = 'col-sm-4 col-lg-4 col-md-4')[2]

#print(box.find('a').text)

#print(box.find('p',class_ = 'description').text)

#box2 = soup.find_all('ul',class_ = 'nav',id = 'side-menu')[0]

#print(box2.find_all('li')[1].text)

#Coding Exercise Stock Prices

url = 'https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol'

page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')

val = soup.find('h2','intraday__price')

print(val.find('bg-quote').text)

val_prev_day = soup.find_all('div',class_ = 'intraday__close')[0]

print(val_prev_day.find('td').text)

val_range_head = soup.find_all('div',class_='range__header')[-1]

print(val_range_head.find_all('span',class_ = 'primary')[0].text)
print(val_range_head.find_all('span',class_ = 'primary')[1].text)

val_act = soup.find('li',class_="analyst__option active").text
print(val_act)

#[print(i) for i in val]
