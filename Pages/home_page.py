from selenium.webdriver import ActionChains
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
    SECOND_EMAIL = (By.ID, "customer_login__email")
    PASSWORD = (By.ID, 'quick_login__password')
    SECOND_PASSWARD = (By.ID, "customer_login__password")
    LOGIN_BUTTON = (By.ID, 'quick_login__submit')
    SECOND_LOGIN_BUTTON = (By.ID, "customer_login__submit")
    ERROR_MESSAGE = (By.XPATH, "//*[@id='customer_login']//*[@data-error-type = 'password_mismatch']")

    def open_home_page(self):
        self.chrome.get("https://www.licentepc.ro/")

    def click_accept_cookies_button(self):
        accept_cookie = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(
            self.ACCEPT_COOKIES_BUTTON))
        accept_cookie.click()

    def click_my_account_bottom_link(self):
        bottom_link = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(
            self.CLICK_MY_ACCOUNT_BOTTOM_LINK))

        # Executăm un script JavaScript pentru a seta propietatea CSS Index la valoarea 999.
        # O folosim pentru a ne asigura că elementul se află în prim plan şi nu este acoperit de alte elemente.
        self.chrome.execute_script("arguments[0].style.zIndex = '999';", bottom_link)

        # Executăm un alt script cu care ne asigurăm că elementul este vizibil în pagină.
        self.chrome.execute_script("arguments[0].style.visibility = 'visible';", bottom_link)

        # Un al treilea script JavaScript este utilizat pentru a seta proprietatea CSS display a
        # elementului bottom_link la valoarea 'block'.
        # Acest lucru poate fi folosit pentru a ne asigura că elementul este afişat în modul corect.
        self.chrome.execute_script("arguments[0].style.display = 'block';", bottom_link)
        ActionChains(self.chrome).move_to_element_with_offset(bottom_link, 0, 0).perform()
        self.chrome.implicitly_wait(3)
        bottom_link.click()

    def click_autentificare_link(self):
        max_try = 3
        attempts = 0
        while attempts < max_try:
            try:
                login_button = self.chrome.find_element(*self.LOGIN_LINK)
                if login_button:
                    login_button.click()
                    self.chrome.implicitly_wait(3)
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

    def second_insert_email(self):
        try:
            user_email = self.chrome.find_element(*self.SECOND_EMAIL)
            user_email.send_keys("valentinvlad03@gmail.com")
        except Exception as i:
            logging.error(f"An error occurred while inserting the email: {str(i)}. This email address is invalid.")

    def insert_invalid_password(self, password):
        try:
            user_password = self.chrome.find_element(*self.SECOND_PASSWARD)
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

    def second_click_login_button(self):
        try:
            sing_in_button = self.chrome.find_element(*self.SECOND_LOGIN_BUTTON)
            sing_in_button.click()
        except Exception as i:
            logging.error(f"An error occurred while clicking the Login button: {str(i)}")

    def login_failed(self, error_message):
        alerta = self.chrome.find_element(*self.ERROR_MESSAGE)
        alerta_text = alerta.text
        assert error_message in alerta_text
        logging.info("Login failed => {}".format(error_message))

    def insert_password(self):
        try:
            userpassword = self.chrome.find_element(*self.PASSWORD)
            userpassword.send_keys("Testare123!")
        except Exception as i:
            logging.error(f"An error occurred while inserting the password: {str(i)}")

    def my_account_page(self):
        account_url = "https://www.licentepc.ro/account"
        assert self.chrome.current_url == account_url
        logging.info("Test passed => Current URL match the expected account URL")
