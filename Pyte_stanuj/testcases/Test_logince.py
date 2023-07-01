import pytest
import time
@pytest.mark.usefixtures("setup")
class Testlogin :
    def test_001(self):
        import time
        from helpersUsers import cust_fun
        self.driver.implicitly_wait(30)
        cust_fun.find_element_by_name(self.driver, [{'field': 'empid', 'value': "mis1011"}], "login")
        cust_fun.find_element_by_name(self.driver, [{'field': 'password', 'value': "Q!W@e3r4t5"}], 'login')
        if "utkarsh" in self.driver.find_element_by_class_name("custom-control-label").text:
            assert True
        else:
            assert False
    print("login successfully")
    def test_002(self):
        from helpersUsers import cust_fun
        self.driver.implicitly_wait(30)
        cust_fun.find_element_by_name(self.driver, [{'field': 'empid', 'value': "mis1011"}], "login")
        cust_fun.find_element_by_name(self.driver, [{'field': 'password', 'value': "0"}], 'login')
        if "In Correct Id or Password" in self.driver.find_element_by_class_name(" alert-warning").text:
            assert True
        else:
            assert False

    def test_003(self):
        from helpersUsers import cust_fun
        self.driver.implicitly_wait(30)
        cust_fun.find_element_by_name(self.driver, [{'field': 'empid', 'value': "0"}], "login")
        cust_fun.find_element_by_name(self.driver, [{'field': 'password', 'value': "Q!W@e3r4t5"}], 'login')
        if "In Correct Id or Password" in self.driver.find_element_by_class_name("alert-dismissible").text:
            assert True
        else:
            assert False

    def test_004(self):
        from helpersUsers import cust_fun
        self.driver.implicitly_wait(30)
        cust_fun.find_element_by_name(self.driver, [{'field': 'empid', 'value': "mis1011"}], "login")
        cust_fun.find_element_by_name(self.driver, [{'field': 'password', 'value': "Q!W@e3r4t5"}], 'login')
        if "Dumy text to display the information" in self.driver.find_element_by_class_name("text-danger ").text:
            assert True
        else:
            assert False

