"""
This is the page object for the Tools QA Text Box page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class ToolsQATextBoxPage:
    #URL
    URL = 'https://demoqa.com/text-box'
    
    #Locators
    FULL_NAME_INPUT = (By.ID, 'userName') 
    EMAIL_INPUT= (By.ID, 'userEmail')
    CURRENT_ADDRESS_INPUT= (By.ID, 'currentAddress')
    PERMANENT_ADDRESS_INPUT= (By.ID, 'permanentAddress')
    SUBMIT_BUTTON = (By.ID, 'submit')
    NAME_SHOW = (By.ID, 'name')
    EMAIL_SHOW= (By.ID, 'email')
    CURRENT_ADDRESS_SHOW= (By.XPATH, '//p[@id="currentAddress"]')
    PERMANENT_ADDRESS_SHOW = (By.XPATH, '//p[@id="permanentAddress"]')
    
    #Initializer
    def __init__(self, browser):
        self.browser = browser
        
    # Methods for interacting with the page
    
    def load(self):
        self.browser.get(self.URL)
        
    def fillName(self, name):
        name_input = self.browser.find_element(*self.FULL_NAME_INPUT)
        name_input.send_keys(name)
        
    def fillEmail(self, email):
        email_input = self.browser.find_element(*self.EMAIL_INPUT)
        email_input.send_keys(email)
    
    def fillCurrentAddress(self, caddress):
        caddress_input = self.browser.find_element(*self.CURRENT_ADDRESS_INPUT)
        caddress_input.send_keys(caddress)
        
    def fillPermanentAddress(self, paddress):
        paddress_input = self.browser.find_element(*self.PERMANENT_ADDRESS_INPUT)
        paddress_input.send_keys(paddress)
      
    def submit(self):
        self.browser.find_element(*self.SUBMIT_BUTTON).click()
        
    
    def getName(self):
        name_output = self.browser.find_element(*self.NAME_SHOW).text
        return name_output
    
    def getEmail(self):
        email_output = self.browser.find_element(*self.EMAIL_SHOW).text
        return email_output
    
    def getCurrentAddress(self):
        caddress_output = self.browser.find_element(*self.CURRENT_ADDRESS_SHOW).text
        return caddress_output
    
    def getPermanentAddress(self):
        paddress_output = self.browser.find_element(*self.PERMANENT_ADDRESS_SHOW).text
        return paddress_output
    
    def getEmailTooltip(self):
        email_input = self.browser.find_element(*self.EMAIL_INPUT)
        tooltip_hover = ActionChains(self).move_to_element(email_input)
        #getting the mouse hover text quite difficult: not in the page source, but in CSS properties
        tooltip_hover.perform()
        
        
        
        