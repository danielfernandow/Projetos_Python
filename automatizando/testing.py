from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
url = 'file:///media/d5/HD/Faculdade/1%20S/DAW/APS/la%20recette%20cafe/index.html'
e = 'contato.html'
sleep(1)

browser.get(url)
browser.find_element_by_tag_name(e)


#"""browser.quit()"""
