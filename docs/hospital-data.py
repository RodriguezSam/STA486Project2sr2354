import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd

# initiate connection
driver = webdriver.Chrome()
URL = "https://gis.azdhs.gov/ephtexplorer/"
driver.get(URL)

# wait for website to load
time.sleep(20)

# switch to iframe page
driver.switch_to.frame("iframe1")

# initate data frame
df = pd.DataFrame()

# collect the content area filters
contentIndex = [1, 4, 6, 10, 12, 14, 15, 16, 18]
contentArea = Select(driver.find_element(by=By.XPATH,
                                         value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/select"))
contentList = driver.find_elements(by=By.XPATH,
                                   value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/select")
content = []
for index in contentList:
    content.append(index.text)
content = content[0].splitlines()

# loop through all the content
for cont in contentIndex:
    # switch contents
    contentArea.select_by_visible_text(content[cont])
    time.sleep(10)
    # collect all the years for the content
    options = Select(driver.find_element(by=By.XPATH,
                                         value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/select"))
    yearList = driver.find_elements(by=By.XPATH,
                                    value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/select")
    years = []
    for index in yearList:
        years.append(index.text)
    years = years[0].split()
    # loop through the years
    for yr in years:
        # switch years
        options.select_by_visible_text(yr)
        time.sleep(10)
        # fill an empty dataframe
        if df.empty:
            rows = 1 + len(driver.find_elements(by=By.XPATH,
                                                value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody[1]/tr"))
            cols = len(driver.find_elements(by=By.XPATH,
                                            value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/thead[1]/tr[1]/th")) - 1
            headers = driver.find_elements(by=By.XPATH,
                                           value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/thead[1]/tr[1]/th")
            headers.pop(0)
            df = pd.DataFrame(columns=[h.text for h in headers])
            col1 = driver.find_elements(by=By.XPATH,
                                        value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[2]")
            col2 = driver.find_elements(by=By.XPATH,
                                        value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[3]")
            col3 = driver.find_elements(by=By.XPATH,
                                        value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[4]")
            col4 = [yr] * (rows - 1)
            col5 = [content[cont]] * (rows - 1)
            df[df.columns[0]] = [s.text for s in col1]
            df[df.columns[1]] = [s.text for s in col2]
            df[df.columns[2]] = [s.text for s in col3]
            df['Year'] = col4
            df['Content.Area'] = col5
        # concatenate data frames
        else:
            rows = 1 + len(driver.find_elements(by=By.XPATH,
                                                value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody[1]/tr"))
            cols = len(driver.find_elements(by=By.XPATH,
                                            value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/thead[1]/tr[1]/th")) - 1
            headers = driver.find_elements(by=By.XPATH,
                                           value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/thead[1]/tr[1]/th")
            headers.pop(0)
            newDf = pd.DataFrame(columns=[h.text for h in headers])
            col1 = driver.find_elements(by=By.XPATH,
                                        value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[2]")
            col2 = driver.find_elements(by=By.XPATH,
                                        value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[3]")
            col3 = driver.find_elements(by=By.XPATH,
                                        value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[4]")
            col4 = [yr] * (rows - 1)
            col5 = [content[cont]] * (rows - 1)
            newDf[newDf.columns[0]] = [s.text for s in col1]
            newDf[newDf.columns[1]] = [s.text for s in col2]
            newDf[newDf.columns[2]] = [s.text for s in col3]
            newDf['Year'] = col4
            newDf['Content.Area'] = col5
            df = pd.concat([df, newDf], ignore_index=True)

# create csv file
df.to_csv('hospital_data.csv')

# close out of the session
driver.quit()

#######################################################################################################################

# # find year option
# #years = ["2019", "2018", "2017", "2016", "2015"]
# options = Select(driver.find_element(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/select"))
# yearList = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/select")
# years = []
# for index in yearList:
#     years.append(index.text)
# years = years[0].split()
# options.select_by_visible_text(years[2])
# time.sleep(20)
# # for o in years:
# #     print(type(o))
#
# # find content area option
# contentArea = Select(driver.find_element(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/select"))
# contentList = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/select")
# content = []
# for index in contentList:
#     content.append(index.text)
# content = content[0].splitlines()
# #print(content)
# contentArea.select_by_visible_text(content[1])
# time.sleep(20)
#
# # count the number of columns and rows
# rows = 1 + len(driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody[1]/tr"))
# cols = len(driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/thead[1]/tr[1]/th")) - 1
#
# # get the column names and remove the first one
# headers = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/thead[1]/tr[1]/th")
# headers.pop(0)
# # for h in headers:
# #     print(h.text)
#
# # create data frame with column names
# df = pd.DataFrame(columns=[h.text for h in headers])
#
# # get the elements for each column
# # counties = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody[1]/tr")
# # for index, s in enumerate(counties):
# #     print('row {}:'.format(index))
# #     print('{}'.format(s.text))
# col1 = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[2]")
# col2 = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[3]")
# col3 = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[4]")
# col4 = [years[2]] * (rows - 1)
# col5 = [content[1]] * (rows - 1)
#
#
# # print(col1, end='\n')
#
# # put elements into the data frame
# df[df.columns[0]] = [s.text for s in col1]
# df[df.columns[1]] = [s.text for s in col2]
# df[df.columns[2]] = [s.text for s in col3]
# df['Year'] = col4
# df['Content.Area'] = col5
#
# newDf = pd.DataFrame(columns=[h.text for h in headers])
# options.select_by_visible_text(years[3])
# time.sleep(3)
# col1 = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[2]")
# col2 = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[3]")
# col3 = driver.find_elements(by=By.XPATH, value="html/body/div[@id='main-page']/div[@id='jimu-layout-manager']/div/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='ValuesTable']/div[@id='insertedTable_wrapper']/table[@id='insertedTable']/tbody/tr/td[4]")
# col4 = [years[3]] * (rows - 1)
# col5 = [content[1]] * (rows - 1)
# newDf[newDf.columns[0]] = [s.text for s in col1]
# newDf[newDf.columns[1]] = [s.text for s in col2]
# newDf[newDf.columns[2]] = [s.text for s in col3]
# newDf['Year'] = col4
# newDf['Content.Area'] = col5
#
# df = pd.concat([df, newDf], ignore_index=True)

########################################################################################################################
