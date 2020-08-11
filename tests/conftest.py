"""
Shared fixtures
"""
import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'):
    #Read the config file
    with open('config.json') as config_file:
        config = json.load(config_file)
        
    assert config['browser'] in ['Firefox', 'Chrome']
    
    return config

@pytest.fixture
def browser(config):
    #Initialize the Webdriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    
    b.implicitly_wait(config['implicit_wait'])
    
    #Return the Webdriver instance for the setup
    yield b
    
    #Quit the WebDriver instance for the cleanup
    
    b.quit()
    
        
    
