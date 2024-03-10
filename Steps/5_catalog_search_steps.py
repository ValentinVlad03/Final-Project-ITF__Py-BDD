from behave import *



# T6 = paşii pentru scenariul 6, de testare negativă, în care verificăm
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

@then('I am redirected to a new page with the following message displayed : "{text_to_search}"')
def step_impl(context, text_to_search):
    context.catalog_search_page.no_result_msg(text_to_search)


# La căutarea negativă (testul negativ) am luat în considerare doar mesajul
# de eroare secundar (--Incearca o noua cautare--).
#
# Mesajul de eroare principal apare fragmentat în codul HTML, adică este rezultatul unei
# construcţii a mai multor elemente de tip string.
#
# (--Cautarea ta dupa surubelnita nu a intors niciun rezultat.--)
#    Cautarea ta dupa + surubelnita + nu a intors niciun rezultat.
#
# (--Cautarea ta dupa pepene galben nu a intors niciun rezultat.--)
#    Cautarea ta dupa + pepene galben + nu a intors niciun rezultat.




# T7 = paşii pentru scenariul 7, de testare pozitivă,
# în care verificăm faptul că se face corect căutarea
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




# T8 = paşii pentru scenariul 8, de testare pozitivă, în care verificăm
# faptul că se poate sorta o listă de produse, după preţ, în ordine crescătoare
@given('I am on PDF search result page')
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




# T9 = paşii pentru scenariul 9, de testare pozitivă, în care verificăm
# faptul că putem adăuga un produs la categoria "Favorite"
@when('I click on Favorite link of Corel PDF')
def step_impl(context):
    context.catalog_search_page.click_add_to_favorites_link()

@then('I go to Favorite section of my account and check that the product is listed')
def step_impl(context):
    context.catalog_search_page.go_to_favorite_section_in_my_account()
    context.catalog_search_page.check_corel_pdf_in_favorite()




# T10 = paşii pentru scenariul 10, de testare pozitivă, în care verificăm
# faptul că putem scoate din listă un produs de la categoria "Favorite"
@when('I click on "Software" link on the upper left side of the webpage')
def step_impl(context):
    context.catalog_search_page.click_software_category_link()

@when('I click on "Corel" link from the left side category list')
def step_impl(context):
    context.catalog_search_page.click_corel_category_link()

@when('I click on "COREL PDF FUSION" link from category list on the left side')
def step_impl(context):
    context.catalog_search_page.click_corel_pdf_fusion_category_link()

@when('I click on product name link')
def step_impl(context):
    context.catalog_search_page.click_on_product_name()

@when('I click on the activated Favorite link')
def step_impl(context):
    context.catalog_search_page.click_activated_favorites_link()

@then('The product is removed from the list')
def step_impl(context):
    context.catalog_search_page.go_to_favorite_section_in_my_account()
    context.catalog_search_page.check_if_empty_favorite_list()

