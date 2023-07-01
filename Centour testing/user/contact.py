from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from userLogin import User
def Contact(driver):
    User()
    driver.find_element(By.LINK_TEXT,"Contact US").click()
driver=User()
Contact(driver)

