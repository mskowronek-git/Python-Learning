from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

starttime = time.time()
timeout = starttime + 60*5
timebuy = time.time() + 5


cookie_click = driver.find_element(By.XPATH, '//*[@id="cookie"]')

def buy_feature():

    money = int((driver.find_element(By.ID, 'money')).text)
    features = driver.find_elements(By.CSS_SELECTOR, '#store b')
    del features[-1]
    features_list = [int((re.sub(".*" + "- ", '', feature.text)).replace(',','')) for feature in features]
    highest_buy_index = 0
    for price in features_list:
        if money > price:
            highest_buy_index = features_list.index(price)
    features[highest_buy_index].click()




while True:

    cookie_click.click()
    if time.time() > timeout:
        cps = driver.find_element(By.ID, 'cps').text
        print(cps)
        break

    if time.time() > timebuy:
        timebuy = time.time() + 5
        buy_feature()

