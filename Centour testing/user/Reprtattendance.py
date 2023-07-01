from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from userLogin import User

def attendance(driver):
    User()
    driver.find_element(By.CLASS_NAME,"dropdown-toggle").click()
    cust_fun.find_elements_by_class(driver, 'dropdown-item', 1)
    driver.quit()
driver=User()
attendance(driver)