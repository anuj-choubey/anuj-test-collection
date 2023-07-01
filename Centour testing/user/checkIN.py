from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By


# enter a check in page
driver .get("http://localhost/centaur/user/clientp")
# click in check in button
driver.find_element(By.CLASS_NAME,"nav-link").click()

cust_fun.find_element_by_name(driver, [{"field": "clientname","value":"anuj"}])
cust_fun.find_element_by_name(driver, [{"field":"premise_image","value":"C://Users//Admin//Pictures//Screenshots//Src.png.png"}])
cust_fun.find_element_by_name(driver, [{"field":"discussion","value":"Anuj choubey samanpur seth"}])
driver.find_element(By.NAME,"submit").click()
# # check out process
# cust_fun.find_element_by_name(driver, [{"field":"expense_detail","value":"Anuj choubey samanpur seth"}])
# cust_fun.find_element_by_name(driver, [{"field":"exp_image","value":"C://Users//Admin//Pictures//Screenshots//Src.png.png"}])
# # click on check out button
# driver.find_element_by_name("submit").click()


driver.quit()