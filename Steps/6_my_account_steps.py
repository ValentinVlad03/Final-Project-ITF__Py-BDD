from behave import *


@given("I am on my account page")
def step_impl(context):
    context.my_account_page.open_account_page()

@when("I click sign out link")
def step_impl(context):
    context.my_account_page.click_on_sign_out_link()

@then("I am redirected to home page")
def step_impl(context):
    context.my_account_page.check_redirect_to_home_page()
