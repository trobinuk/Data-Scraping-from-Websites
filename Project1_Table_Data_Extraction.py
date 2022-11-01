# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:27:36 2022

@author: trobi
"""
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'

page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')

table_values = soup.find('table',class_="table table-striped table-bordered table-hover table-condensed table-list")

table_values.find_all('th')
#print(table_population_headers)

table_headers = []

[table_headers.append(i.text) for i in table_values.find_all('th')]

#print(table_headers)

df = pd.DataFrame(columns = table_headers)

for j in table_values.find_all('tr')[1:]:
    row_data = j.find_all('td')
    #break
    #print(row_data)
    row = [x.text for x in row_data]
    #print(row)
    length = len(df)
    df.loc[length] = row
    
df.to_csv('C:\\Users\\trobi\\Desktop\\Projects\\Data_Mining\\Scraped_data_Population.csv')
    
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nfl.com/standings/league/2019/REG'

page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')
table_values = soup.find('table',
class_="d3-o-table d3-o-table--row-striping d3-o-table--detailed d3-o-standings--detailed d3-o-table--sortable {sortlist: [[4,1]], sortinitialorder: 'desc'}")

#print(table_values.find_all('th'))
table_headers= []

[table_headers.append(i.text.strip()) for i in table_values.find_all('th')]

#print(table_headers)

df1 = pd.DataFrame(columns = table_headers)

#print(table_values.find_all('tr')[1:])
for j in table_values.find_all('tr')[1:]:
    first_td_data = j.find_all('td')[0].find('div',class_ = 'd3-o-club-fullname').text.strip()
    #print(first_td_data)
    row_data = j.find_all('td')[1:]
    row = [x.text.strip() for x in row_data]
    row.insert(0,first_td_data)
    length = len(df1)
    df1.loc[length] = row