from selenium.webdriver.common.by   import By
from pages.BasePage import BasePage

"""
Class contains the login page locators and
getting all the elements of those locators
"""
class LoginPage (BasePage):

    usename_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    dashboard_page = (By.ID, "")

    # calling the constructor
    def __init__(self, driver):
        super().__init__(driver)

    # interacting with the username element
    def enter_username (self, username):
        self.entering_text_element(self.usename_input, username)
    
    # interacting with password element
    def enter_password(self, password):
        self.entering_text_element(self.password_input, password)

    # now clicking on the login button
    def click_on_element(self, element_locator):
        self.click_on_element