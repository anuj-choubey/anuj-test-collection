import selenium
import time
from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from login import pass_word
def addAccess(driver):
    pass_word()
    driver.find_element(By.LINK_TEXT,"Add").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Add Client").click()
    time.sleep(2)
    cust_fun.find_element_by_name(driver,[{'field':"clientname",'value':"MISTPL"}])
    time.sleep(2)
    cust_fun.find_element_by_name(driver,[{'field':'contactperson','value':'Utkarsh'}])
    time.sleep(3)
    cust_fun.find_element_by_name(driver,[{'field':'phone','value':'7879764563'}])
    time.sleep(3)
    cust_fun.find_element_by_name(driver,[{'field':'email','value':'utkarsh@1234.com'}])
    time.sleep(2)
    cust_fun.find_element_by_name(driver, [{'field': 'access_groupt', 'value': "Bhopal"}])
    time.sleep(3)
    cust_fun.find_element_by_name(driver, [{'field': 'address', 'value': "Bhopal"}])
    time.sleep(2)
    driver.find_element(By.NAME,"submit").click()
driver=pass_word()
addAccess(driver)
