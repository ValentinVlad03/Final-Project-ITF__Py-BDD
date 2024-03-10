from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep
import logging


class Edit_Account_page(Browser):

    # selector on account page
    UPDATE_ACCOUNT_LINK = (By.CSS_SELECTOR, '#main > section > div > aside.page__aside-main > ul > li.customer-menu__item.customer-menu__item--edit-account > a')
    # selectors on edit_account page
    ADDRESS = (By.ID, 'customer_update__billing_address_1')
    UPDATE_BUTTON = (By.XPATH, '//*[@id="customer_update__submit"]')

    def open_account_page(self):
        self.chrome.get("https://www.licentepc.ro/account")

    def open_edit_account_page(self):
        self.chrome.get("https://www.licentepc.ro/edit_account")

    def click_update_account_link(self):
        try:
            sing_in_button = self.chrome.find_element(*self.UPDATE_ACCOUNT_LINK)
            sing_in_button.click()
            sleep(2)
        except Exception as i:
            logging.error(f"An error occurred while clicking the Edit Account button =>  {str(i)}")

    def my_account_page(self):
        account_url = "https://www.licentepc.ro/account"
        assert self.chrome.current_url == account_url
        logging.info(f"Test passed => Current URL match the expected account URL: {str(account_url)}")

    def delete_current_address(self):
        text_address = self.chrome.find_element(*self.ADDRESS)
        text_address.send_keys(Keys.CONTROL, 'a')
        text_address.send_keys(Keys.BACKSPACE)
        sleep(2)

    def enter_new_address(self):
        text_address = self.chrome.find_element(*self.ADDRESS)
        text_address.send_keys("Str. Veteranilor nr. 12, Bloc C8, Sc. A, Etaj 1, Apt. 6")
        sleep(3)

    def click_update_button(self):
        update_now = self.chrome.find_element(*self.UPDATE_BUTTON)
        self.chrome.execute_script("arguments[0].style.zIndex = '999';", update_now)
        self.chrome.execute_script("arguments[0].style.visibility = 'visible';", update_now)
        self.chrome.execute_script("arguments[0].style.display = 'block';", update_now)
        ActionChains(self.chrome).move_to_element_with_offset(update_now, 0, 0).perform()
        update_now.click()
