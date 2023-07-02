from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import random
import details.constants as const 

class Details(webdriver.Chrome):
    def __init__(self, driver_path = r'E:/Softwares/chromedriver_win32', teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] = self.driver_path
        super(Details, self).__init__()
        self.implicitly_wait(time_to_wait=15)
        self.maximize_window()
    def __exit__(self, exc_type, exc_value, trace):
        if self.teardown:
            self.quit() # quit the browser

    def land_first_page(self):
        self.get(const.BASE_URL)

    def sign_in(self, email, password):

        time.sleep(random.randint(1,4))
        # entering username
        username = self.find_element(By.ID, "username")
        username.send_keys(email) 
        
        time.sleep(random.randint(2,4))
        # entering password
        pword = self.find_element(By.ID, "password")
        pword.send_keys(password)       
        

        time.sleep(random.randint(2,7))
        # Clicking on the log in button
        self.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(random.randint(2,6))
        current_page = self.find_element(By.CSS_SELECTOR, 'a[class="ember-view block"]')
        url = current_page.get_attribute('href')
        self.get(url)

        time.sleep(random.randint(2,5))

    def education(self):

        creds = {"school": 'Jadavpur University', 
                 "degree": 'B.E.',
                 "field_of_study": 'Production Engineering',
                 "grades": '8.5/10',
                 "activities": 'Debating, MUN, etc.'}
        
        button = self.find_element(By.CSS_SELECTOR, 'a[id="navigation-add-edit-deeplink-add-education"]')
        button.click()

        time.sleep(random.randint(1,3))
        sc = self.find_element(
            By.CSS_SELECTOR, 
            'input[id="single-typeahead-entity-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAEShGo4BR8nbxIOD-U-QXrywb1wR-LxFWs-1-school"]'
            )
        sc.send_keys(creds['school'])
        
        time.sleep(random.randint(1,3))
        deg = self.find_element(
            By.CSS_SELECTOR, 
            'input[id="single-typeahead-entity-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAEShGo4BR8nbxIOD-U-QXrywb1wR-LxFWs-1-degree"]'
            )
        deg.send_keys(creds['degree'])

        time.sleep(random.randint(1,3))
        fos = self.find_element(
            By.CSS_SELECTOR, 
            'input[id="single-typeahead-entity-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAEShGo4BR8nbxIOD-U-QXrywb1wR-LxFWs-1-fieldsOfStudy"]'
            )
        fos.send_keys(creds['field_of_study'])

        time.sleep(random.randint(1,3))
        gd = self.find_element(
            By.CSS_SELECTOR, 
            'input[id="single-line-text-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAEShGo4BR8nbxIOD-U-QXrywb1wR-LxFWs-1-grade"]'
            )
        gd.send_keys(creds['grades'])

        time.sleep(random.randint(1,3))
        act = self.find_element(
            By.CSS_SELECTOR, 
            'textarea[id="multiline-text-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAEShGo4BR8nbxIOD-U-QXrywb1wR-LxFWs-1-activities"]'
            )
        act.send_keys(creds['activities'])

        time.sleep(random.randint(1,3))
        save_button = self.find_element(
            By.CSS_SELECTOR, 
            'button[class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]'
            )
        save_button.click()


"""    def test(self):
        button = self.find_element(
            By.CSS_SELECTOR, 
            'button[class="artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view mh1"]'
            )
        button.click()

        time.sleep(random.randint(1,3))
        element = self.find_element(
            By.CSS_SELECTOR, 
            'a[class="app-aware-link  fb-navigation-button artdeco-button artdeco-button--tertiary mt4"]'
            )
        url = element.get_attribute('href')
        print(url)"""




    