import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

DRUG_ONE = "codeine"
DRUG_TWO = "Adderall"

browser = webdriver.Firefox()
browser.get('http://reference.medscape.com/drug-interactionchecker')

search = browser.find_element_by_id('MDICtextbox')
for char in DRUG_ONE:    
    search.send_keys(char)
search.send_keys(Keys.RETURN) # hit return after you enter search text

search = browser.find_element_by_id('MDICtextbox')
for char in DRUG_TWO:
    search.send_keys(char)
search.send_keys(Keys.RETURN) # hit return after you enter search text

contraindicated = browser.find_element_by_id('contraindicated_list')
significant = browser.find_element_by_id('significant_list')
serious = browser.find_element_by_id('serious_list')
minor = browser.find_element_by_id('minor_list')


# browser.quit()