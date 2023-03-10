from booking.booking import Booking
import time

start = time.time()
with Booking() as bot:
    bot.land_first_page()
    bot.change_language_to_Eng()
    bot.catch_login_ad()
    bot.change_currency(currency="CAD")
    bot.select_place_to_go('Zhanjiang')
    bot.select_dates(check_in_date='2023-03-05',check_out_date='2023-03-08')
    bot.select_adults(1)
    bot.search()
    bot.apply_filtration()
end = time.time()
print("total run time " + str(end - start) )