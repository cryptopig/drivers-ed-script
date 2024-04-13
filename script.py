from splinter import Browser
from time import sleep
browser = Browser('chrome')
browser.visit('https://jumpstart.courseinstruction.com/course/content/page/userfront_login')
print('connected to google.com')

EMAIL = 'vedant.g273@gmail.com'
PASSWORD = 'Vedu!1234'

browser.find_by_id('email').click()
browser.type('email', EMAIL)
browser.find_by_id('password')
browser.type('password', PASSWORD)

browser.find_by_css('button medium green sign-in').click()

sleep(5)

browser.quit()