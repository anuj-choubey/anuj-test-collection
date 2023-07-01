from selenium.webdriver.common.by import By
from userLogin import User
def Logout(driver):
    User()
    driver.find_element(By.CLASS_NAME,"fa-user").click()
    driver.quit()
driver=User()
Logout(driver)