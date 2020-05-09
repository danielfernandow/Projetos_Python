from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()

browser.get("https://translate.google.com")
browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]").click()
browser.find_element(By.NAME, "Portuguese").click()
browser.find_element(By.XPATH, "//*[@id='source']").send_keys('click here')
time.sleep(3)
browser.close()
