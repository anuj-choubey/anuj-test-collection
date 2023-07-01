from selenium import webdriver
from helpersUsers import cust_fun
import time
from login import pass_word

from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By

def product(driver):
    pass_word()
    driver.find_element(By.LINK_TEXT,("Products")).click()
    driver.find_element(By.CLASS_NAME,("btn-outline-primary")).click()
    # select wattage
    driver.find_element(By.CLASS_NAME,("form-select ")).click()
    cust_fun.find_elements_by_class(driver, 'form-control', 4)
    # select shape
    driver.find_element(By.CLASS_NAME,("form-group ")).click()
    cust_fun.find_elements_by_class(driver, 'form-control', 4)
    # Enter Quantity
    cust_fun.find_element_by_class_name(driver, [{'field': 'amnt', 'value': "400"}])
    # Discounted
    cust_fun.find_element_by_id(driver,[{'field': 'price5', 'value': "66"}])
driver=pass_word()
product(driver)