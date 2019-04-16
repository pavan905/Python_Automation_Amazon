"""
This file is an Test script file having all the scenarios
OR Actions on webelements are called to perform in the required sequences
"""
import pytest
from pages.search_product_parametrized import ParametrizedSearch
from pages.Login_Logout import LoginLogout
from pages.Headphone_add_to_cart import AddHeadphone
from pages.Macbook_search_add import MacbookPro
import time

@pytest.mark.usefixtures("test_setup")
class TestAmazonSearchProducts:

    # def test_login(self):
    #     driver = self.driver
    #     lg = LoginLogout(driver)
    #     lg.click_login()
    #     lg.enter_login_credentials()

    def test_add_headphone(self):
        driver = self.driver
        hdph = AddHeadphone(driver)
        hdph.mousehover_on_departments_tab()
        hdph.click_electronic_link()
        hdph.click_headphones_section()
        hdph.select_first_result_product()
        hdph.click_add_to_cart_button()



    def test_add_macbook(self):
        driver = self.driver
        mcbk = MacbookPro(driver)
        mcbk.search_macbook()
        mcbk.click_search_button()
        mcbk.click_second_result_product()
        mcbk.select_quantity()
        hdph = AddHeadphone(driver)
        hdph.click_add_to_cart_button()
        time.sleep(5) #to handle selenium to browser speed sync
        mcbk.exit_pop_up()
        hdph.click_view_cart_button()

    def test_delete_headphone_from_cart(self):
        driver = self.driver
        hp = AddHeadphone(driver)
        # hp.naviagte_to_cart()# to be enabled only when executing each scenario in independent browser(non sequencially)
        hp.delete_headphone()

    def test_reduce_quantity(self):
        driver = self.driver
        hp = AddHeadphone(driver)
        # hp.naviagte_to_cart() # to be enabled only when executing each scenario in independent browser(non sequencially)
        mk = MacbookPro(driver)
        mk.reduce_quantity()
        mk.proceed_to_checkout()

    def test_parameter_based_search(self):
        driver = self.driver
        ex = ParametrizedSearch(driver)
        ex.search_product_parametrized("Amazon fire stick")
        ex.search_product_parametrized("samasung galaxy s10")
        ex.search_product_parametrized("Toshiba TV")

    def test_logout(self):
        driver = self.driver
        lgn = LoginLogout(driver)
        lgn.logout()












