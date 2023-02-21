import time
import booking.constants as const
from selenium.webdriver.common.by import By
from selenium import webdriver



class Booking(webdriver.Firefox):
    def __init__(self, teardown = False): # driver path missing  
        super(Booking, self).__init__()
        
        self.teardown = teardown
        self.implicitly_wait(3)
        self.maximize_window()
    def land_first_page(self):
        self.get(const.BASE_URL)
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    def change_currency(self,currency = None):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()
        selected_currency_element = self.find_elements(By.CLASS_NAME, 'ea1163d21f') #three letter currency
        for element in selected_currency_element:
            if element.text == currency:
                element.click()
                break
        time.sleep(4)
    def select_place_to_go(self,place_to_go):
        search_field = self.find_element(By.NAME, 'ss')
        search_field.click()
        search_field.send_keys(place_to_go)
        time.sleep(2)
        try:
            self.find_element(By.CLASS_NAME,'a40619bfbe').click()
        except:
            self.find_element(By.CSS_SELECTOR,'li[data-i="0"]').click()
        time.sleep(4)
    def select_dates(self,check_in_date,check_out_date):
        try:
            check_in_element = self.find_element(
            By.CSS_SELECTOR,
            f'td[data-date="{check_in_date}"]'
        )
        except:
            check_in_element = self.find_element(
                By.CSS_SELECTOR,
                f'span[data-date="{check_in_date}"]'
        )
        check_in_element.click()
        try:
            check_out_element = self.find_element(
            By.CSS_SELECTOR,
            f'td[data-date="{check_out_date}"]'
        )
        except:
            check_out_element = self.find_element(
                By.CSS_SELECTOR,
                f'span[data-date="{check_out_date}"]'
        )
        check_out_element.click()

        
