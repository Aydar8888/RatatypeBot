from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import random



driver = webdriver.Chrome("C:\ChromeDriver\chromedriver_win32\chromedriver")
driver.get("https://www.ratatype.ru/typing-test/test/")

element = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/button")
element.click() 

elem = driver.find_element_by_id("startButton")
elem.click()

in_elem = driver.find_element_by_class_name("mainTxt")
actions = ActionChains(driver)

def press_key(key):
    actions.send_keys(key)
    actions.perform()
    time.sleep(random.uniform(0.02, 0.06))
    
for i in in_elem.text:
    press_key(i)
