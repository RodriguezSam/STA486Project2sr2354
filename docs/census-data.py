import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd

# initiate connection
driver = webdriver.Chrome()
URL = "https://data.census.gov/cedsci/table"
driver.get(URL)

# wait for website to load
time.sleep(10)

geography = driver.find_element(by=By.XPATH,
                                value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/section[1]/ul[1]/li[2]")
geography.click()
time.sleep(5)
county = driver.find_element(by=By.XPATH,
                             value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/div[2]/div[2]/div[1]/div[3]")
county.click()
time.sleep(5)
arizona = driver.find_element(by=By.XPATH,
                              value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/ul[1]/li[5]")
arizona.click()
time.sleep(5)
allCounties = driver.find_element(by=By.XPATH,
                                  value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/ul[1]/li[1]")
allCounties.click()
time.sleep(5)
surveys = driver.find_element(by=By.XPATH,
                                value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/section[1]/ul[1]/li[3]")
surveys.click()
time.sleep(5)
acs = driver.find_element(by=By.XPATH,
                             value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/ul[1]/li[1]")
acs.click()
time.sleep(5)
oneYear = driver.find_element(by=By.XPATH,
                             value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/ul[1]/li[1]")
oneYear.click()
time.sleep(5)
dataProfiles = driver.find_element(by=By.XPATH,
                             value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/ul[1]/li[2]")
dataProfiles.click()
time.sleep(5)
years = driver.find_element(by=By.XPATH,
                                value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/section[1]/ul[1]/li[5]")
years.click()
time.sleep(5)
yearList = driver.find_elements(by=By.XPATH,
                                value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/ul[1]/li")
#years.click()
for y in yearList:
    print(y)
time.sleep(5)
#print(acs.text)

# close out of the session
driver.quit()

