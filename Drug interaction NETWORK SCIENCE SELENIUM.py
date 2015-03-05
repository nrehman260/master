import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://reference.medscape.com/drug-interactionchecker')

search = browser.find_element_by_id('MDICtextbox')
search.send_keys("codeine")
search.send_keys(Keys.RETURN) # hit return after you enter search text

search = browser.find_element_by_id('MDICtextbox')
search.send_keys("adderall")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results
browser.quit()