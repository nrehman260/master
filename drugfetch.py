from selenium import webdriver

DRUG_ID = "137"

browser = webdriver.Firefox()
browser.get("https://pubchem.ncbi.nlm.nih.gov/compound/" + DRUG_ID)

name = browser.find_elements_by_tag_name('body')[0].get_attribute("data-pubchem-title")

print(name)
browser.quit()