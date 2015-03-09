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
time.sleep(2)
search.send_keys(Keys.RETURN) # hit return after you enter search text

search = browser.find_element_by_id('MDICtextbox')
for char in DRUG_TWO:
    search.send_keys(char)
time.sleep(2)
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results
browser.quit()