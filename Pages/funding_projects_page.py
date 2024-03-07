from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep
import logging


class FundingProjects_page(Browser):

    #  selectorul pentru linkul cu "Proiecte Fonduri"
    PROJECTS_LINK = (By.XPATH, '//*[@href="/info/cookies"]')
    #  linkul catre site-ul oficial al Asus
    ASUS_LINK = (By.XPATH, '//*[@title="Asus"]')

    def open_home_page(self):
        self.chrome.get("https://www.licentepc.ro/")

    def open_funding_projects_page(self):
        proiecte_fonduri = self.chrome.find_element(*self.PROJECTS_LINK)
        proiecte_fonduri.click()
        sleep(3)

    def click_on_asus_link(self):
        selected_link = self.chrome.find_element(*self.ASUS_LINK)
        selected_link.click()

    def check_current_url(self):
        asus_url = "https://www.asus.com/ro/"
        assert self.chrome.current_url == asus_url
        logging.info(f"Test passed => Current URL match the expected URL :  {str(asus_url)}")
