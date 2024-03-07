from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep
import logging


class My_Account_page(Browser):

    # selectorul linkului "Iesire" de pe pagina contului personal
    SIGN_OUT_LINK = (By.XPATH, '//a[@href="https://www.licentepc.ro/logout"]')

    def open_account_page(self):
        self.chrome.get("https://www.licentepc.ro/account")

    def click_on_sign_out_link(self):
        try:
            sing_in_button = self.chrome.find_element(*self.SIGN_OUT_LINK)
            sing_in_button.click()
            sleep(2)
        except Exception as i:
            logging.error(f"An error occurred while clicking the Sign Out button =>  {str(i)}")

    def check_redirect_to_home_page(self):
        homepage_url = "https://www.licentepc.ro"
        assert self.chrome.current_url == homepage_url
        logging.info(f"Test passed: Current URL match the expected home page URL =>  {str(homepage_url)}")
