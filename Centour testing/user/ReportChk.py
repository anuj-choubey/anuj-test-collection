from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from userLogin import User
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def checkre(driver):
    User()
    driver.find_element(By.CLASS_NAME,"dropdown-toggle").click()
    # drp_item = driver.find_elements_by_class_name("dropdown-item")
    # drp_item[1].click()
    cust_fun.find_elements_by_class(driver, 'dropdown-item', 0)
    driver.find_element(By.CLASS_NAME,"dropdown-toggle").click()
    driver.find_element(By.PARTIAL_LINK_TEXT,"Click here").click()
    cust_fun.find_element_by_name(driver, [{"field": "expense_amount", "value": "22222"}])
    # driver.find_element_by_name("discussion").clear()
    cust_fun.find_element_by_name(driver, [{"field": "discussion", "value": "Aman gupta "}])
    driver.find_element(By.CLASS_NAME,"btn-primary").click()
    driver.quit()
driver=User()
checkre(driver)

