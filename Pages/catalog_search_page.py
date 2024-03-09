from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
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
    FAVORITE_BUTTON = (By.XPATH, '//*[@id="main"]//*[@title="Adauga la Favorite"]')
    HEART_FAVORITE_LINK = (By.XPATH, '//*[@id="header_wrapper"]/div[3]/a[1]/div')
    COREL_PDF_PRODUCT = (By.XPATH, '//*[@id="main"]//a[@title ="Corel PDF Fusion ENG - Licenta permanenta"]')

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
        visible_message = self.chrome.find_element(*self.MISSING_PRODUCT_MESSAGE).text  #
        assert visible_message.strip() == expected_message.strip()  # ne folosim de functia stipe ca sa
        # eliminam spatiile goala de la inceputul sau sfarsitul unui sir de caractere, in caz ca exista
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
        text_to_find = "sort_by=price_asc"
        assert text_to_find in current_page, "The URL doesn't contain the sorting option (ascending price)."


# metode pentru scenariul T10
    def open_search_result_page(self):
        self.chrome.get("https://www.licentepc.ro/catalog/q/PDF")

    def click_add_to_favorites_link(self):
        search_bar = self.chrome.find_element(*self.SEARCH_INLINE)
        search_bar.send_keys("Corel PDF Fusion ENG - Licenta permanenta")
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        self.chrome.find_element(*self.FAVORITE_BUTTON).click()

    def check_corel_pdf_in_favorite(self):
        self.chrome.get('https://www.licentepc.ro/wishlist')
        product_search = self.chrome.find_element(*self.COREL_PDF_PRODUCT)
        if product_search.is_displayed():
            print(f"The product named Corel PDF is listed in Favorite list")
        else:
            print(f"The product named Corel PDF is not listed.")




