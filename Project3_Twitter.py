# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 15:30:45 2022

@author: trobi
"""
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

user_name = 'robinso80625423'
password = 'Roderick!3'
celebrity_name  = 'The Rock'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://twitter.com/login')
time.sleep(3)
user_box = driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
user_box.send_keys(user_name)
user_box.send_keys(Keys.TAB)
user_box.send_keys(Keys.ENTER)
'''
password_box = driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
#password_box = driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
time.sleep(8)
password_box.send_keys(password)
password_box.send_keys(Keys.TAB)
password_box.send_keys(Keys.TAB)
driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div').click()
'''
#                                      //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div 
time.sleep(15)
search_box = driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')
search_box.send_keys(celebrity_name)
search_box.send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div/span').click()
time.sleep(2)
driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span').click()
tweets = []
tweet_distinct  = []
soup = BeautifulSoup(driver.page_source,'lxml')
#print(soup)
tweets_list = soup.find_all('div',class_='css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')

#driver.execute_script('window.scrollTo(0,6000)')
height = 3000
try:
    while True:
        for tweet in tweets_list:
            tweet_text = ''
            for i in tweet.find_all('span',{'class': ['r-18u37iz','css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']}):
                tweet_text = tweet_text+i.text
            tweets.append(tweet_text)
            
        driver.execute_script('window.scrollTo(0,'+str(height)+')')
        height += 3000
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source,'lxml')
        #print(soup)
        tweets_list = soup.find_all('div',class_='css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')   
        if len(tweet_distinct) > 100:
            break
        tweet_distinct = list(set(tweets))
except:
    pass
df = pd.DataFrame({'Tweets':tweet_distinct})
print(tweet_distinct)

    
'''print(len(tweet_list))
[print(i.text) for i in tweet_list[0].find_all('span',class_='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')]
[print(i.text) for i in tweet_list[0].find_all('span',class_='r-18u37iz')]
[print(i.text) for i in tweet_list[0].find_all('span',{'class': ['r-18u37iz','css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']})]

tweet1 = []
for tweet in tweets_list:
    tweet1.append([i.text for i in tweet.find_all('span',{'class': ['r-18u37iz','css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']})])
    
print(tweet1)'''


 