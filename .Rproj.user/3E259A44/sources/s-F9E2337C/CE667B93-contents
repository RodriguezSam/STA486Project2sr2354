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
for h in headers:
    print(h.text)
print(rows)
print(cols)

df = pd.DataFrame(columns=[h.text for h in headers])
df.head()

for r in range(2,rows+1):
    for c in range(1,cols+1):
        value = driver.find_element(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody[1]/tr").text

print(value, end="  ")
print(len(value))

#driver.find_elements(by=By.ID, value="insertedTable")
driver.quit()

#soup = BeautifulSoup(page.content, "html.parser")

#results = soup.find(id="iframe1")

#print(results.prettify())



