
import selenium
import time
from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from login import pass_word
def check(driver):
    pass_word()
    driver.find_element(By.XPATH,"//a[contains(text(),'Check In')]").click()
    time.sleep(3)
    cust_fun.find_element_by_name(driver,[{'field':'clientname','value':'utkarsh'}])
    time.sleep(3)
    cust_fun.find_element_by_name(driver,[{'field':'premise_image','value':'C:/Users/Admin/Pictures/Screenshots/anuj.png.jpg'}])
    time.sleep(3)
    cust_fun.find_element_by_name(driver,[{'field':'discussion','value':'my name utkarsh dixit i am from vidisha'}])
    driver.find_element(By.ID,"Check_In").click()
driver=pass_word()
check(driver)






