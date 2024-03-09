from behave import *
from time import sleep


@when("I click on Update account link")
def step_impl(context):
    # context.edit_account_page.click_update_account_link()
    context.edit_account_page.open_edit_account_page()

@when("I delete the current address")
def step_impl(context):
    context.edit_account_page.delete_current_address()

@when("I enter my new address")
def step_impl(context):
    context.edit_account_page.enter_new_address()

@when("I click on the Update button")
def step_impl(context):
    context.edit_account_page.click_update_button()

@then("I am redirected to my account home page")
def step_impl(context):
    context.edit_account_page.my_account_page()

