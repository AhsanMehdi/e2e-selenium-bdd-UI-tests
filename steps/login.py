from behave import given, when, then
from pages.LoginPage import LoginPage

@given("user is on login page")
def step_user_on_login_page(context):
    context.login_page = LoginPage(context.driver)  # Initialize LoginPage
    context.driver.get("https://www.saucedemo.com/")  # URL of the login page

@when("user enters the valid username")
def step_user_enters_username(context):
    context.login_page.enter_username("standard_user")  # Replace with dynamic username if needed

@when("user enters the valid password")
def step_user_enters_password(context):
    context.login_page.enter_password("secret_sauce")  # Replace with dynamic password if needed

@when("user clicks on login button")
def step_user_clicks_login_button(context):
    context.login_page.click_on_login_btn()

@then("user should be landed on dashboard page")
def step_user_lands_on_dashboard(context):
    assert context.login_page.is_dashboard_displayed(), "User is not on dashboard page"
