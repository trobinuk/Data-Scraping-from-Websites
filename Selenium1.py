from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#driver = webdriver.Chrome('C:\\Program Files\\Python310\\chromedriver.exe')
'''
driver.get('https://www.google.com/')

box = driver.find_element(by = By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('web scraping')
box.send_keys(Keys.TAB)
#box.send_keys(Keys.ENTER)
#print(box)

#Clicking on a button
button = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

#driver.find_element(by=By.XPATH,value='//*[@id="rso"]/div[1]/div/div/div[1]/div/a/h3').click()

#driver.find_element(by=By.XPATH,value='//*[@id="mw-content-text"]/div[1]/p[1]/a[1]').click()

#Taking a Screenshot
#driver.save_screenshot('C:\\Users\\trobi\\Desktop\\Projects\\Data_Mining\\screenshot.png')

driver.find_element(by=By.XPATH,value='//*[@id="rso"]/div[1]/div/div/div[1]/div/a/h3').screenshot('C:\\Users\\trobi\\Desktop\\Projects\\Data_Mining\\screenshot2.png')
'''
driver.get('https://www.google.com/')

box = driver.find_element(by = By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('giraffe')
box.send_keys(Keys.ENTER)

driver.find_element(by = By.XPATH,value='//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()

#driver.find_element(by = By.XPATH,value='//*[@id="islrg"]/div[1]/div[2]/a[1]/div[1]/img').screenshot('C:\\Users\\trobi\\Desktop\\Projects\\Data_Mining\\giraffe.png')

#Self Scrolling
#print(driver.execute_script('return document.body.scrollHeight'))
#driver.execute_script('window.scrollTo(0,3270)')

#driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.google.com/')

box = driver.find_element(by = By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('giraffe')
box.send_keys(Keys.ENTER)


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.ID,'cntsdd')))

driver.find_element(by = By.XPATH,value='//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()