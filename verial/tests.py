from django.test import TestCase
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs


def Istek(Tarih, Sehir):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver_path = r'C:/Users/yunus/Documents/TrakyaOturum/chromedriver.exe'
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
    browser.get('https://portal.tnb.org.tr/Sayfalar/NobetciNoterBul.aspx')
    tarih = browser.find_element_by_name('ctl00$ctl48$g_dfd472f4_0bcb_41d8_8b8b_adbe9855f370$ctl00$txtTarih')
    sehir = browser.find_element_by_name('ctl00$ctl48$g_dfd472f4_0bcb_41d8_8b8b_adbe9855f370$ctl00$ddlSehirler')
    AramayaBasla = browser.find_element_by_name('ctl00$ctl48$g_dfd472f4_0bcb_41d8_8b8b_adbe9855f370$ctl00$btnAra')
    tarih.send_keys(Tarih)
    sehir.send_keys(Sehir)
    AramayaBasla.click()
    content = browser.page_source
    browser.close()
    return content


def Data(data):
    liste = []
    soup = bs(data, 'html.parser')
    tables = soup.find_all('table', attrs={'class': 'table'})
    for table in tables:
        data = table.find_all('td')
        for d in data:
            liste.append(d.text)
            print(d.text)
    return liste


content = Istek('04/05/2019', 'ADANA')
data = Data(content)
print(data)
