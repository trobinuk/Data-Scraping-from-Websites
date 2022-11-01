# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:24:37 2022

@author: trobi
"""
'''
google
box type = 'top 100 movies of all time'

go to imbd webpage 

Then create a wait time for 10 s

then do self scroll all the way down to 50 th best movie of all time

then take a screenshot of actual page

and then another screenshot where you take just the poster of that movie'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.google.com/')

box = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

box.send_keys('Top 100 movies of all time')

box.send_keys(Keys.ENTER)

driver.find_element(by=By.XPATH,value='//*[@id="rso"]/div[1]/div/div[1]/div/a/h3').click()
time.sleep(3)


#element = WebDriverWait(driver, 120).until(
 #   EC.presence_of_element_located((By.ID,'cntsdd')))

driver.execute_script('window.scrollTo(0,22500)')

    
#time.sleep(15)
#Screenshot 1
driver.find_element(by=By.XPATH,value='//*[@id="main"]/div/div[4]/div[3]/div[50]/div[1]/a/img').screenshot('C:\\Users\\trobi\\Desktop\\Projects\\Data_Mining\\Movie_Screenshot.png')
#Click Click Screenshot 2
driver.find_element(by=By.XPATH,value='//*[@id="main"]/div/div[4]/div[3]/div[50]/div[1]/a/img').click()

driver.find_element(by=By.XPATH,value='//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div/div[1]/div/div/a').click()

#driver.find_element(by=By.XPATH,value='//*[@id="iconContext-clear"]').click()

driver.save_screenshot('C:\\Users\\trobi\\Desktop\\Projects\\Data_Mining\\Movie_Poster_Screenshot.png')