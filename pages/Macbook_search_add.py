"""
This file contains the locators and actions on those locators
to be performed for searching Macbokk product and adding and reducing the quantity from cart
"""
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import testdata.testinputs as td


class MacbookPro:

    def __init__(self,driver):
        self.driver = driver
        self.search_bar_id = "twotabsearchtextbox"
        self.search_button_xpath = "//*[@value='Go']"
        self.select_second_resultsproduct_xpath = "//*[@class='s-result-list sg-row']/child::div[4]/child::div/child::div/child::div/child::div[2]/child::div"
        self.qty_dropdown_id = "quantity"
        self.cart_qty_dropdown_xpath = "//*[@class='a-button a-button-dropdown a-button-small a-button-span8 quantity']" #"//*[@class='a-dropdown-prompt']"
        self.checkout_button_xpath = "//*[@name='proceedToCheckout']"


#To Search the required product and check the availability
    def search_macbook(self):
        self.driver.find_element_by_id(self.search_bar_id).send_keys(td.macbook_pro)


    def click_search_button(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

#To select the required  product from the search results
    def click_second_result_product(self):
        self.driver.find_element_by_xpath(self.select_second_resultsproduct_xpath).click()

#To select the desired quantioty of the product
    def select_quantity(self):
        self.quantity_drdp = self.driver.find_element_by_id(self.qty_dropdown_id)
        self.qty_select = Select(self.quantity_drdp)
        self.qty_select.select_by_value("2")

#To overcome the Add to cart pop up(which is observed only for macbook products)
    def exit_pop_up(self):
        self.act = ActionChains(self.driver)
        self.act.send_keys(Keys.ENTER).perform()


#To reduce the quantity from the cart before check out
    def reduce_quantity(self):
        self.driver.find_element_by_xpath(self.cart_qty_dropdown_xpath).click()
        self.ac = ActionChains(self.driver)
        self.ac.move_to_element(self.driver.find_element_by_xpath(self.cart_qty_dropdown_xpath)).send_keys(Keys.NUMPAD1).perform()
        time.sleep(2)
        self.ac.send_keys(Keys.ENTER).perform()

#Proceeding to the checkout
    def proceed_to_checkout(self):
         self.driver.find_element_by_xpath(self.checkout_button_xpath).click()
         time.sleep(5)
         self.driver.back()




