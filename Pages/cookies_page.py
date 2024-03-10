from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from browser import Browser


class Cookies_page(Browser):

    # selectorul pentru linkul cu "Politica de Cookies"
    COOKIES_LINK = (By.XPATH, '//*[@href="/info/cookies"]')
    HOME_LINK = (By.XPATH, '//*[@id="header_logo"]')
    EMAIL_ADDRESS_LINK = (By.XPATH, '//a[@href="mailto:vanzari@licentepc.ro"]')
    TEXT = (By.XPATH, "//*[@id='main']//*[text()='Care este durata de viata a unui cookie?']")

    def open_home_page(self):
        self.chrome.get("https://www.licentepc.ro/")

    def click_cookies_link(self):
        politica_cookies = self.chrome.find_element(*self.COOKIES_LINK)
        self.chrome.execute_script("arguments[0].style.zIndex = '999';", politica_cookies)
        self.chrome.execute_script("arguments[0].style.visibility = 'visible';", politica_cookies)
        self.chrome.execute_script("arguments[0].style.display = 'block';", politica_cookies)
        ActionChains(self.chrome).move_to_element_with_offset(politica_cookies, 0, 0).perform()
        politica_cookies.click()

    def check_text_on_page(self):
        text_to_search = "Care este durata de viata a unui cookie"
        actual_text = self.chrome.find_element(*self.TEXT).text
        if text_to_search in actual_text:
            print(f"The text '{text_to_search}' is shown on this webpage: Politica de Cookies.")
        else:
            print(f"The text '{text_to_search}' is not present on this webpage: Politica de Cookies.")

    def click_return_to_home_page(self):
        button_home = self.chrome.find_element(*self.HOME_LINK)
        button_home.click()

    def open_cookies_policy_page(self):
        self.chrome.get("https://www.licentepc.ro/info/cookies")

