from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users\18327\python-selenium-automation\chromedriver.exe')
driver.get('https://www.amazon.com/')

# Amazon logo, search By Xpath, tag and attribute.
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")

# Email field, search by ID,
driver.find_element(By.ID, "ap_email")

# Continue button,search By ID
driver.find_element(By.ID,"continue").click()

# continue button search By Xpath, tag and attribute

driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")

# Conditions of Use and Privacy Notice.search by Xpath, contains:

driver.find_element(By.XPATH,"//a[contains(@href, 'a =ap_signin_notification_condition_of_use')]")

# Need help link, search by Xpath. tag and attribute
driver.find_element(By.XPATH,"//span[@class='a-expander-promt']")

# Forgot your password, search By xpath, contains:
driver.find_element(By.XPATH,"//a[contains(@href,'https://www.amazon.com/ap/forgot password')]")

# Other issues with Sign-In, search my ID
driver.find_element(By.ID, "ap-other-signin-issues-link").click()

# condition of use link, search by xpath, contains:
driver.find_element(By.XPATH,"//a[contains(@ref, 'ap_ desktop_ footer_ cou')]")

# Create your Amazon account button, search by ID:

driver.find_element(By.ID,"createAccountSubit").send_keys()

# Privacy Notice link, search by xpath
driver.find_element(By.XPATH, "//html[@ref='ap_desktop_footer_privacy_notice']")







