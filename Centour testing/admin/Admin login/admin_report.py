import selenium
from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from login import pass_word

def report(driver):
    pass_word()

    driver.find_element(By.LINK_TEXT,"Report").click()
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT,"Check-in Report").click()

    cust_fun.find_element_by_tag_name(driver, [{"field": 'select', "value": 'Utkarsh'}])

    # Get today's date
    # presentday = datetime.now()  # or presentday = datetime.today()
    # # Get Yesterday
    # yesterday = presentday - timedelta(1)
    # # tomorrow = presentday + timedelta(1)
    # Yesterday =  yesterday.strftime('%d-%m-%Y')
    # Today = presentday.strftime('%d-%m-%Y')
    #
    # cust_fun.find_element_by_name(driver, [{'field': 'min', 'value': Yesterday}])
    # cust_fun.find_element_by_name(driver, [{'field': 'max', 'value': Today}])

    driver.find_element(By.CLASS_NAME,"buttons-excel").click()
    # cust_fun.find_element_by_link_text(driver,"Click here",2)
    driver.find_element(By.LINK_TEXT,"Click here").click()
driver = pass_word()
report(driver)