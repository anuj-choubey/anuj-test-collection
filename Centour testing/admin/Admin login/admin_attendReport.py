import selenium
from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from login import pass_word

def ATtendRE(driver):
    pass_word()

    driver.find_element(By.LINK_TEXT,"Report").click()
    driver.find_element(By.LINK_TEXT,"Attendance Report").click()

    # cust_fun.find_element_by_name(driver, [{'field': 'min', 'value':"02/15/2023"}])
    # cust_fun.find_element_by_name(driver, [{'field': 'max', 'value':"02/15/2023"}])


    #  search  var properly working
    cust_fun.find_element_by_class_name(driver, [{'field': 'form-control-sm', 'value': "	centura001"}])
driver=pass_word()
ATtendRE(driver)