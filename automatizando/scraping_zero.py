from selenium.webdriver import Firefox
import time

browser = Firefox()
url = ' https://translate.google.com'
browser.get(url)


def translate(text):
    textt = text
    set_language = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]').click()
    time.sleep(2)
    chose_language = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[2]/div/div[3]/div[75]/div[2]').click()
    set_text = browser.find_element_by_tag_name('textarea')
    set_text.clear()
    set_text.send_keys(text)
    assert "No results found." not in browser.page_source
    time.sleep(2)
    ##browser.close()

i = 0
while i < 3:
    print('####################')
    user = input(f'Type to Translate: ')
    translate(user)
    i+=1
