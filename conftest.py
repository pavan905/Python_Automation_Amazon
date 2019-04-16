from selenium import webdriver
import testdata.testinputs as td
from pages.Login_Logout import LoginLogout
import pytest
import os
path = os.getcwd().replace("\\","/").replace("Amazon_Python_Automation","Amazon_Python_Automation/driver/chromedriver_v73.exe")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    driver = webdriver.Chrome(executable_path=path)

    driver.get(td.AMAZON_URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver

    lg = LoginLogout(driver)
    lg.click_login()
    lg.enter_login_credentials()
    yield
    driver.quit()

