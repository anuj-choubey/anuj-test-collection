from selenium import webdriver
from os.path import exists  ## imported the  exist method

# my custom import
from helpersUsers import cust_fun
# Enter incorrect password

import time

from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
time.sleep(5)
try:

    driver = webdriver.Chrome()
    driver.get("http://localhost/centour/")
    # driver.implicitly_wait(5)
    time.sleep(6)
    cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value': "mis1011"}, {'field': 'password', 'value': "Q!W@e3r4t"}], 'login')
    time.sleep(8)
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




driver.get("http://localhost/centour/")

# Enter correct password
try:
    driver = webdriver.Chrome()
    driver.get("http://localhost/centour/")
    # driver.implicitly_wait(5)
    time.sleep(5)
    cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value': "mis1011"}, {'field': 'password', 'value': "Q!W@e3r4t5"}], 'login')
    time.sleep(5)
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
        f.write("loging su\n")
        f.close()