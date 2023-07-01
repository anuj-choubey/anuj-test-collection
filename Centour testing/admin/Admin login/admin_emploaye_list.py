# import selenium
# from selenium import webdriver
# from helpersUsers import cust_fun
# from selenium.webdriver.common.by import By
# from datetime import datetime, timedelta
# from login import pass_word
#
# def Emploaye_list(driver):
#     pass_word()
#
#     driver.find_element(By.LINK_TEXT,"Employee List").click()
#     # date
#
#     # Get today's date
#     presentday = datetime.now()  # or presentday = datetime.today()
#     # Get Yesterday
#     yesterday = presentday - timedelta(1)
#     # tomorrow = presentday + timedelta(1)
#     Yesterday =  yesterday.strftime('%d-%m-%Y')
#     Today = presentday.strftime('%d-%m-%Y')
#     # Tomorrow = tomorrow.strftime('%d-%m-%Y')
#     cust_fun.find_element_by_name(driver, [{'field': 'min', 'value': Yesterday}])
#     cust_fun.find_element_by_name(driver, [{'field': 'max', 'value': Today}])
#
#     # Error date and time dobble print
#
# driver=pass_word()
# Emploaye_list(driver)