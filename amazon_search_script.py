from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users\18327\python-selenium-automation\chromedriver.exe')
driver.get('https://www.amazon.com/')

driver.find_element(By.ID,'twotabsearchtextbox').send_keys('table')
driver.find_element(By.ID, 'nav-search-submit-button').click()

