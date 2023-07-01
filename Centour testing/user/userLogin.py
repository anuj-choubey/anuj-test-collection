import time
from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By

def User():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    time.sleep(5)
    driver.get("http://localhost/centour/")
    cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value': "test100"}, {'field': 'password', 'value': "test@321"}])
    driver.find_element(By.NAME,"login").click()
    return driver
User()