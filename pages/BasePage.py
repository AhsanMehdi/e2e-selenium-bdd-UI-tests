from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
The purpose of class to define some generic functions mostly utilized
like clicking element
entering text
getting element
getting element text
"""
class BasePage:

    # driver initialization
    def __init__ (self, driver):
        self.driver = driver
        self.time_to_wait = 30

    # click on element
    def click_on_element (self, element_locator):
        WebDriverWait (self.driver, self.time_to_wait).until(EC.visibility_of_element_located(element_locator)).click()
    # enter the text in web element
    def entering_text_element(self, element_locator, text_to_enter):
        WebDriverWait (self.driver, self.time_to_wait).until(EC.visibility_of_element_located(element_locator)).send_keys(text_to_enter)
    # get the text of the web element
    def get_the_element_text (self, element_locator):
        return   WebDriverWait (self.driver, self.time_to_wait).until(EC.visibility_of_element_located(element_locator)).text
    # getting a web element
    def get_an_element (self, element_locator):
        return  WebDriverWait (self.driver, self.time_to_wait).until(EC.visibility_of_element_located(element_locator))