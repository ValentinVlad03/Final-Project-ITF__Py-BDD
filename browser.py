from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import logging


class Browser():
    s = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=s)
    chrome.maximize_window()
    logging.basicConfig(level=logging.INFO)

    # chrome.implicitly_wait(10)
    # chrome.set_page_load_timeout(10)

    def maximise_windows(self):
        self.chrome.maximize_window()
        
    def close(self):
        self.chrome.quit()
