import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
URL = "https://data.census.gov/cedsci/table"

for index in range(10):
    # initiate connection
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
    listYears = driver.find_elements(by=By.XPATH,
                                    value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/ul[1]/li/div[1]/div[2]/div[1]")
    yr = []
    for y in listYears:
        yr.append(y.text)

    print(yr)

    yearList[index].click()
    time.sleep(3)

    close = driver.find_element(by=By.XPATH,
                                value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
    close.click()
    time.sleep(3)

########################################################################################################################

    county_headers = [None] * 10
    current_county = driver.find_element(by=By.XPATH,
                                         value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]")
    county_headers[0] = current_county.text
    scroll_horizontal = driver.find_element(by=By.XPATH,
                                            value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[5]/div[2]")
    horizontal_bar_width = scroll_horizontal.rect["width"]
    for i in range(9):
        driver.execute_script("arguments[0].scrollLeft += 750", scroll_horizontal)
        next_county = driver.find_element(by=By.XPATH,
                                          value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/span[1]")
        county_headers[i+1] = next_county.text
        time.sleep(5)
    counties = county_headers
    county_headers.insert(0,"Labels")

    main_data = pd.DataFrame(columns=county_headers)
    print(main_data)
    # SCROLL BACK
    driver.execute_script("arguments[0].scrollLeft -= 8000", scroll_horizontal)
    time.sleep(5)

########################################################################################################################
    header_column = driver.find_elements(by=By.XPATH,
                                         value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div")
    headers = pd.DataFrame()
    headers["Labels"] = [h.text for h in header_column]
    #print(headers)
    element_size = driver.find_element(by=By.XPATH,
                                       value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]")
    size = element_size.size
    height = size['height']
    width = size['width']
    scroll_height = (len(header_column) + 10) * height
    scroll_vertical = driver.find_element(by=By.XPATH,
                                          value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]")

    # SCROLL 1
    driver.execute_script("arguments[0].scrollBy(0,arguments[1])", scroll_vertical, scroll_height)
    time.sleep(5)
    header_column = driver.find_elements(by=By.XPATH,
                                         value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div")
    new_headers = pd.DataFrame()
    new_headers["Labels"] = [h.text for h in header_column]
    #print(new_headers)
    first_scroll = scroll_height
    second_scroll = (len(new_headers)) * height
    # SCROLL 2
    driver.execute_script("arguments[0].scrollBy(arguments[1],arguments[2])", scroll_vertical, first_scroll, second_scroll)
    time.sleep(5)
    header_column = driver.find_elements(by=By.XPATH,
                                         value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div")
    third_headers = pd.DataFrame()
    third_headers["Labels"] = [h.text for h in header_column]
    #print(third_headers)
    first_scroll = second_scroll
    second_scroll = len(third_headers) + scroll_height
    # SCROLL 3
    # driver.execute_script("arguments[0].scrollBy(arguments[1], arguments[2])", scroll_vertical, first_scroll, second_scroll)
    # time.sleep(5)
    # header_column = driver.find_elements(by=By.XPATH,
    #                                      value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div")
    # last_headers = pd.DataFrame()
    # last_headers["Labels"] = [h.text for h in header_column]
    # print(last_headers)
    # last_headers.drop(labels=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
    #                   axis=0,
    #                   inplace=True)
    header_frames = [headers, new_headers, third_headers]
    full_headers = pd.concat(header_frames, ignore_index=True)

    add_col = full_headers["Labels"]
    main_data["Labels"] = add_col
    print(main_data)

    # SCROLL TOP
    driver.execute_script("arguments[0].scrollTo(0,-200)", scroll_vertical)
    time.sleep(5)
    ####################################################################################################################

    # SCROLL BACK
    driver.execute_script("arguments[0].scrollLeft -= 8000", scroll_horizontal)
    time.sleep(5)

    count = 1
    #1
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='2']")
    inner_data.pop(0)
    inner_data.pop(0)
    estimate_one = pd.DataFrame()
    estimate_one["County"] = [e.text for e in inner_data]
    scroll_vertical = driver.find_element(by=By.XPATH,
                                          value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]")
    element_size = driver.find_element(by=By.XPATH,
                                       value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]")
    size = element_size.size
    height = size['height']
    scroll_height = (len(estimate_one) + 10) * height
    ###
    driver.execute_script("arguments[0].scrollBy(0,arguments[1])", scroll_vertical, scroll_height)
    time.sleep(5)
    # inner_data = driver.find_elements(by=By.XPATH,
    #                                      value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]")
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='2']")
    estimate_two = pd.DataFrame()
    estimate_two["County"] = [e.text for e in inner_data]
    first_scroll = scroll_height
    second_scroll = (len(estimate_two)) * height
    ###
    driver.execute_script("arguments[0].scrollBy(arguments[1],arguments[2])", scroll_vertical, first_scroll,
                          second_scroll)
    time.sleep(5)
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='2']")
    estimate_three = pd.DataFrame()
    estimate_three["County"] = [e.text for e in inner_data]
    first_scroll = second_scroll
    second_scroll = len(estimate_three) + scroll_height
    ###
    # driver.execute_script("arguments[0].scrollBy(arguments[1], arguments[2])", scroll_vertical, first_scroll,
    #                       second_scroll)
    # time.sleep(5)
    # inner_data = driver.find_elements(by=By.XPATH,
    #                                   value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]")
    # estimate_four = pd.DataFrame()
    # estimate_four["County"] = [e.text for e in inner_data]
    # estimate_four.drop(labels=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
    #                    axis=0,
    #                    inplace=True)
    estimate_frames = [estimate_one, estimate_two, estimate_three]
    full_estimate = pd.concat(estimate_frames, ignore_index=True)
    add_col = full_estimate["County"]
    main_data[counties[count]] = add_col
    # print(main_data[counties[count]])
    # print(main_data)
    # SCROLL TOP
    driver.execute_script("arguments[0].scrollTo(0,-200)", scroll_vertical)
    time.sleep(5)
    driver.execute_script("arguments[0].scrollLeft += 750", scroll_horizontal)
    time.sleep(5)
    count += 1
    print("1")
    #2
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='6']")
    inner_data.pop(0)
    inner_data.pop(0)
    estimate_one = pd.DataFrame()
    estimate_one["County"] = [e.text for e in inner_data]
    scroll_vertical = driver.find_element(by=By.XPATH,
                                          value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]")
    element_size = driver.find_element(by=By.XPATH,
                                       value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]")
    size = element_size.size
    height = size['height']
    scroll_height = (len(estimate_one) + 10) * height
    ###
    driver.execute_script("arguments[0].scrollBy(0,arguments[1])", scroll_vertical, scroll_height)
    time.sleep(5)
    # inner_data = driver.find_elements(by=By.XPATH,
    #                                      value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]")
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='6']")
    estimate_two = pd.DataFrame()
    estimate_two["County"] = [e.text for e in inner_data]
    first_scroll = scroll_height
    second_scroll = (len(estimate_two)) * height
    ###
    driver.execute_script("arguments[0].scrollBy(arguments[1],arguments[2])", scroll_vertical, first_scroll,
                          second_scroll)
    time.sleep(5)
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='6']")
    estimate_three = pd.DataFrame()
    estimate_three["County"] = [e.text for e in inner_data]
    first_scroll = second_scroll
    second_scroll = len(estimate_three) + scroll_height
    ###
    # driver.execute_script("arguments[0].scrollBy(arguments[1], arguments[2])", scroll_vertical, first_scroll,
    #                       second_scroll)
    # time.sleep(5)
    # inner_data = driver.find_elements(by=By.XPATH,
    #                                   value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]")
    # estimate_four = pd.DataFrame()
    # estimate_four["County"] = [e.text for e in inner_data]
    # estimate_four.drop(labels=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
    #                    axis=0,
    #                    inplace=True)
    estimate_frames = [estimate_one, estimate_two, estimate_three]
    full_estimate = pd.concat(estimate_frames, ignore_index=True)
    add_col = full_estimate["County"]
    main_data[str(counties[count])] = add_col
    # print(main_data[counties[count]])
    # print(main_data)
    # SCROLL TOP
    driver.execute_script("arguments[0].scrollTo(0,-200)", scroll_vertical)
    time.sleep(5)
    driver.execute_script("arguments[0].scrollLeft += 750", scroll_horizontal)
    time.sleep(5)
    count += 1
    print("2")
    #3
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='10']")
    inner_data.pop(0)
    inner_data.pop(0)
    estimate_one = pd.DataFrame()
    estimate_one["County"] = [e.text for e in inner_data]
    scroll_vertical = driver.find_element(by=By.XPATH,
                                          value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]")
    element_size = driver.find_element(by=By.XPATH,
                                       value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]")
    size = element_size.size
    height = size['height']
    scroll_height = (len(estimate_one) + 10) * height
    ###
    driver.execute_script("arguments[0].scrollBy(0,arguments[1])", scroll_vertical, scroll_height)
    time.sleep(5)
    # inner_data = driver.find_elements(by=By.XPATH,
    #                                      value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]")
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='10']")
    estimate_two = pd.DataFrame()
    estimate_two["County"] = [e.text for e in inner_data]
    first_scroll = scroll_height
    second_scroll = (len(estimate_two)) * height
    ###
    driver.execute_script("arguments[0].scrollBy(arguments[1],arguments[2])", scroll_vertical, first_scroll,
                          second_scroll)
    time.sleep(5)
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='10']")
    estimate_three = pd.DataFrame()
    estimate_three["County"] = [e.text for e in inner_data]
    first_scroll = second_scroll
    second_scroll = len(estimate_three) + scroll_height
    estimate_frames = [estimate_one, estimate_two, estimate_three]
    full_estimate = pd.concat(estimate_frames, ignore_index=True)
    add_col = full_estimate["County"]
    main_data[counties[count]] = add_col
    # print(main_data[counties[count]])
    # print(main_data)
    # SCROLL TOP
    driver.execute_script("arguments[0].scrollTo(0,-200)", scroll_vertical)
    time.sleep(5)
    driver.execute_script("arguments[0].scrollLeft += 750", scroll_horizontal)
    time.sleep(5)
    count += 1
    print(count)
    #4
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='14']")
    inner_data.pop(0)
    inner_data.pop(0)
    estimate_one = pd.DataFrame()
    estimate_one["County"] = [e.text for e in inner_data]
    scroll_vertical = driver.find_element(by=By.XPATH,
                                          value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]")
    element_size = driver.find_element(by=By.XPATH,
                                       value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]")
    size = element_size.size
    height = size['height']
    scroll_height = (len(estimate_one) + 10) * height
    ###
    driver.execute_script("arguments[0].scrollBy(0,arguments[1])", scroll_vertical, scroll_height)
    time.sleep(5)
    # inner_data = driver.find_elements(by=By.XPATH,
    #                                      value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]")
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='14']")
    estimate_two = pd.DataFrame()
    estimate_two["County"] = [e.text for e in inner_data]
    first_scroll = scroll_height
    second_scroll = (len(estimate_two)) * height
    ###
    driver.execute_script("arguments[0].scrollBy(arguments[1],arguments[2])", scroll_vertical, first_scroll,
                          second_scroll)
    time.sleep(5)
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='14']")
    estimate_three = pd.DataFrame()
    estimate_three["County"] = [e.text for e in inner_data]
    first_scroll = second_scroll
    second_scroll = len(estimate_three) + scroll_height
    estimate_frames = [estimate_one, estimate_two, estimate_three]
    full_estimate = pd.concat(estimate_frames, ignore_index=True)
    add_col = full_estimate["County"]
    main_data[counties[count]] = add_col
    # print(main_data[counties[count]])
    # print(main_data)
    # SCROLL TOP
    driver.execute_script("arguments[0].scrollTo(0,-200)", scroll_vertical)
    time.sleep(5)
    driver.execute_script("arguments[0].scrollLeft += 750", scroll_horizontal)
    time.sleep(5)
    count += 1
    print(count)
    #5
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='18']")
    inner_data.pop(0)
    inner_data.pop(0)
    estimate_one = pd.DataFrame()
    estimate_one["County"] = [e.text for e in inner_data]
    scroll_vertical = driver.find_element(by=By.XPATH,
                                          value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]")
    element_size = driver.find_element(by=By.XPATH,
                                       value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]")
    size = element_size.size
    height = size['height']
    scroll_height = (len(estimate_one) + 10) * height
    ###
    driver.execute_script("arguments[0].scrollBy(0,arguments[1])", scroll_vertical, scroll_height)
    time.sleep(5)
    # inner_data = driver.find_elements(by=By.XPATH,
    #                                      value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]")
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='18']")
    estimate_two = pd.DataFrame()
    estimate_two["County"] = [e.text for e in inner_data]
    first_scroll = scroll_height
    second_scroll = (len(estimate_two)) * height
    ###
    driver.execute_script("arguments[0].scrollBy(arguments[1],arguments[2])", scroll_vertical, first_scroll,
                          second_scroll)
    time.sleep(5)
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='18']")
    estimate_three = pd.DataFrame()
    estimate_three["County"] = [e.text for e in inner_data]
    first_scroll = second_scroll
    second_scroll = len(estimate_three) + scroll_height
    estimate_frames = [estimate_one, estimate_two, estimate_three]
    full_estimate = pd.concat(estimate_frames, ignore_index=True)
    add_col = full_estimate["County"]
    main_data[counties[count]] = add_col
    # print(main_data[counties[count]])
    # print(main_data)
    # SCROLL TOP
    driver.execute_script("arguments[0].scrollTo(0,-200)", scroll_vertical)
    time.sleep(5)
    driver.execute_script("arguments[0].scrollLeft += 750", scroll_horizontal)
    time.sleep(5)
    count += 1
    print(count)
    #6
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='22']")
    inner_data.pop(0)
    inner_data.pop(0)
    estimate_one = pd.DataFrame()
    estimate_one["County"] = [e.text for e in inner_data]
    scroll_vertical = driver.find_element(by=By.XPATH,
                                          value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]")
    element_size = driver.find_element(by=By.XPATH,
                                       value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]")
    size = element_size.size
    height = size['height']
    scroll_height = (len(estimate_one) + 10) * height
    ###
    driver.execute_script("arguments[0].scrollBy(0,arguments[1])", scroll_vertical, scroll_height)
    time.sleep(5)
    # inner_data = driver.find_elements(by=By.XPATH,
    #                                      value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]")
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='22']")
    estimate_two = pd.DataFrame()
    estimate_two["County"] = [e.text for e in inner_data]
    first_scroll = scroll_height
    second_scroll = (len(estimate_two)) * height
    ###
    driver.execute_script("arguments[0].scrollBy(arguments[1],arguments[2])", scroll_vertical, first_scroll,
                          second_scroll)
    time.sleep(5)
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='22']")
    estimate_three = pd.DataFrame()
    estimate_three["County"] = [e.text for e in inner_data]
    first_scroll = second_scroll
    second_scroll = len(estimate_three) + scroll_height
    estimate_frames = [estimate_one, estimate_two, estimate_three]
    full_estimate = pd.concat(estimate_frames, ignore_index=True)
    add_col = full_estimate["County"]
    main_data[counties[count]] = add_col
    # print(main_data[counties[count]])
    # print(main_data)
    # SCROLL TOP
    driver.execute_script("arguments[0].scrollTo(0,-200)", scroll_vertical)
    time.sleep(5)
    driver.execute_script("arguments[0].scrollLeft += 750", scroll_horizontal)
    time.sleep(5)
    count += 1
    print(count)
    #7
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='26']")
    inner_data.pop(0)
    inner_data.pop(0)
    estimate_one = pd.DataFrame()
    estimate_one["County"] = [e.text for e in inner_data]
    scroll_vertical = driver.find_element(by=By.XPATH,
                                          value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]")
    element_size = driver.find_element(by=By.XPATH,
                                       value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]")
    size = element_size.size
    height = size['height']
    scroll_height = (len(estimate_one) + 10) * height
    ###
    driver.execute_script("arguments[0].scrollBy(0,arguments[1])", scroll_vertical, scroll_height)
    time.sleep(5)
    # inner_data = driver.find_elements(by=By.XPATH,
    #                                      value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]")
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='26']")
    estimate_two = pd.DataFrame()
    estimate_two["County"] = [e.text for e in inner_data]
    first_scroll = scroll_height
    second_scroll = (len(estimate_two)) * height
    ###
    driver.execute_script("arguments[0].scrollBy(arguments[1],arguments[2])", scroll_vertical, first_scroll,
                          second_scroll)
    time.sleep(5)
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='26']")
    estimate_three = pd.DataFrame()
    estimate_three["County"] = [e.text for e in inner_data]
    first_scroll = second_scroll
    second_scroll = len(estimate_three) + scroll_height
    estimate_frames = [estimate_one, estimate_two, estimate_three]
    full_estimate = pd.concat(estimate_frames, ignore_index=True)
    add_col = full_estimate["County"]
    main_data[counties[count]] = add_col
    # print(main_data[counties[count]])
    # print(main_data)
    # SCROLL TOP
    driver.execute_script("arguments[0].scrollTo(0,-200)", scroll_vertical)
    time.sleep(5)
    driver.execute_script("arguments[0].scrollLeft += 750", scroll_horizontal)
    time.sleep(5)
    count += 1
    print(count)
    #8
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='30']")
    inner_data.pop(0)
    inner_data.pop(0)
    estimate_one = pd.DataFrame()
    estimate_one["County"] = [e.text for e in inner_data]
    scroll_vertical = driver.find_element(by=By.XPATH,
                                          value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]")
    element_size = driver.find_element(by=By.XPATH,
                                       value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]")
    size = element_size.size
    height = size['height']
    scroll_height = (len(estimate_one) + 10) * height
    ###
    driver.execute_script("arguments[0].scrollBy(0,arguments[1])", scroll_vertical, scroll_height)
    time.sleep(5)
    # inner_data = driver.find_elements(by=By.XPATH,
    #                                      value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]")
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='30']")
    estimate_two = pd.DataFrame()
    estimate_two["County"] = [e.text for e in inner_data]
    first_scroll = scroll_height
    second_scroll = (len(estimate_two)) * height
    ###
    driver.execute_script("arguments[0].scrollBy(arguments[1],arguments[2])", scroll_vertical, first_scroll,
                          second_scroll)
    time.sleep(5)
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='30']")
    estimate_three = pd.DataFrame()
    estimate_three["County"] = [e.text for e in inner_data]
    first_scroll = second_scroll
    second_scroll = len(estimate_three) + scroll_height
    estimate_frames = [estimate_one, estimate_two, estimate_three]
    full_estimate = pd.concat(estimate_frames, ignore_index=True)
    add_col = full_estimate["County"]
    main_data[counties[count]] = add_col
    # print(main_data[counties[count]])
    # print(main_data)
    # SCROLL TOP
    driver.execute_script("arguments[0].scrollTo(0,-200)", scroll_vertical)
    time.sleep(5)
    driver.execute_script("arguments[0].scrollLeft += 750", scroll_horizontal)
    time.sleep(5)
    count += 1
    print(count)
    #9
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='34']")
    inner_data.pop(0)
    inner_data.pop(0)
    estimate_one = pd.DataFrame()
    estimate_one["County"] = [e.text for e in inner_data]
    scroll_vertical = driver.find_element(by=By.XPATH,
                                          value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]")
    element_size = driver.find_element(by=By.XPATH,
                                       value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]")
    size = element_size.size
    height = size['height']
    scroll_height = (len(estimate_one) + 10) * height
    ###
    driver.execute_script("arguments[0].scrollBy(0,arguments[1])", scroll_vertical, scroll_height)
    time.sleep(5)
    # inner_data = driver.find_elements(by=By.XPATH,
    #                                      value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]")
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='34']")
    estimate_two = pd.DataFrame()
    estimate_two["County"] = [e.text for e in inner_data]
    first_scroll = scroll_height
    second_scroll = (len(estimate_two)) * height
    ###
    driver.execute_script("arguments[0].scrollBy(arguments[1],arguments[2])", scroll_vertical, first_scroll,
                          second_scroll)
    time.sleep(5)
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='34']")
    estimate_three = pd.DataFrame()
    estimate_three["County"] = [e.text for e in inner_data]
    first_scroll = second_scroll
    second_scroll = len(estimate_three) + scroll_height
    estimate_frames = [estimate_one, estimate_two, estimate_three]
    full_estimate = pd.concat(estimate_frames, ignore_index=True)
    add_col = full_estimate["County"]
    main_data[counties[count]] = add_col
    # print(main_data[counties[count]])
    # print(main_data)
    # SCROLL TOP
    driver.execute_script("arguments[0].scrollTo(0,-200)", scroll_vertical)
    time.sleep(5)
    driver.execute_script("arguments[0].scrollLeft += 750", scroll_horizontal)
    time.sleep(5)
    count += 1
    print(count)
    #10
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='38']")
    inner_data.pop(0)
    inner_data.pop(0)
    estimate_one = pd.DataFrame()
    estimate_one["County"] = [e.text for e in inner_data]
    scroll_vertical = driver.find_element(by=By.XPATH,
                                          value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]")
    element_size = driver.find_element(by=By.XPATH,
                                       value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]")
    size = element_size.size
    height = size['height']
    scroll_height = (len(estimate_one) + 10) * height
    ###
    driver.execute_script("arguments[0].scrollBy(0,arguments[1])", scroll_vertical, scroll_height)
    time.sleep(5)
    # inner_data = driver.find_elements(by=By.XPATH,
    #                                      value="html/body/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]")
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='38']")
    estimate_two = pd.DataFrame()
    estimate_two["County"] = [e.text for e in inner_data]
    first_scroll = scroll_height
    second_scroll = (len(estimate_two)) * height
    ###
    driver.execute_script("arguments[0].scrollBy(arguments[1],arguments[2])", scroll_vertical, first_scroll,
                          second_scroll)
    time.sleep(5)
    inner_data = driver.find_elements_by_css_selector("div[aria-colindex='38']")
    estimate_three = pd.DataFrame()
    estimate_three["County"] = [e.text for e in inner_data]
    first_scroll = second_scroll
    second_scroll = len(estimate_three) + scroll_height
    estimate_frames = [estimate_one, estimate_two, estimate_three]
    full_estimate = pd.concat(estimate_frames, ignore_index=True)
    add_col = full_estimate["County"]
    main_data[counties[count]] = add_col
    # print(main_data[counties[count]])
    # print(main_data)
    # SCROLL TOP
    driver.execute_script("arguments[0].scrollTo(0,-200)", scroll_vertical)
    time.sleep(5)
    count += 1
    print(count)
    year = [yr[index]] * len(main_data)
    print(year)
    main_data["Year"] = year
    main_data.to_csv('census_data_{}.csv'.format(yr[index]))
    # all_data = pd.DataFrame()
    # if(index == 0):
    #     all_data = main_data
    # else:
    #     all_data = pd.concat([all_data, main_data], ignore_index=True, axis=1)
    print("Next:")
    print(index)
time.sleep(5)

# create csv file
#all_data.to_csv('census_data.csv')

# close out of the session
driver.quit()

