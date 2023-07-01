import time

import selenium
from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from login import pass_word
def work(driver):
    pass_word()
    driver.find_element(By.ID,"dropdownSubMenu1").click()
    driver.find_element(By.LINK_TEXT,"Work Report").click()
    # driver.find_element(By.NAME,"attendance_length").click()
    time.sleep(3)
    # driver.find_element(By.XPATH,"//body/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]/input[1]").send_keys('test')
    time.sleep(3)
    driver.back()
driver=pass_word()
work(driver)