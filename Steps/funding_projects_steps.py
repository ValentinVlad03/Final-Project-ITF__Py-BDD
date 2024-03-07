from behave import *


@given("I am on home page")
def step_impl(context):
    context.funding_projects_page.open_home_page()

@when("I click on Funding Projects link")
def step_impl(context):
    context.funding_projects_page.open_funding_projects_page()

@when("I click on an company name link, from the list")
def step_impl(context):
    context.funding_projects_page.click_on_asus_link()

@then("I am redirected to an external website")
def step_impl(context):
    context.funding_projects_page.check_current_url()
