from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency="CAD")
    bot.select_place_to_go('Zhanjiang')
    bot.select_dates(check_in_date='2023-03-05',check_out_date='2023-03-08')
    
    