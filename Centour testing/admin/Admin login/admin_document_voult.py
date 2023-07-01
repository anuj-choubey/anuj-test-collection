import time
from login import pass_word
from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By


def document(driver):
    pass_word()
    # Document vault
    driver.implicitly_wait(10)
    voult = driver.find_element(By.XPATH, "//a[contains(text(),'Document Vault')]")
    voult.click()
    time.sleep(3)
    cust_fun.find_element_by_name(driver, [{'field': 'title', 'value': "Solar light"}])
    time.sleep(7)
    cust_fun.find_element_by_name(driver, [{'field':'document_address', 'value':'C:/Users/Admin/Pictures/Screenshots/anuj.png.jpg'}])
    time.sleep(6)
    driver.find_element(By.NAME,'submit').click()
    driver.find_element(By.XPATH, "//body/div[1]/div[1]/section[1]/div[1]/div[1]/div[3]/div[8]/div[1]/a[1]/i[1]").click()
    time.sleep(3)
driver = pass_word()
document(driver)
