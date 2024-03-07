from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from browser import Browser
from time import sleep
import logging


class Home_page(Browser):

    # selectorii de pe licentepc
    LOGIN_LINK = (By.XPATH, '//*[@id="header_wrapper"]//*[@title="Contul meu"]')
    CLICK_MY_ACCOUNT_BOTTOM_LINK = (By.XPATH, '//a[@href="/account"]')
    ACCEPT_COOKIES_BUTTON = (By.XPATH, '//*[@id="cookie-policy-overlay"]//button[1][@class = "btn btn-primary"]')
    EMAIL = (By.ID, 'quick_login__email')
    PASSWORD = (By.ID, 'quick_login__password')
    LOGIN_BUTTON = (By.ID, 'quick_login__submit')

    def open_home_page(self):
        self.chrome.get("https://www.licentepc.ro/")

    def click_accept_cookies_button(self):
        accept_cookie = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(
            self.ACCEPT_COOKIES_BUTTON))
        accept_cookie.click()

    def click_my_account_bottom_link(self):
        bottom_link = self.chrome.find_element(*self.CLICK_MY_ACCOUNT_BOTTOM_LINK)
        bottom_link.click()

    def click_autentificare_link(self):
        max_try = 3
        attempts = 0
        while attempts < max_try:
            try:
                login_button = self.chrome.find_element(*self.LOGIN_LINK)
                if login_button:
                    login_button.click()
                    sleep(3)    # dacă ştergi sleepul ăsta îţi dă eroare pentru
                                # că nu are timp suficient să apară fereastra de introducere a credenţialelor
                    break
                else:
                    raise AssertionError("Login button element not found.")
            except Exception as i:
                logging.error(f"An error occurred while clicking the Login button: {str(i)}")
            attempts += 1

    def insert_email(self):
        try:
            user_email = self.chrome.find_element(*self.EMAIL)
            user_email.send_keys("valentinvlad03@gmail.com")
        except Exception as i:
            logging.error(f"An error occurred while inserting the email: {str(i)}. This email address is invalid.")

    def insert_invalid_password(self, password):
        try:
            user_password = self.chrome.find_element(*self.PASSWORD)
            user_password.send_keys(password)
            sleep(1)
        except Exception as i:
            logging.error(f"An error occurred while inserting the password: {str(i)}")

    def click_login_button(self):
        try:
            sing_in_button = self.chrome.find_element(*self.LOGIN_BUTTON)
            sing_in_button.click()
        except Exception as i:
            logging.error(f"An error occurred while clicking the Login button: {str(i)}")

    def login_failed(self, error_message):
        try:
            alerta = self.chrome.switch_to.alert
            alerta_text = alerta.text
            assert error_message in alerta_text
            alerta.accept()
            logging.info("Login failed {}".format(error_message))
        except NoAlertPresentException:
            assert False, "Expected alert not found."
        sleep(4)

    def insert_password(self):
        try:
            userpassword = self.chrome.find_element(*self.PASSWORD)
            userpassword.send_keys("Testare123!")
        except Exception as i:
            logging.error(f"An error occurred while inserting the password: {str(i)}")

    def my_account_page(self):
        account_url = "https://www.licentepc.ro/account"
        assert self.chrome.current_url == account_url
        logging.info("Test passed : Current URL match the expected account URL")
