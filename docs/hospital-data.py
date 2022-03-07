import time
import urllib.request

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

URL = "https://gis.azdhs.gov/ephtexplorer/"
driver.get(URL)
time.sleep(20)
driver.switch_to.frame("iframe1")
rows = 1 + len(driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody[1]/tr"))
cols = len(driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/thead[1]/tr[1]/th")) - 1
headers = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/thead[1]/tr[1]/th")
headers.pop(0)
# for h in headers:
#     print(h.text)

df = pd.DataFrame(columns=[h.text for h in headers])

counties = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody[1]/tr")
# for index, s in enumerate(counties):
#     print('row {}:'.format(index))
#     print('{}'.format(s.text))

col1 = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[2]")
col2 = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[3]")
col3 = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[4]")

# print(col1, end='\n')

df[df.columns[0]] = [s.text for s in col1]
df[df.columns[1]] = [s.text for s in col2]
df[df.columns[2]] = [s.text for s in col3]

df.to_csv('hospital_data.csv')

driver.quit()



