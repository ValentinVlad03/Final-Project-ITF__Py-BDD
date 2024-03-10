from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from browser import Browser
import logging


class FundingProjects_page(Browser):

    #  selectorul pentru linkul cu "Proiecte Fonduri"
    PROJECTS_LINK = (By.XPATH, '//*[@id="help"]//*[text()="Proiecte Fonduri"]')
    #  linkul catre site-ul oficial al Asus
    ASUS_LINK = (By.XPATH, '//*[@title="Asus"]')

    def open_home_page(self):
        self.chrome.get("https://www.licentepc.ro/")

    def open_funding_projects_page(self):
        proiecte_fonduri = self.chrome.find_element(*self.PROJECTS_LINK)
        self.chrome.execute_script("arguments[0].style.zIndex = '999';", proiecte_fonduri)
        self.chrome.execute_script("arguments[0].style.visibility = 'visible';", proiecte_fonduri)
        self.chrome.execute_script("arguments[0].style.display = 'block';", proiecte_fonduri)
        ActionChains(self.chrome).move_to_element_with_offset(proiecte_fonduri, 0, 0).perform()
        proiecte_fonduri.click()

    def click_on_asus_link(self):
        selected_link = self.chrome.find_element(*self.ASUS_LINK)
        selected_link.click()

    def check_current_url(self):
        # stabilesc care este tab-ul principal
        main_tab = self.chrome.current_window_handle
        # îi spun că s-a mai deschis un nou tab
        new_tab = self.chrome.window_handles[-1]
        # îi spun să se mute pe noul tab
        self.chrome.switch_to.window(new_tab)
        asus_url = "https://www.asus.com/ro/"
        assert self.chrome.current_url == asus_url
        logging.info(f"Test passed => Current URL match the expected URL: {str(asus_url)}")
        # îi spun să închidă noul tab deschis
        self.chrome.close()
        # îi spun să se mute înapoi pe tab-ul principal
        self.chrome.switch_to.window(main_tab)
