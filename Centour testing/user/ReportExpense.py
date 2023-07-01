from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from userLogin import User

def Expanse(driver):
    User()
    driver.find_element(By.CLASS_NAME,"dropdown-toggle").click()
    cust_fun.find_elements_by_class(driver, 'dropdown-item', 3)
    down_load=driver.find_elements(By.LINK_TEXT,"Download")
    down_load[3].click()
    driver.quit()
driver=User()
Expanse(driver)