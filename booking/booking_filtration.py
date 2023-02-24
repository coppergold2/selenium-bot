from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver
    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(By.ID,'filter_group_class_:R1kq:')
        star_child_elements = star_filtration_box.find_element(By.CSS_SELECTOR,'div[data-filters-item="class:class=f{star_values[0]}"]').click()
        