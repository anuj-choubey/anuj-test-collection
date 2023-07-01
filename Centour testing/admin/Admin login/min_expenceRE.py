import selenium
from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from login import pass_word

def EXpencere(driver):
    pass_word()

    driver.find_element(By.LINK_TEXT,"Report").click()
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT,"Expense Report").click()

    cust_fun.find_element_by_name(driver, [{'field': 'min', 'value': "04/10/2013"}])
    cust_fun.find_element_by_name(driver, [{'field': 'max', 'value': "02/11/2023"}])

    cust_fun. find_elements_by_class(driver, "exp_approve", 6)
    cust_fun. find_elements_by_class(driver, "fa-download ", 6)

driver=pass_word()
EXpencere(driver)
