from behave import *



# T7 = paşii pentru scenariul 7, de testare negativă, în care verificăm
# faptul că dă mesaj de eroare la căutarea unor produse inexistente în portofoliul magazinului online

@given("I am on the Licentepc homepage and I want to search for an invalid product")
def step_impl(context):
    context.home_page.open_home_page()

@when('I enter the "{invalid_product}" name in the search box')
def step_impl(context, invalid_product):
    context.catalog_search_page.insert_invalid_product(invalid_product)

@when("I click on the search button")
def step_impl(context):
    context.catalog_search_page.click_search_button()

@then('I am redirected to a new page with the following message displayed : "{no_results}"')
def step_impl(context, no_results):
    context.catalog_search_page.no_results_msg(no_results)


# La căutarea negativă (testul negativ) am luat în considerare doar mesajul
# de eroare secundar (--Incearca o noua cautare--).
#
# Mesajul de eroare principal apare fragmentat în codul HTML, adică este rezultatul unei
# construcţii a mai multor elemente de tip string. Nu ştiu cum să tratez această situaţie...
#
# (--Cautarea ta dupa surubelnita nu a intors niciun rezultat.--)
#    Cautarea ta dupa + surubelnita + nu a intors niciun rezultat.
#
# (--Cautarea ta dupa pepene galben nu a intors niciun rezultat.--)
#    Cautarea ta dupa + pepene galben + nu a intors niciun rezultat.




# T8 = paşii pentru scenariul 8, de testare pozitivă, faptul că se face corect căutarea
@given("I am on the Licentepc homepage and I want to search for a valid product")
def step_impl(context):
    context.home_page.open_home_page()

@when('I enter the "{product_name}" in the search box')
def step_impl(context, product_name):
    context.catalog_search_page.insert_valid_product(product_name)

@when("I click the search button")
def step_impl(context):
    context.catalog_search_page.click_search_button()

@then('I am redirected to a new page that contains the "{results_title}"')
def step_impl(context, results_title):
    context.catalog_search_page.check_listed_products_page_label(results_title)




# T9 = paşii pentru scenariul 9, de testare pozitivă, în care verificăm
# faptul că se poate sorta o listă de produse, după preţ, în ordine crescătoare
@given('I am on "PDF" search result page')
def step_impl(context):
    context.catalog_search_page.open_search_result_page()

@when("I click on sorting options checklist box")
def step_impl(context):
    context.catalog_search_page.click_sort_checklist_box()

@when("I click on Ascending Price option")
def step_impl(context):
    context.catalog_search_page.select_ascending_price_option()

@then("The list is shown sorted in ascending order by price")
def step_impl(context):
    context.catalog_search_page.check_ascending_order_url()




# T10 = paşii pentru scenariul 10, de testare pozitivă, în care verificăm
# faptul că putem adăuga 3 produse la categoria "Favorite"
@given('I am on "PDF" search result page')
def step_impl(context):
    context.catalog_search_page.open_search_result_page()

@when('I click on Favorite link of the "<product_name>"')
def step_impl(context):
    context.catalog_search_page.click_add_to_favorites_link()

@then('A "<confirmation_message>" is shown')
def step_impl(context, confirmation_message):
    context.catalog_search_page.check_confirmation_message_favorite(confirmation_message)

