from selenium import webdriver

class Booking(webdriver.Chrome):
    def __init__(self): # driver path missing  
        super(Booking, self).__init__()
