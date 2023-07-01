import selenium
from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from login import pass_word


def Add_Client(driver):
    pass_word()
    driver.find_element(By.CLASS_NAME,"dropdown-toggle").click()
    driver.find_element(By.LINK_TEXT,"Add Client").click()
    cust_fun.find_element_by_name(driver, [{'field': 'clientname', 'value': "mistpl"}])
    cust_fun.find_element_by_name(driver, [{'field': 'contactperson', 'value': "Anuj"}])
    cust_fun.find_element_by_name(driver, [{'field': 'phone', 'value': "621660376111"}])
    cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "Ajdjhdj@gmaiik.com"}])
    cust_fun.find_element_by_name(driver, [{'field': 'address', 'value': "Bhopal mp"}])
    cust_fun.find_element_by_name(driver, [{'field': "image_path", 'value': "C://Users//Admin//Pictures//Screenshots//anuj.png.jpg"}])
    cust_fun.find_element_by_name(driver, [{'field': 'access_groupt', 'value': "Indore"}])
    driver.find_element(By.NAME,"submit").click()
driver=pass_word()
Add_Client(driver)