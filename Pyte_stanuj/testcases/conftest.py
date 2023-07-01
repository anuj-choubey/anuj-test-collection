import pytest
from selenium import webdriver

@pytest.fixture
def setup(request):
    request.cls.driver = webdriver.Chrome(executable_path="chromedriver.exe")
    request.cls.driver.get("http://localhost/centaur/")
    driver.implicitly_wait(30)
    yield
    request.cls.driver.quit()