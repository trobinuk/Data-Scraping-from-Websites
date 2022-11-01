from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
#from webdriver_manager import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.newbalance.com/men/shoes/all-shoes/?start=0&sz=168')

while True:
    try:
        last_height = driver.execute_script('return document.body.scrollHeight')-1800
        print(last_height)
        driver.execute_script('window.scrollTo(0,'+str(last_height)+')')
        driver.find_element(by=By.XPATH,value='//*[@id="btn-loadMore"]').click()
        time.sleep(8)
    except Exception as e:
        print(e)
        break

soup = BeautifulSoup(driver.page_source,'lxml')

prod_list = soup.find_all('div',class_ = 'product w-100')
print('The prod_list is '+str(len(prod_list)))

df = pd.DataFrame({'name':[''],'desc':[''],'price':['']})

for product in prod_list:
    name = product.find('a',class_='link font-weight-bold pname text-underline no-underline-lg').text    
    desc = product.find('span',class_="category-name font-body w-100 d-block pt-2").text
    try:
        price = str(product.find('span',class_="price-value").find('span',class_='sales font-body-large').text)
    except:
        price = 'NA'
    df = df.append({'name':name,'desc':desc,'price':price},ignore_index=True)


#driver.execute_script('window.scrollTo(0,'+str(last_height)+')')

#driver.find_element(by=By.XPATH,value='//*[@id="btn-loadMore"]').click()

#print(soup.find('button',class_= 'nb-button button-large button-secondary bold button-full-width-mobile col-12 col-lg-3 more').get('data-url'))