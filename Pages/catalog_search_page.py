from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from browser import Browser
from time import sleep
import logging


class CatalogSearch_page(Browser):

    #  selectorul pentru bara de căutare "Cauta produse" din partea de sus a paginii
    SEARCH_INLINE = (By.XPATH,'//input[@class="search-inline__input form-control"]')
    #  selectorul pentru butonul cu lupa de căutare, din dreapta barei "Cauta produse"
    SEARCH_BUTTON = (By.XPATH, '//button[@class="search-inline__button btn btn-primary"]')
    #  selectorul pentru mesajul secundar de eroare la cautarea de produse inexistente in magazin
    MISSING_PRODUCT_MESSAGE = (By.XPATH,'//div[@class="missing-records__sub-message"]')
    #  selectorul pentru titlul căutarii afişat în partea stângă sus a grilei cu produsele afişate
    RESULTS_PAGE_TITLE = (By.XPATH,'//h1[@class="page__heading"]')
    # selectorii pentru casuta cu optiunile de sortare, cel general si cel pentru pret ascendent
    SORT_VIEW_LABEL = (By.ID, 'sort_options')
    SORT_PRICE_ASCENDING_LABEL = (By.XPATH, '//*[@id="sort_options"]//option[@ value="price_asc"]')


    #  selectorii pentru inimioara de selectat pentru a fi inclus produsul la Favorite
    COREL_PDF_PRODUCT_LINK = (By.XPATH, '//a[@ title="Corel PDF Fusion ENG - Licenta permanenta"]')
    NITRO_PDF_PRODUCT_LINK = (By.XPATH, '//a[@ title="Nitro PDF Professional v13 – licenta permanenta"]')
    FOXIT_PDF_PRODUCT_LINK = (By.XPATH, '//a[@ title="Foxit PDF Editor, v12 Windows/Mac - licenta perpetua"]')


# metode pentru scenariul T7
    def insert_invalid_product(self, invalid_product):
        text_to_search = self.chrome.find_element(*self.SEARCH_INLINE)
        text_to_search.send_keys(Keys.CONTROL, 'a')
        text_to_search.send_keys(Keys.BACKSPACE)
        text_to_search.send_keys(invalid_product)
        sleep(3)

    def click_search_button(self):
        inquiry_square = self.chrome.find_element(*self.SEARCH_BUTTON)
        inquiry_square.click()

    def no_result_msg(self, no_results):
        expected_message = no_results
        visible_message = self.chrome.find_element(*self.MISSING_PRODUCT_MESSAGE)
        assert visible_message == expected_message
        logging.info(f"Test passed => Missing records message is correctly shown :  {str(visible_message)}")



# metode pentru scenariul T8
    def insert_valid_product(self, product_name):
        text_to_search = self.chrome.find_element(*self.SEARCH_INLINE)
        text_to_search.send_keys(Keys.CONTROL, 'a')
        text_to_search.send_keys(Keys.BACKSPACE)
        text_to_search.send_keys(product_name)
        sleep(3)


    def check_listed_products_page_label(self, results_title):
        title_of_page = self.chrome.find_element(*self.RESULTS_PAGE_TITLE)
        current_title = title_of_page.text
        assert current_title == results_title
        logging.info(f"Test passed => The title of page with the searching results is correctly shown :  {str(results_title)}")
        sleep(3)


# metode pentru scenariul T9
    def click_sort_checklist_box(self):
        sorting_checkbox = self.chrome.find_element(*self.SORT_VIEW_LABEL)
        sorting_checkbox.click()

    def select_ascending_price_option(self):
        sorting_option = WebDriverWait(self.chrome, 10).until(
            EC.visibility_of_element_located(self.SORT_PRICE_ASCENDING_LABEL))
        sorting_option.click()

    def check_ascending_order_url(self):
        current_page = self.chrome.current_url
        text_url = current_page.text
        text_to_find = "sort_by=price_asc"
        assert text_to_find in text_url, "The URL doesn't contain the sorting option (ascending price)."



# metode pentru scenariul T10
    def open_search_result_page(self):
        self.chrome.get("https://www.licentepc.ro/catalog/q/PDF")

    def click_add_to_favorites_link(self, product_name):
        product_selector = str('//a[@ title="' + product_name + '"] //button[@ class="grid-image__save-wishlist btn btn-icon"]')
        current_product = self.chrome.find_element(*self.product_selector)
        current_product.click()

    def check_confirmation_message_favorite(self, confirmation_message):
        try:
            alerta = self.chrome.switch_to.alert
            alerta_text = alerta.text
            assert confirmation_message in alerta_text
            logging.info("Adding to Favorites failed. {}".format(confirmation_message))
        except NoAlertPresentException:
            assert False, "Expected message not found."
        sleep(4)





