from selenium.webdriver import Chrome
import time

print('Which movie to watch??')
text_filme = input('Type here: ')

browser = Chrome()
url = 'https://www.netflix.com/browse'
browser.get(url)

id = browser.find_element_by_name('userLoginId')
id.send_keys('userlogin')
time.sleep(1)
password = browser.find_element_by_name('password')
password.send_keys('password')
password.submit()
time.sleep(3)
person = browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/span')
#person = browser.find_element_by_class_name("profile-icon")
person.click()
search_bar = browser.find_element_by_class_name('searchTab')
search_bar.click()
type_search = browser.find_element_by_name('searchInput')
type_search.send_keys(text_filme)
time.sleep(3)
click_movie = browser.find_element_by_id('title-card-0-0')
click_movie.click()

play_video = browser.find_element_by_class_name('ltr-18i00qw')
play_video.click()
#browser.close()
