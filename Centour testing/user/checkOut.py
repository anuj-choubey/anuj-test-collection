from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from userLogin import User

def checkout(driver):
    User()
    driver .get("http://localhost/centaur/user/clientp")
    # driver .get("http://localhost/centaur/user/clientp")
    cust_fun.find_element_by_name(driver, [{"field":"expense_detail","value":"Anuj choubey"}])
    cust_fun.find_element_by_name(driver, [{"field":"exp_image","value":"C://Users//Admin//Pictures//Screenshots//Src.png.png"}])
    # click on check out button
    driver.find_element(By.NAME,"submit").click()
    driver.quit()
driver=User()
checkout(driver)

# Do not open maps