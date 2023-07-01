# import time
#
# import selenium
# from selenium import webdriver
# from helpersUsers import cust_fun
# from selenium.webdriver.common.by import By
# from login import pass_word
# def EMP_click(driver):
#     pass_word()
#
#     driver.find_element(By.LINK_TEXT,"Employee List").click()
#
#     # driver.find_element_by_link_text("Click").click()
#     cust_fun.find_element_by_link_text(driver, "Click", 5)
#
#     driver.find_element(By.NAME,"name").clear()
#     cust_fun.find_element_by_name(driver, [{'field': 'name', 'value': "Anuj choubey"}])
#
#     driver.find_element(By.NAME,"empid").clear()
#     cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value': "mis1111"}])
#
#     driver.find_element(By.NAME,"phone").clear()
#     cust_fun.find_element_by_name(driver, [{'field': 'phone', 'value': "6363636363"}])
#     time.sleep(3)
#     driver.find_element(By.NAME,"email").clear()
#     cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "anuj@gmail.com"}])
#     time.sleep(2)
#     # location
#     cust_fun.find_element_by_name(driver, [{'field': 'access_group', 'value': "Bhopal"}])
#     time.sleep(2)
#     # role
#     cust_fun.find_element_by_name(driver, [{'field': 'role', 'value': "Executive"}])
#     time.sleep(2)
#     driver.find_element(By.NAME,"password").clear()
#     cust_fun.find_element_by_name(driver, [{'field': 'password', 'value': "Anuj@123"}])
#
#     driver.find_element(By.NAME,"image_path").clear()
#     cust_fun.find_element_by_name(driver, [{'field': 'image_path', 'value': "D://Users//Anuj Choubey//Selenium testing//src.png.png"}])
#
#     # submit button
#     driver.find_element(By.NAME,"submit").click()
# driver=pass_word()
# EMP_click(driver)