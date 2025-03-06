from selenium.webdriver.common.by   import By
from pages.BasePage import BasePage

"""
Class contains the login page locators and
getting all the elements of those locators
"""
class LoginPage (BasePage):

    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    dashboard_page = (By.CLASS_NAME, "app_logo")

    # calling the constructor
    def __init__(self, driver):
        super().__init__(driver)

    # interacting with the username element
    def enter_username (self, username):
        self.entering_text_element(self.username_input, username)
    
    # interacting with password element
    def enter_password(self, password):
        self.entering_text_element(self.password_input, password)

    # now clicking on the login button
    def click_on_login_btn(self):
        self.click_on_element(self.login_button)

    # assert the is dashboard displayed
    def is_dashboard_displayed(self):
        return self.get_an_element(self.dashboard_page) is not None