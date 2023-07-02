from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.thesun.co.uk/")
driver.implicitly_wait(30)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')
for container in containers:
    title = container.find_element(by="xpath", value= './a/h2').text
    subtitle = container.find_element(by="xpath", value= './a/p').text
    link = container.find_element(by="xpath", value= './a').get_attribute("href")

