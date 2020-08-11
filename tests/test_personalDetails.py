"""
Testing filling in the personal data and submitting it
"""

import pytest

from pages.TextBox import ToolsQATextBoxPage


#Scenario 1: user fills in name
def test_fill_in_name(browser):
    TextBox_page = ToolsQATextBoxPage(browser)
    #NAME = "Ville Kalle"
    
    #Given the user is on the Text Box page
    TextBox_page.load()
    
    #When user fills in full name
    TextBox_page.fillName("Pertti Koponen")
    
    #And user clicks submit
    TextBox_page.submit()
    
    #Then the name should be shown
    print(TextBox_page.getName())
    assert "Pertti Koponen" in TextBox_page.getName() 


#And user fills in email
#And user fills in current address
#And user fills in permanent address
