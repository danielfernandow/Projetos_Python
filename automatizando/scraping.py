from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
url = 'file:///media/d5/HD/Faculdade/1%20S/DAW/APS/la%20recette%20cafe/index.html'
#e = 'contato.html'
sleep(1)
browser.find_element_by_link_text('Contato').click()

browser.get(url)
browser.find_element_by_tag_name(e)


#"""browser.quit()"""
