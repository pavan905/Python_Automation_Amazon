"""
This file contains the locator and search action on the locator
using the parametrized data(argument) passing to search bar
"""
import  os


path = os.getcwd().replace("\\","/").replace("pages","testdata/exceldata.xlsx")

class ParametrizedSearch:
    def __init__(self,driver):
        self.driver = driver
        self.search_bar_id = "twotabsearchtextbox"
        self.search_button_xpath = "//*[@value='Go']"
                
    

#To search desired products from the global search bar of the Amazon web application
    def search_product_parametrized(self,product):
        self.driver.find_element_by_id(self.search_bar_id).clear() #To clear the previously entered search text/product name
        self.driver.find_element_by_id(self.search_bar_id).send_keys(product)
        self.driver.find_element_by_xpath(self.search_button_xpath).click()










