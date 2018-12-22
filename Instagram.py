from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

usernameStr = 'nisha140293415kumari'
passwordStr = 'intime@lpu'
emailStr = 'nisha140293415kumari@gmail.com'
fnameStr = 'Nisha Kumari'
browser = webdriver.Chrome('C:/Users/Nishant/Downloads/chromedriver_win32/chromedriver.exe')
browser.get(('https://www.instagram.com/accounts/emailsignup/?hl=en'))

# fill in username and hit the next button
email = browser.find_elements_by_css_selector('form input')[0]
fname= browser.find_elements_by_css_selector('form input')[1]
username=browser.find_elements_by_css_selector('form input')[2]
password=browser.find_elements_by_css_selector('form input')[3]

#username = browser.find_element_by_id('/*[.*]/*')
email.send_keys(emailStr)
time.sleep(5)
fname.send_keys(fnameStr)
time.sleep(5)
username.send_keys(usernameStr)
time.sleep(5)
password.send_keys(passwordStr)

browser.find_elements_by_css_selector('form input')[3].submit()
#nextButton = browser.find_element_by_id('f7f203604cd934')
#nextButton.click()

# wait for transition then continue to fill items

#password = WebDriverWait(browser, 10).until(
#    EC.presence_of_element_located((By.NAME, "password")))

#password.send_keys(passwordStr)

#signUpButton = browser.find_elements_by_css_selector("button[@type = 'submit']")
#signUpButton.click()
