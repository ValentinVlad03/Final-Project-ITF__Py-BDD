from behave import *

# metode pentru testul T4
@given("I am on home page")
def step_impl(context):
    context.cookies_page.open_home_page()

@when("I click on Cookies Policy link")
def step_impl(context):
    context.cookies_page.click_cookies_link()

@when("I check that a specified text is shown")
def step_impl(context):
    context.cookies_page.check_text_on_page()

@then("I return to home page")
def step_impl(context):
    context.cookies_page.click_return_to_home_page()




