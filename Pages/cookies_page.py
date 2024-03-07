from selenium.webdriver.common.by import By
from selenium import webdriver
from browser import Browser
from time import sleep


class Cookies_page(Browser):

    # selectorul pentru linkul cu "Politica de Cookies"
    COOKIES_LINK = (By.XPATH, '//*[@href="/info/cookies"]')
    HOME_LINK = (By.ID, '//*[@id="header_logo"]')

    def open_home_page(self):
        self.chrome.get("https://www.licentepc.ro/")

    def click_cookies_link(self):
        politica_cookies = self.chrome.find_element(*self.COOKIES_LINK)
        politica_cookies.click()
        sleep(5)

    def check_text_on_page(self):
        text_to_search = "Care este durata de viata a unui cookie"
        specified_url = self.chrome.current_url
        driver = webdriver.Chrome()
        driver.get(specified_url)
        get_source = driver.page_source
        if text_to_search in get_source:
            print(f"The text '{text_to_search}' is shown on this webpage: Politica de Cookies")
        else:
            print(f"The text '{text_to_search}' is not present on this webpage: Politica de Cookies")

    def click_return_to_home_page(self):
        button_home = self.chrome.find_element(*self.HOME_LINK)
        button_home.click()
