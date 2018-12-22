from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

usernameStr = 'nishant.pal3'
passwordStr = 'intime#lpu'

browser = webdriver.Chrome('C:/Users/Nishant/Downloads/chromedriver_win32/chromedriver.exe')
browser.get(('https://www.instagram.com/accounts/login/?source=auth_switcher'))
username = browser.find_elements_by_css_selector('form input')[0]

#username=browser.find_element_by_id('f38e5f1237a115')
username.send_keys(usernameStr)
time.sleep(5)
# wait for transition then continue to fill items

password =browser.find_elements_by_css_selector('form input')[1]

password.send_keys(passwordStr)
time.sleep(5)
browser.find_elements_by_css_selector('form input')[1].submit()

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()

browser.get(('https://www.instagram.com/lalitgarg9191/'))
time.sleep(5)

follow = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/button')
ActionChains(browser).move_to_element(follow).click().perform()

