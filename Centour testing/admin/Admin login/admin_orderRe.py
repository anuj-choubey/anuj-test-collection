import selenium
import time
from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from login import pass_word
def order_re(driver):
    pass_word()
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT,"Report").click()
    driver.find_element(By.LINK_TEXT,"Order Report").click()

    # cust_fun.find_element_by_name(driver, [{'field': 'min', 'value': "05/01/2013"}])
    # cust_fun.find_element_by_name(driver, [{'field': 'max', 'value': "01/01/2023"}])

    driver.find_element(By.XPATH,"//body/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]/input[1]").send_keys("LED BULB")

    # cust_fun.find_elements_by_class(driver, "fs-3", 6)
    time.sleep(3)
    # driver.find_element(By.CLASS_NAME,"fa-user").click()
driver = pass_word()
order_re(driver)