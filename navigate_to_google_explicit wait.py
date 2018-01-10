from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")

flocator = "input[name=q]"

try:
    search_field = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, flocator)))
finally:
    driver.quit()