"""
Testing filling in the personal data and submitting it
"""

import pytest

from pages.TextBox import ToolsQATextBoxPage


#Scenario 1: user fills in name
def test_fill_in_name(browser):
    TextBox_page = ToolsQATextBoxPage(browser)
    NAME = "Ville Kalle"
    
    #Given the user is on the Text Box page
    TextBox_page.load()
    
    #When user fills in full name
    TextBox_page.fillName(NAME)
    
    #And user clicks submit
    TextBox_page.submit()
    
    #Then the name should be shown
    print(TextBox_page.getName())
    assert NAME in TextBox_page.getName() 


#Scenario2: User fills in all info
@pytest.mark.parametrize("name, email, current_address, permanent_address", [("Pertti Kosonen", "pk@iki.fi", "Hevostie 2", "D-kuja 5"), ("Ville Kauppinen", "ttttt@lll.gg", "D-kuja","rrrr")])
def test_fill_in_all_fields (browser, name, email, current_address, permanent_address):
    
        
    #Given the user is on the Text Box page
    TextBox_page = ToolsQATextBoxPage(browser)
    TextBox_page.load()
    
    #When user fills in all info 
    TextBox_page.fillName(name)
    TextBox_page.fillEmail(email)
    TextBox_page.fillCurrentAddress(current_address)
    TextBox_page.fillPermanentAddress(permanent_address)
       
    TextBox_page.submit()
    
    #Then the info should be shown on the page
    assert name in TextBox_page.getName()
    assert email in TextBox_page.getEmail()
    assert current_address in TextBox_page.getCurrentAddress()
    assert permanent_address in TextBox_page.getPermanentAddress()
    
#Scenario3: invalid email address