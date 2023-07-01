import pytest
import time
@pytest.mark.usefixtures("setup")

# def test_001(self):
#     import time
#     from helpersUsers import cust_fun
#     # time.sleep(2)
#     cust_fun.find_element_by_name(self.driver, [{'field': 'empid', 'value': "mis1011"}], "login")
#     cust_fun.find_element_by_name(self.driver, [{'field': 'password', 'value': "Q!W@e3r4t5"}], 'login')
#     if "utkarsh" in self.driver.find_element_by_class_name("custom-control-label").text:
#         assert True
#     else:
#         assert False
# print("login successfully")
def test_005(self):
    from helpersUsers import cust_fun

    self.driver.find_element_by_class_name("nav-link").click()
    cust_fun.find_element_by_name(self.driver, [{"field": "clientname","value":"anuj"}])
    cust_fun.find_element_by_name(self.driver, [{"field":"premise_image","value":"C://Users//Admin//Pictures//Screenshots//Src.png.png"}])
    cust_fun.find_element_by_name(self.driver, [{"field":"discussion","value":"Anuj choubey samanpur seth"}])
    self.driver.find_element_by_name("submit").click()
    if "User denied the request for Geolocation"in self.driver.find_element_by_class_name(" col-sm-12 ").text:
        assert True
    else:
        assert False