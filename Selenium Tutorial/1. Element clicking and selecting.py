import  os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH']+= r'E:/Softwares/chromedriver_win32'

driver = webdriver.Chrome()

driver.get("https://www.seleniumeasy.com/tags/file-download")
driver.implicitly_wait(time_to_wait=8) # waiting time for any element to load, if the website gets loaded earlier, then the control goes to the next line
# use driver.implicitly_wait only once in the whole code

my_element = driver.find_element(by='id', value='edit-search-block-form--2') # Searching by element_id

my_element.click()

# Explicit Waiting time
"""WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'), # Element filtration
        'Complete!'# The expected text
    )
) """
while(True):
    pass