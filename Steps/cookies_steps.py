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



# metode pentru testul T5
@given("I am on Cookies Policy page")
def step_impl(context):
    context.cookies_page.open_cookies_policy_page()

@when("I click on the email address specified")
def step_impl(context):
    context.cookies_page.click_email_address()

@then("I am redirected to an external application (email client)")
def step_impl(context):
    context.cookies_page.check_redirecting_to_email_client_app()





