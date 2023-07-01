import time
from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from login import pass_word
def Logout(driver):
    pass_word()
    driver.find_element(By.LINK_TEXT," Logout").click()
driver=pass_word()
Logout(driver)