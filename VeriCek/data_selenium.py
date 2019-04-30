import time

from bs4 import BeautifulSoup as bs
from selenium import webdriver
import datetime


def Tarayici():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-logging')
    driver_path = r'/Users/mac16/Desktop/yunusileri/TurkerApi/chromedriver'
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
    return browser


def data_get(tarih, sehir):
    browser = Tarayici()
    browser.get('https://portal.tnb.org.tr/Sayfalar/NobetciNoterBul.aspx')
    # time.sleep(2)
    tarih_ = browser.find_element_by_name('ctl00$ctl48$g_dfd472f4_0bcb_41d8_8b8b_adbe9855f370$ctl00$txtTarih')
    sehir_ = browser.find_element_by_name(
        'ctl00$ctl48$g_dfd472f4_0bcb_41d8_8b8b_adbe9855f370$ctl00$ddlSehirler')
    btn_ara = browser.find_element_by_name('ctl00$ctl48$g_dfd472f4_0bcb_41d8_8b8b_adbe9855f370$ctl00$btnAra')

    tarih_.send_keys(tarih)
    sehir_.send_keys(sehir)

    btn_ara.click()
    time.sleep(2)
    content = browser.page_source
    browser.close()
    return data_split(content)


def data_split(data):
    liste = []
    soup = bs(data, 'html.parser')
    tables = soup.find_all('table', attrs={'class': 'table'})
    for table in tables:
        data = table.find_all('td')
        for i in range(int(len(data) / 6)):
            d = {
                f'Noter {i + 1}': {'Bölge': data[i * 6].text, 'Ad': data[(i * 6) + 1].text,
                                   'Adres': data[(i * 6) + 2].text,
                                   'Telefon': data[(i * 6) + 3].text,
                                   'Tarih': data[(i * 6) + 4].text}
            }
            liste.append(d)
    file = open('Logs.txt', 'a')
    file.write(f'{datetime.datetime.now()}\n')
    for l in liste:
        file.write(f'{l}\n')
    file.close()
    return liste
