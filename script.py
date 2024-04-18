from splinter import Browser

from time import sleep


browser = Browser('chrome')
print('successfully established browser')

browser.visit('https://jumpstart.courseinstruction.com/course/content/page/userfront_login')
print('opened portal')

EMAIL = 'EMAIL'
PASSWORD = 'PASSWORD'

browser.find_by_id('email').click()
browser.type('email', EMAIL)
browser.find_by_id('password')
browser.type('password', PASSWORD)

browser.find_by_css('a[class="button medium green sign-in"]').click()
sleep(1)

# navigate to actual lesson, start loop from here

browser.visit('https://jumpstart.courseinstruction.com/course/content/page/course_home')

browser.find_by_id('navlink_outline').click()
sleep(1)


# while True:
browser.find_by_css('a[href="javascript:if(true){GoTo(\'8\');}"').click()
sleep(1)

browser.find_by_css('a[href="javascript:if(true){GoTo(\'8.1\');}"').click()
sleep(1)

sleep(5)
browser.quit()