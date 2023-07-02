from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import booking.constants as const 

class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r'E:/Softwares/chromedriver_win32', teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] = self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(time_to_wait=15)
        self.maximize_window()
    def __exit__(self, exc_type, exc_value, trace):
        if self.teardown:
            self.quit() # quit the browser

    def land_first_page(self):
        self.get(const.BASE_URL)

    def close_signup(self):
        close = self.find_element(By.CSS_SELECTOR, 
                                    value='path[d="M13.31 12l6.89-6.89a.93.93 0 1 0-1.31-1.31L12 10.69 5.11 3.8A.93.93 0 0 0 3.8 5.11L10.69 12 3.8 18.89a.93.93 0 0 0 1.31 1.31L12 13.31l6.89 6.89a.93.93 0 1 0 1.31-1.31z"]')
        
        close.click()

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR,
            value='button[data-testid="header-currency-picker-trigger"]'
        )

        currency_element.click()
        elements = self.find_elements(By.CSS_SELECTOR, value = 'div[class=" ea1163d21f"]')
        for element in elements:
            if element.text == currency:
                print(element.text)
                element.click()
                break

    def select_place_to_go(self, place_to_go = None):
        search_field = self.find_element(By.CSS_SELECTOR, value= 'input[name="ss"]')
        search_field.clear()
        search_field.send_keys(place_to_go)

        
