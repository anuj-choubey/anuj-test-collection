# import driver as driver
from selenium import webdriver
from os.path import exists  ## imported the  exist method
import time

from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
# my custom import
from helpersUsers import cust_fun
# Enter incorrect password
try:
    driver = webdriver.Chrome()
    driver.get("http://localhost/centour/")
    driver.implicitly_wait(5)
    cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value': "test100"}, {'field': 'password', 'value': "test@321"}], 'login')
    driver.back()
    file_exists = exists("./error_log.txt")
    ## check in file exist
    if file_exists :
        f = open("error_log.txt", "a")
        f.write("loging failed\n")
        f.close()
    else :
        f = open("error_log.txt", "x")
        f.write("loging failed\n")
        f.close()
except:
    file_exists = exists("./error_log.txt")
    ## check in file exist
    if file_exists :
        f = open("error_log.txt", "a")
        f.write("loging failed\n")
        f.close()
    else :
        f = open("error_log.txt", "x")
        f.write("loging failed\n")
        f.close()
driver .get("http://localhost/centour/")

# Enter correct password
try:
    driver = webdriver.Chrome()
    driver.get("http://localhost/centour/")
    driver.implicitly_wait(5)
    cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value': "test100"}, {'field': 'password', 'value': "test@321"}], 'login')
    driver.back()
    file_exists = exists("./error_log.txt")
    ## check in file exist
    if file_exists :
        f = open("error_log.txt", "a")
        f.write("loging  succesfully\n")
        f.close()
    else :
        f = open("error_log.txt", "x")
        f.write("loging succesfuly\n")
        f.close()
except:
    file_exists = exists("./error_log.txt")
    ## check in file exist
    if file_exists :
        f = open("error_log.txt", "a")
        f.write("loging failed\n")
        f.close()
    else :
        f = open("error_log.txt", "x")
        f.write("loging failed\n")
        f.close()
        cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value': "mis1011"}, {'field': 'password', 'value': "test@321"}], 'login')

        # Click on log out button
        driver.find_element(By.CLASS_NAME,('fa-user')).click()

        # Enter incorrect id
        cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value': "mis101"}, {'field': 'password', 'value': "Q!W@e3r4t"}], 'login')

        # Enter correct id
        cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value': "mis1011"}, {'field': 'password', 'value': "Q!W@e3r4t5"}], 'login')

        # Meassage are showing on screen "in correct id and password "

        driver.quit()