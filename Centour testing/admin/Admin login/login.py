import time
from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By


def pass_word():
    driver= webdriver.Chrome()
    driver.implicitly_wait(10)
    time.sleep(5)
    driver.get("http://localhost/centour/")
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[contains(text(),'Click here')]").click()
    # password Enter
    cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "Centaur@gmail.com"}, {'field': 'password', 'value': "Centaur@321"}])
    driver.find_element(By.CLASS_NAME, "btn-block").click()
    time.sleep(5)
    return driver
# login()