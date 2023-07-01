from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from userLogin import User
def order(driver):
    User()
    driver.find_element(By.ID,"bhagwaan_uu").click()
    # Order page
    a = driver.find_elements("form-control")
    select = Select(a[0])
    select.select_by_visible_text('TATA Steel')
    # b = driver.find_elements_by_class_name('prd_name')
    select = Select(a[1])
    select.select_by_visible_text('LED BULB')
    select = Select(a[2])
    select.select_by_visible_text('GLIZZ')
    select = Select(a[3])
    select.select_by_visible_text('15W')
    select = Select(a[4])
    select.select_by_visible_text('ROUND')
    select = Select(a[5])
    select.select_by_visible_text('Natural White')
    cust_fun.find_element_by_class_name(driver,[{'field': 'discount', 'value': '50'}])
    cust_fun.find_element_by_class_name(driver,[{'field': 'quantity', 'value': '100'}])
    # driver. find_element_by_class_name("btn btn-primary")
    #  Not workind in order button
    # Error
    driver.quit()
driver=User()
order(driver)
