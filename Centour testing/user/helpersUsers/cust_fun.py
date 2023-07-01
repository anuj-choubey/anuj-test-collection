from selenium.webdriver.common.by import By

def find_element_by_name(driver, data_list, click_btn=None):
    for data in data_list:
        driver.find_element(By.NAME,(data["field"])).send_keys(data["value"])
    if click_btn:
        driver.find_element_by_name(By.NAME,(click_btn)).click()




def find_element_by_class_name(driver , data_list ):
    for data in data_list:
        driver.find_element(By.CLASS_NAME,(data["field"])).send_keys(data["value"])

def find_element_by_id(driver,data_list,click_btn=None ):
    for data in data_list :
        driver.find_element(By.ID,(data["field"]))


def find_element_by_xpath(driver, data_list):
    for data in data_list:
        driver.find_element(By.XPATH,(data ["field"])).send_key(data["value"])
def find_elements_by_class(driver, name, item_num):
       drp_item = driver.find_elements(By.NAME,(name))
       drp_item[item_num].click()

def Error_log (driver):
    pass