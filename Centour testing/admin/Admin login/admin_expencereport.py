import time

from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from login import pass_word
def Expanse(driver):
    pass_word()
    driver.find_element(By.LINK_TEXT,"Report").click()
    driver.find_element(By.LINK_TEXT,"Expense Report").click()
    driver.find_element(By.NAME,"manager").click()
    time.sleep(3)
    driver.quit()
driver=pass_word()
Expanse(driver)