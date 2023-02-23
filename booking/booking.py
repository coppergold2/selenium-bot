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
    def change_language_to_Eng(self):
        language_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-language-picker-trigger"]')
        language_element.click()
        englishuk_element = self.find_elements(By.CLASS_NAME, 'cf67405157')
        for element in englishuk_element:
            if element.text == "English (US)":
                element.click()
                break

        
    def change_currency(self,currency = None):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()
        selected_currency_element = self.find_elements(By.CLASS_NAME, 'ea1163d21f') #three letter currency
        for element in selected_currency_element:
            if element.text == currency:
                element.click()
                break
    def select_place_to_go(self,place_to_go):
        search_field = self.find_element(By.NAME, 'ss')
        search_field.click()
        search_field.send_keys(place_to_go)
        time.sleep(1)
        try:
            self.find_element(By.CLASS_NAME,'a40619bfbe').click()
        except:
            self.find_element(By.CSS_SELECTOR,'li[data-i="0"]').click()
        
    def catch_login_ad(self):
            time.sleep(1)
            iframe = self.find_element(By.XPATH,'/html/body/div[21]/div[2]/div[2]/iframe')
            self.switch_to.frame(iframe)
            close_button = self.find_element(By.CLASS_NAME,"Bz112c-r9oPif")
            close_button.click()
            self.switch_to.default_content()
    def select_dates(self,check_in_date,check_out_date):  # current code cannot select date in the next two or more months, but can be implemented
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
    def select_adults(self,count):
        try:
            selection_element = self.find_element(By.CSS_SELECTOR,'button[data-testid="occupancy-config"]')
            selection_element.click()
        except:
            selection_element = self.find_element(By.CLASS_NAME,'xp__input-group.xp__guests')
            selection_element.click()
        try:
            decrease_adult_element = self.find_element(By.CSS_SELECTOR,'button[aria-label="Decrease number of Adults"]')
        except:
            decrease_adult_element  = self.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[1]')
        while True:
            adults_value_element = int(self.find_element(By.ID,'group_adults').get_attribute('value'))
            print("hi")
            if (adults_value_element != 1): 
                print(adults_value_element)
                decrease_adult_element.click()
            else:
                break
        try:
            increase_adult_element = self.find_element(By.CSS_SELECTOR,'button[aria-label="Increase number of Adults"]')
        except:
            increase_adult_element = self.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[2]')
        while True:
            adults_value_element = int(self.find_element(By.ID,'group_adults').get_attribute('value'))
            if (adults_value_element < count):
                increase_adult_element.click()
            else:
                break

