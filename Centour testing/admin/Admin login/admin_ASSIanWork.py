from datetime import datetime

from selenium.webdriver.common.by import By

from helpersUsers import cust_fun
from login import pass_word
from datetime import datetime
today_date = datetime.today().strftime('%Y-%m-%d')

def assianwork(driver):
    pass_word()
    driver.implicitly_wait(10)
    driver.find_element(By.LINK_TEXT,"Assign Work").click()
    cust_fun.find_element_by_name(driver,[{'field':'empname','value':'utkarsh dixit'}])
    driver.find_element(By.NAME,"empid").send_keys("Centaur")
    cust_fun.find_element_by_name(driver,[{'field':'work','value':'programing'}])
    driver.find_element(By.NAME,'level').send_keys('Mid')
    presentday = datetime.now()
    Today = presentday.strftime('%m-%d-%Y')
    driver.find_element(By.NAME,'deadline').send_keys(Today)
    driver.find_element(By.NAME,"submit").click()
driver=pass_word()
assianwork(driver)







