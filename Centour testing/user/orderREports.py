from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from userLogin import User

def or_report(driver):
    User()
    driver.find_element(By.ID,"ramlal_uu").click()
    driver.find_element(By.CLASS_NAME,"sorting_1").click()
    driver.find_element(By.CLASS_NAME,"fa-solid ").click()
    driver.quit()
driver=User()
or_report(driver)
