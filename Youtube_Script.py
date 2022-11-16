
import csv
import io
from grpc import Channel
from selenium import webdriver
from selenium.common import exceptions
import sys
import time
import pandas as pd





def scrape(url):
    title = []
    viwess = []
    date = []
    channel = []

    driver = webdriver.Chrome('')
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    details = driver.find_elements_by_xpath('//*[@id="metadata"]')
    details = [row.text for row in details]
    for row in details:

        try:
 
            title = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-vertical-list-renderer/div[1]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a').text
            viewss = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-vertical-list-renderer/div[1]/ytd-video-renderer[1]/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[1]').text
            date = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-vertical-list-renderer/div[1]/ytd-video-renderer[1]/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[2]').text
            channel = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-vertical-list-renderer/div[1]/ytd-video-renderer[1]/div[1]/div/div[2]/ytd-channel-name/div/div/yt-formatted-string/a').text
            time.sleep(7)
        except exceptions.NoSuchElementException:
            error = "Error: Double check selector OR "
            error += "element may not yet be on the screen at the time of the find operation"
            print(error)
        time.sleep(7)


        last_height = driver.execute_script("return document.documentElement.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")


        print("> VIDEO TITLE: " + title + "\n")
        print("> VIEWS of Video: " + viewss + "\n")
        print("> Date: " + date + "\n")
        print(">Channel Name: " + channel + "\n")

    
        with io.open('File location','w',newline='',encoding="utf-16") as file:
            writer = csv.writer(file,delimiter=",",quoting=csv.QUOTE_ALL)
            writer.writerow(["Title","Views","Date","Channelname"])
            writer.writerow([title,viewss,date,channel])
        

    
        a = pd.read_csv("File location",encoding="utf-16")
        a.to_html("Storing Location")
        driver.close()

scrape("https://www.youtube.com/results?search_query=")
