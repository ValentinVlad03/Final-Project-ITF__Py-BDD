from browser import Browser
from Pages.home_page import Home_page
from Pages.edit_account_page import Edit_Account_page
from Pages.cookies_page import Cookies_page
from Pages.funding_projects_page import FundingProjects_page
from Pages.catalog_search_page import CatalogSearch_page
from Pages.my_account_page import My_Account_page


def before_all(context):
    context.browser = Browser()
    context.browser.maximise_windows()
    # aici vom instantia obiectele din folderul Pages (adică atunci când vom adăuga fişiere în folderul Pages vom
    # instanţia aici obiectele din ele)
    context.home_page = Home_page()
    context.edit_account_page = Edit_Account_page()
    context.cookies_page = Cookies_page()
    context.funding_projects_page = FundingProjects_page()
    context.catalog_search_page = CatalogSearch_page()
    context.my_account_page = My_Account_page()

def after_all(context):
    context.browser.close()
