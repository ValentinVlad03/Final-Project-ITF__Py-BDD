from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from browser import Browser
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

    # selectorii pentru căsuţa cu opţiunile de sortare, cel general şi cel pentru pret_ascendent
    SORT_VIEW_LABEL = (By.ID, 'sort_options')
    SORT_PRICE_ASCENDING_LABEL = (By.XPATH, '//*[@id="sort_options"]//option[@ value="price_asc"]')
    FAVORITE_BUTTON = (By.XPATH, '//*[@id="main"]//*[@title="Adauga la Favorite"]')
    HEART_FAVORITE_LINK = (By.XPATH, '//*[@id="header_wrapper"]/div[3]/a[1]/div')
    COREL_PDF_PRODUCT = (By.XPATH, '//*[@id="main"]//a[@title ="Corel PDF Fusion ENG - Licenta permanenta"]')

    # selectorii pentru a naviga către pagina produsului "Corel PDF Fusion" pentru a-l scoate din lista de Favorite
    SOFTWARE_CATEGORY_LINK = (By.XPATH, '//li[@id="header_menu_item_100009465"] //a[@href="/catalog/software-653469"]')
    COREL_CATEGORY_LINK = (By.XPATH, '//li[@class="facet__option facet__option--tree facet__option--level-2"] //a[@href="/catalog/corel-653419"]')
    COREL_PDF_FUSION_CATEGORY_LINK = (By.XPATH, '//li[@class="facet__option facet__option--tree facet__option--level-3"] //a[@href="/catalog/corel-pdf-fusion-653433"]')
    COREL_PDF_FUSION_PRODUCT_LINK = (By.XPATH, '//div[@class="product product--grid"] //a[@class="product__name"]')
    COREL_PDF_SAVE_WISHLIST_LINK = (By.XPATH, '//a[@class="product-summary__save-wishlist btn product-summary__save-wishlist--saved"]')
    EMPTY_LIST_FAV_LIST_MSG = (By.XPATH, '//h1[@class="wishlist__empty-title"]')



# metode pentru scenariul T6
    def insert_invalid_product(self, invalid_product):
        text_to_search = self.chrome.find_element(*self.SEARCH_INLINE)
        text_to_search.send_keys(Keys.CONTROL, 'a')
        text_to_search.send_keys(Keys.BACKSPACE)
        text_to_search.send_keys(invalid_product)

    def click_search_button(self):
        inquiry_square = self.chrome.find_element(*self.SEARCH_BUTTON)
        inquiry_square.click()

    def no_result_msg(self, no_results):
        expected_message = no_results
        visible_message = self.chrome.find_element(*self.MISSING_PRODUCT_MESSAGE).text
        assert visible_message.strip() == expected_message.strip()  # ne folosim de functia strip ca să
        # eliminăm spaţiile goale de la începutul sau sfârşitul unui şir de caractere, în caz că există.
        logging.info(f"Test passed => Missing records message is correctly shown :  {str(visible_message)}")



# metode pentru scenariul T7
    def insert_valid_product(self, product_name):
        text_to_search = self.chrome.find_element(*self.SEARCH_INLINE)
        text_to_search.send_keys(Keys.CONTROL, 'a')
        text_to_search.send_keys(Keys.BACKSPACE)
        text_to_search.send_keys(product_name)

    def check_listed_products_page_label(self, results_title):
        title_of_page = self.chrome.find_element(*self.RESULTS_PAGE_TITLE)
        current_title = title_of_page.text
        assert current_title == results_title
        logging.info(f"Test passed => The title of page with the searching results is correctly shown :  {str(results_title)}")



# metode pentru scenariul T8
    def click_sort_checklist_box(self):
        sorting_checkbox = self.chrome.find_element(*self.SORT_VIEW_LABEL)
        sorting_checkbox.click()

    def select_ascending_price_option(self):
        sorting_option = WebDriverWait(self.chrome, 10).until(
            EC.visibility_of_element_located(self.SORT_PRICE_ASCENDING_LABEL))
        # am adaugat o pauză de aşteptare pentru a avea timp să se afişeze lista cu opţiuni de sortare
        sorting_option.click()

    def check_ascending_order_url(self):
        current_page = self.chrome.current_url
        text_to_find = "sort_by=price_asc"
        assert text_to_find in current_page, "The URL doesn't contain the sorting option (ascending price)."



# metode pentru scenariul T9
    def open_search_result_page(self):
        self.chrome.get("https://www.licentepc.ro/catalog/q/PDF")

    def click_add_to_favorites_link(self):
        search_bar = self.chrome.find_element(*self.SEARCH_INLINE)
        search_bar.send_keys("Corel PDF Fusion ENG - Licenta permanenta")
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        # am adaugat o pauză de aşteptare pentru a avea timp să se încarce butonul de FAVORITE
        fav_button = WebDriverWait(self.chrome, 10).until(
            EC.visibility_of_element_located(self.FAVORITE_BUTTON))
        fav_button.click()

    def go_to_favorite_section_in_my_account(self):
        self.chrome.get("https://www.licentepc.ro/wishlist")

    def check_corel_pdf_in_favorite(self):
        product_search = self.chrome.find_element(*self.COREL_PDF_PRODUCT)
        if product_search.is_displayed():
            print(f"The product named Corel PDF is listed in Favorite list")
        else:
            print(f"The product named Corel PDF is not listed.")



# metode pentru scenariul T10
    def click_software_category_link(self):
        software_category = self.chrome.find_element(*self.SOFTWARE_CATEGORY_LINK)
        software_category.click()

    def click_corel_category_link(self):
        corel_category = WebDriverWait(self.chrome, 10).until(
            EC.visibility_of_element_located(self.COREL_CATEGORY_LINK))
        corel_category.click()

    def click_corel_pdf_fusion_category_link(self):
        pdf_category = self.chrome.find_element(*self.COREL_PDF_FUSION_CATEGORY_LINK)
        pdf_category.click()

    def click_on_product_name(self):
        product_name = self.chrome.find_element(*self.COREL_PDF_FUSION_PRODUCT_LINK)
        product_name.click()

    def click_activated_favorites_link(self):
        save_to_wishlist = self.chrome.find_element(*self.COREL_PDF_SAVE_WISHLIST_LINK)
        save_to_wishlist.click()

    def check_if_empty_favorite_list(self):
        expected_msg = "Nu ai adaugat inca nimic in Favorite"
        displayed_msg = self.chrome.find_element(*self.EMPTY_LIST_FAV_LIST_MSG).text
        assert expected_msg == displayed_msg
        logging.info("Test passed => The product named 'Corel PDF' is not listed in the 'Favorites' list.")
