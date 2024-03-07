from behave import *

@given("I am on the Licentepc website homepage")
def step_impl(context):
    context.home_page.open_home_page()

@when("I click on accept cookies button")
def step_impl(context):
    context.home_page.click_accept_cookies_button()

@when("I click on user icon")
def step_impl(context):
    context.home_page.click_autentificare_link()

@when("I enter my valid email")
def step_impl(context):
    context.home_page.insert_email()

@when("I enter my valid password")
def step_impl(context):
    context.home_page.insert_password()

@when("I click on the sign in account button")
def step_impl(context):
    context.home_page.click_login_button()
####

@then("I am redirected to my account page")
def step_impl(context):
    context.home_page.my_account_page()

@when('I insert my invalid "{user_password}"')
def step_impl(context, user_password):
    context.home_page.insert_invalid_password(user_password)

@then('I receive an "{error_message}"')
def step_impl(context, error_message):
    context.home_page.login_failed(error_message)

