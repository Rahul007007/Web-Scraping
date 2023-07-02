import  os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.environ['PATH']+= r'E:/Softwares/chromedriver_win32'

driver = webdriver.Chrome()

driver.get('https://www.calculator.net/math-calculator.html')
driver.implicitly_wait(5)
search = driver.find_element(by='id', value='twotabsearchtextbox')
#driver.find_element_by_css_selector()

search.send_keys('Camera')
search.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)