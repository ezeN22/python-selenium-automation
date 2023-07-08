from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users\18327\python-selenium-automation\chromedriver.exe')
driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH,"//span[@class= 'nav-line-2']")

 expected_text = 'Sing in'

actual-text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert actual_text == expected_text

# verify email field is present
assert driver.find_element(By.ID, 'ap_email').is_displayed()

