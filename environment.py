from selenium import webdriver

def before_all(context):
     # before all scenario must initialize the driver
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

    # before each scenario delete all cookies
def before_scenario(context, scenario):
    context.driver.delete_all_cookies()

    # after each scenario delete all_cookies
def after_scenario (context, scenario):
    context.driver.delete_all_cookies()

    # after all scenarios quit the driver : It will close all the browser
def after_all (context):
    context.driver.quit()