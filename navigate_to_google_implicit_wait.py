from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.implicitly_wait(15)
search_field = driver.find_element_by_css_selector("input[name=q]")
driver.quit()