'''

Extracts the image URLS from ufostalker site and writes them to a file
'''


import time
import http

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

imageFile = 'imageurls_4.txt'

def get_elements(pageNo):
    elements = driver.find_elements_by_css_selector('td.ng-scope')
    i = 1
    for anchorTag in elements:
        href = anchorTag.find_elements_by_css_selector('a')
        with open(imageFile, 'a+') as f:
            f.write(str(href[0].get_attribute("href")) + '\n')

chromedriver = "./chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver)
driver.wait = WebDriverWait(driver, 60)

cur, end = 72249, 81000

retries = 0
while cur <= end:
    print("Current Page" + str(cur))
    try:
        url = 'http://www.ufostalker.com/event/'
        eventOccurence = url + str(cur)
        driver.get(eventOccurence)
        time.sleep(1)
        get_elements(cur)
        cur += 1
    # add more exceptions if you run into them
    except (http.client.RemoteDisconnected, IndexError, ConnectionResetError):
        print('Error!')
        retries += 1
        if retries >= 3:
            cur, retries = cur + 1, 0

driver.close()
