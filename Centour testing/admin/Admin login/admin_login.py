import time

from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
def wright_login():
    driver= webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost/centour/")
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[contains(text(),'Click here')]").click()

    #password Enter
    cust_fun.find_element_by_name(driver,
                                  [{'field': 'email', 'value': "Centaur@gmail.com"}, {'field': 'password', 'value': "Centaur@321"}])
    driver.find_element(By.CLASS_NAME, "btn-block").click()
    time.sleep(5)
    driver.back()
time.sleep(20)
def wrong_login():
    driver= webdriver.Chrome()
    time.sleep(5)
    driver.get("http://localhost/centour/")
    cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "Centaur@gmail.com"},
                                           {'field': 'password', 'value': "centura@321"}])
    driver.find_element(By.CLASS_NAME, "btn-block").click()

