from selenium.webdriver.common.by import By
from userLogin import User
def vault(driver):
    User()
    driver.find_element(By.ID,"syamlal_uu").click()
    # driver.find_element_by_class_name("fs-3").click()
    doc_vout=driver.find_elements(By.CLASS_NAME,"fa-download")
    doc_vout[5].click()
    driver.quit()
driver=User()
vault(driver)
