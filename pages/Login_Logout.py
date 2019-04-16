"""
This file contains the locators and actions on those locators
to be performed for Login and Logout of Amazon account
"""

from selenium.webdriver import ActionChains
import testdata.testinputs as td #Importing the credential data stored in centralized data file(testinputs.py)

class LoginLogout:

    def __init__(self,driver):
        self.driver = driver
        self.signin_buttonxpath = "//*[text()='Hello, Sign in']"
        self.email_id = "ap_email"
        self.password_id = "ap_password"
        self.login_sign_in_id = "signInSubmit"
        self.sign_out_tab_xpath = "//*[text()='Hello, pythonautomation']"
        self.sign_out_button_xpath = "//*[text()='Sign Out']"


#To Verify user can click Sign In button to sign into the amazon registered account
    def click_login(self):
        self.driver.find_element_by_xpath(self.signin_buttonxpath).click()

#To login by entering username(email)/password and to verify user is logged in to desired accountdesired Amazon account and verify login
    def enter_login_credentials(self):
        self.driver.find_element_by_id(self.email_id).send_keys(td.EMAIL_ID)
        self.driver.find_element_by_id(self.password_id).send_keys(td.PASSWORD)
        self.driver.find_element_by_id(self.login_sign_in_id).click()

#To logout of the account after the required actions are performed
    def logout(self):
        self.signout_tab = self.driver.find_element_by_xpath(self.sign_out_tab_xpath)
        self.mhover = ActionChains(self.driver)
        self.mhover.move_to_element(self.signout_tab).perform()
        self.driver.find_element_by_xpath(self.sign_out_button_xpath).click()

