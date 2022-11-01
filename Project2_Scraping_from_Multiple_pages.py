# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 08:06:48 2022

@author: trobi
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.airbnb.com/s/Honolulu--Oahu--Hawaii--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&query=Honolulu%2C%20Oahu%2C%20HI&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&date_picker_type=calendar&checkin=2022-08-02&checkout=2022-08-09&source=structured_search_input_header&search_type=autocomplete_click'

page_number = 1
while True:
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'lxml')
        
        posting_number = 1
        postings = soup.find_all('div',class_ = 'c4mnd7m dir dir-ltr')
        post_number = []
        link = []
        title = []
        price = []
        rating = []
        details = []
        for post in postings:
            post_number.append(posting_number)
            link.append('https://www.airbnb.com'+post.find('a',class_ = 'ln2bl2p dir dir-ltr').get('href'))
            title.append(post.find('meta',{'itemprop':'name'}).get('content'))
            price.append(post.find('span',class_ = "_tyxjp1").text)
            rating.append(post.find('span',class_ = 't5eq1io r4a59j5 dir dir-ltr').get('aria-label'))
            details.append(post.find('div',class_ = 'f15liw5s s1cjsi4j dir dir-ltr').find('span').get('aria-label'))
            posting_number += 1
        
        df = pd.DataFrame({'Post Number':post_number,'Link':link,
                           'Title':title,'Price':price,'Ratings':rating,'Details':details})
        #break
        path = 'C:\\Users\\trobi\\Desktop\\Projects\\Data_Mining\\Airbnb.xlsx'
        if page_number == 1:
            df.to_excel(path,sheet_name= f'page_{page_number}',index=False)
        else:
            with pd.ExcelWriter(path,mode='a',engine='openpyxl',if_sheet_exists='replace') as writer:
                df.to_excel(writer, sheet_name=f'page_{page_number}',index=False)
                
        try:
            next_page = soup.find('a',{'aria-label': "Next"}).get('href')
        except:
            break
        
        url = 'https://www.airbnb.com'+next_page
        page_number += 1
    except:
        pass
    

'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.airbnb.com/s/Honolulu--Oahu--Hawaii--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&query=Honolulu%2C%20Oahu%2C%20HI&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&date_picker_type=calendar&checkin=2022-08-02&checkout=2022-08-09&source=structured_search_input_header&search_type=autocomplete_click'

page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')
#print(soup)  cy5jw6o  dir dir-ltr  cy5jw6o  dir dir-ltr
cnt = 0
for i in soup.find_all('div',class_ = 'c4mnd7m dir dir-ltr'): 
    cnt += 1
    print(cnt,'   ','https://www.airbnb.com'+i.find('a',class_ = 'ln2bl2p dir dir-ltr').get('href'))#.get('href')
    print(i.find('meta',{'itemprop':'name'}).get('content'))
    print(i.find('span',class_ = "_tyxjp1").text)   
'''
#print(soup.find_all('a',{'aria-hidden':("false","true")},{'tabindex':'-1'},class_ = 'rfexzly dir dir-ltr'))
'''links = []
cnt = 0
for i in soup.find_all('a',{'aria-hidden':("false","true")},{'tabindex':'-1'},class_ = 'rfexzly dir dir-ltr'):
    cnt += 1
    links.append('https://www.airbnb.com'+i.get('href'))

links_set = set(links)
links_of_room = list(links_set)
[print(i) for i in links_of_room]'''
    #print(cnt,'  ',i.find())
    #print(cnt,'  ','https://www.airbnb.com'+i.get('href'))

#print(soup)

#Part-2
'''
next_page = soup.find('a',{'aria-label': "Next"}).get('href')
#print(next_page)
next_page_full = 'https://www.airbnb.com'+next_page
print(next_page_full)

url = next_page_full

page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')'''
'''
cnt = 0
while True:
    try:
        next_page = soup.find('a',{'aria-label': "Next"}).get('href')
    except:
        break
    next_page_url = 'https://www.airbnb.com'+next_page
    
    page = requests.get(next_page_url)
    soup = BeautifulSoup(page.text,'lxml')
    cnt += 1
    print(cnt,'  ',next_page_url)
    '''