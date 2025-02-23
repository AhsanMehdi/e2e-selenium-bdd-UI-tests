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