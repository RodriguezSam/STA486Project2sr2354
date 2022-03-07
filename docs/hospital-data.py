import urllib.request

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()

URL = "https://gis.azdhs.gov/ephtexplorer/"
driver.get(URL)

#soup = BeautifulSoup(page.content, "html.parser")

#results = soup.find(id="iframe1")

#print(results.prettify())



