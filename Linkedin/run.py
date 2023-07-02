from details.details import Details
import time
email = 'nottrishanu@gmail.com'
password = 'captainprice'
with Details() as bot:
    bot.land_first_page()
    bot.sign_in(email, password)
    bot.education()
    #bot.test()
    time.sleep(5)
