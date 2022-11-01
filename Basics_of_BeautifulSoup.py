# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 08:49:03 2022

@author: trobi
"""

import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

page = requests.get(url)

#print(page.text)
soup = BeautifulSoup(page.text,'lxml')

#print(soup)

#Tags
soup.header
soup.div
print(soup.div)

#Navigable Strings
tag = soup.header.p
print(tag)
print(tag.string)
soup.header

#Attributes

tag = soup.header.a
print(tag)
print(tag.attrs)
print(tag['data-target'])
#tag['attribute-new'] = 'this is a NEWly added attribute'
#print(tag.attrs)