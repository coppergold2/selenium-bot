from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver
    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(By.CSS_SELECTOR,'div[data-filters-group="class"]')
        for star_value in star_values:
            star_child_elements = star_filtration_box.find_element(By.CSS_SELECTOR,f'div[data-filters-item="class:class={star_value}"]')
            star_child_elements.click()
    def sort_search_result(self):
        sortlist = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="sorters-dropdown-trigger"]')
        sortlist.click()
        by_class_and_price_element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="class_and_price"]')
        by_class_and_price_element.click()
        