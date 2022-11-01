# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:43:05 2022

@author: trobi
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = 'https://www.carpages.ca/used-cars/search/?num_results=50&year_start=2008&year_end=2018&price_amount_start=4000&price_amount_end=18000&category_id=6&sort=price_asc&sale_type=used&p=1'
url_init = 'https://www.carpages.ca'
page_number = 1
while page_number <= 16:
    
    page = requests.get(url)
    
    soup = BeautifulSoup(page.text,'lxml')
    
    postings = soup.find_all('div',class_ = 'media soft push-none rule')
    post_num = 1
    
    title = []
    link = []
    model = []
    price = []
    agency = []
    kms_run = []
    location = []
    for post in postings:
        try:
            try:
                model_value = str(post.find('h5',class_='hN grey').text)
            except:
                model_value = 'NA'
            model.append(model_value)
            price.append(re.sub("^\s+|\s+$", "", post.find('strong').text, flags=re.UNICODE))
            agency.append(post.find('hgroup',class_='vehicle__card--dealerInfo').find('h5').text)
            location.append(post.find('hgroup',class_='vehicle__card--dealerInfo').find('p').text)
            link.append(url_init+post.find('h4',class_='hN').find('a').get('href'))
            title.append(post.find('h4',class_='hN').find('a').get('title'))
            kms_str = ""
            for i in post.find(class_="grey l-column l-column--small-6 l-column--medium-4"):
                kms_str = kms_str+str(i.text)
            kms_run.append(re.sub("^\s+|\s+$", "",kms_str, flags=re.UNICODE))
            #[print(i.find('span').text) for i in post.find(class_="grey l-column l-column--small-6 l-column--medium-4")]
            
        except:
            print('v  ',model_value)
            print(post)
            #break
            pass
        #print(post_num)
        post_num += 1
    #print(len(link),' ',len(title),' ',len(model),' ',len(price),' ',len(kms_run),' ',len(agency),' ',len(location))
    #print(link,'  ',title,model,price,kms_run,agency,location)
        #break
    df = pd.DataFrame({'Title':title,'Link':link,'Model':model,'Price':price,'Agency':agency,'KMs_Rum':kms_run,'Location':location})
    #break
    path = 'C:\\Users\\trobi\\Desktop\\Projects\\Data_Mining\\Carpages.xlsx'
    if page_number == 1:
        df.to_excel(path,sheet_name=f'Page{page_number}',index=False)
    else:
        with pd.ExcelWriter(path,mode='a',engine='openpyxl',if_sheet_exists='replace') as writer:
            df.to_excel(writer,sheet_name=f'Page{page_number}',index=False)
    url = url_init+soup.find('a',{'title':'Next Page'},class_="nextprev").get('href')
    print(page_number,'  ',url)
    page_number += 1

