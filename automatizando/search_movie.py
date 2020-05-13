from selenium.webdriver import Firefox
import time

browser = Firefox()
url = 'https://www.netflix.com/browse'
browser.get(url)

id = browser.find_element_by_name('userLoginId')
id.send_keys('d5fdasilva@gmail.com')
time.sleep(1)
password = browser.find_element_by_name('password')
password.send_keys('danield5')
password.submit()
time.sleep(2)
#person = browser.find_element_by_xpath("//div[@class='profile-name']").click()
person = browser.find_element_by_class_name("avatar-wrapper").find_element_by_class_name('profile-name').click()
#login = browser.find_element_by_class_name('btn login-button btn-submit btn-small').click()
#browser.close()
