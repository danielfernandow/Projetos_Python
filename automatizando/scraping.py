from selenium import webdriver
from selenium.webdriver import Firefox
import pandas as pd
import time

path = '/Downloads/chromedriver_linux64(1)/webdriver'

browser = Firefox()
pages = 3
url = 'http://books.toscrape.com/catalogue/page-1.html'

def getdata(start_url, pgs):
    current = 0
    urls = browser.get(start_url)
    data = {}
    df = pd.DataFrame(columns =['Title', 'Price', 'Stock', 'Star'])
    dictionary = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    while current < pages:
        books = browser.find_elements_by_css_selector('ol.row')
        for book in books:
            for b in book.find_elements_by_css_selector('article.product_pod'):
                data['Title'] = b.find_elements_by_css_selector('img')[0].get_attribute('alt')
                data['Price'] = b.find_elements_by_css_selector('div.product_price p.price_color')[0].text
                data['Stock'] = b.find_elements_by_css_selector('div.product_price p.instock.availability')[0].text
                data['Star'] = b.find_elements_by_css_selector('p')[0].get_attribute('class').split()[-1]
                data['Star'] = [v for k, v in dictionary.items() if k in data['Star']][0]
                df = df.append(data, ignore_index = True)
            current+=1
        next = browser.find_elements_by_css_selector('li.next a')[0].click()
    return df

getdata(url, pages).to_excel('/projeto_python/automatizando/test.xlsx')
