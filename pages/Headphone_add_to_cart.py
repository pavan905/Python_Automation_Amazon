"""
This file contains the locators and actions on those locators
to be performed searching Headphone, adding and deleting from the cart
"""
from selenium.webdriver import ActionChains



class AddHeadphone:

    def __init__(self,driver):
        self.driver = driver
        self.departments_tab_xpath = "//*[text()='Departments']"
        self.electronics_link_xpath = "//span[text()='Electronics']"
        self.headphones_link_xpath = "//*[@alt='Headphones']"
        self.first_search_result_item_xpath = "//*[@class='s-result-list sg-row']/child::div[1]/child::div/child::div/child::div/child::div[2]/child::div"
        self.add_to_cart_id = "add-to-cart-button"
        self.view_cart_id = "hlb-view-cart"
        self.delete_headphone_xpath = "(//*[@value='Delete'])[2]"

#Function to mouse hover on the departments tab in the Amazon Ecommerce webpage
    def mousehover_on_departments_tab(self):
        self.Departments_tab = self.driver.find_element_by_xpath(self.departments_tab_xpath)
        self.action = ActionChains(self.driver)#action is an abject created to perform mouse hover action on departments tab
        self.action.move_to_element(self.Departments_tab).perform()

#To Click on the Electronics link in the Departments tab
    def click_electronic_link(self):
        self.driver.find_element_by_xpath(self.electronics_link_xpath).click()

#To select HeadPhone section of the Electronics page
    def click_headphones_section(self):
        self.driver.find_element_by_xpath(self.headphones_link_xpath).click()

#To select the first Headphone product from the resuts list page
    def select_first_result_product(self):
        self.driver.find_element_by_xpath(self.first_search_result_item_xpath).click()

#To add the first select headphone product and to verify if user is able to add to the cart
    def click_add_to_cart_button(self):
        self.driver.find_element_by_id(self.add_to_cart_id).click()

#To verify if the added product is displayed in the cart with right quantity and product details
    def click_view_cart_button(self):
        self.driver.find_element_by_id(self.view_cart_id).click()
        self.driver.find_element_by_id("nav-cart").click()

# Execution oriented function
    def naviagte_to_cart(self): #This step is required if executing each scenario in separate browser
        self.driver.find_element_by_id("nav-cart").click()


 # To verify the delete functionality from the cart
    def delete_headphone(self):
        self.driver.find_element_by_xpath(self.delete_headphone_xpath).click()




