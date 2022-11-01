# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:06:59 2022

@author: trobi
"""
from bs4 import BeautifulSoup
import pandas as pd
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://www.indeed.com/?from=gnav-jobsearch--jasx'
driver.get(url)
time.sleep(2)
job_input_box = driver.find_element(by=By.XPATH,value='//*[@id="text-input-what"]')
job_input_box.send_keys('Data Engineer')
job_input_box.send_keys(Keys.TAB)

location_box = driver.find_element(by=By.XPATH,value='//*[@id="text-input-where"]')
location_box.send_keys(Keys.CONTROL+"A")
location_box.send_keys(Keys.BACKSPACE)
location_box.send_keys('Austin, Tx')
location_box.send_keys(Keys.TAB)
driver.find_element(by=By.XPATH,value='//*[@id="jobsearch"]/button').click()

soup = BeautifulSoup(driver.page_source,'lxml')

#print(len(job_listings))
title = []
link = [ ]
comp_name = ''
company_name = []
company_location = []
sal = ''
salary = []
posted_before = []
while True:
    
    job_listings = soup.find_all('td',class_='resultContent')
    for job in job_listings:
        title.append(job.find('span').get('title'))
        link.append('https://www.indeed.com'+job.find('a',class_='jcs-JobTitle css-jspxzf eu4oa1w0').get('href'))
        try:
            comp_name = job.find('a',class_='turnstileLink companyOverviewLink').text
        except:
            comp_name = job.find('span',class_="companyName").text
        company_name.append(comp_name)
        company_location.append(job.find('div',class_='companyLocation').text)
        try:
            sal = job.find('div',class_='attribute_snippet').text
        except:
            sal = 'NA'
        salary.append(sal)
        
    days_listings = soup.find_all('table',class_='jobCardShelfContainer big6_visualChanges')
    for days in days_listings:
        try:
            day_final = days.find('span',class_='date').text
            day_final = day_final.replace('PostedPosted ','')
            day_final = day_final.replace('EmployerActive ','')
            posted_before.append(day_final)
        except:
            posted_before.append('posted')
    try:        
        url = soup.find('a', {'aria-label':'Next'}).get('href')
        driver.get('https://www.indeed.com'+url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source,'lxml')
    except:
        break

    
df = pd.DataFrame({'Title':title,'Link':link,'Company Name':company_name,'Company Location':company_location,
                   'Salary':salary,'Posted Before':posted_before})

df.to_csv('C:\\Users\\trobi\\Desktop\\Projects\\Data_Mining\\Indeed.csv')

##############################################################################
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

sender = 'trobinuk@gmail.com'
receiver = 'trobinuk@gmail.com'

msg = MIMEMultipart()
msg['Subject'] = 'New Jobs on Indeed'
msg['From'] = sender
msg['To'] = receiver

part = MIMEBase('application','octet-stream')
part.set_payload(open ('C:\\Users\\trobi\\Desktop\\Projects\\Data_Mining\\Indeed.csv','rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename = "Indeed.csv"')
msg.attach(part)

s = smtplib.SMTP_SSL(host='smtp.gmail.com',port=465)#465
s.login(user = 'trobinuk@gmail.com',password='crzwaywbnlbwczlo')
s.sendmail(sender,receiver,msg.as_string())
s.quit()