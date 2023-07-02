from booking.booking import Booking
import time

with Booking() as bot:
    bot.land_first_page()
    bot.close_signup()
    bot.change_currency(currency='USD')
    bot.select_place_to_go(place_to_go='Delhi')
    time.sleep(5)