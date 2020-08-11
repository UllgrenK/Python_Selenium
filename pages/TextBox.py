"""
This is the page object for the Tools QA Text Box page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ToolsQATextBoxPage:
    #URL
    URL = 'https://demoqa.com/text-box'
    
    #Locators
    FULL_NAME_INPUT = (By.ID, 'userName') 
    #EMAIL_INPUT=
    #CURRENT_ADDRESS_INPUT=
    #PERMANENT_ADDRESS_INPUT=
    SUBMIT_BUTTON = (By.ID, 'submit')
    NAME_SHOW = (By.ID, 'name')
    #EMAIL_SHOW=
    #CURRENT_ADDRESS_SHOW=
    #PERMANENT_ADDRESS_SHOW
    
    #Initializer
    def __init__(self, browser):
        self.browser = browser
        
    # Methods for interacting with the page
    
    def load(self):
        self.browser.get(self.URL)
        
    def fillName(self, name):
        name_input = self.browser.find_element(*self.FULL_NAME_INPUT)
        name_input.send_keys(name)
        
    
    def submit(self):
        self.browser.find_element(*self.SUBMIT_BUTTON).click()
        
    
    def getName(self):
        name_output = self.browser.find_element(*self.NAME_SHOW).text
        #name = name_output.get_attribute('value')
        print(name_output)
        return name_output
        
        