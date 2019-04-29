import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def data_get(tarih, sehir):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver_path = r'/usr/bin/chromedriver'
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)

    browser.get('https://portal.tnb.org.tr/Sayfalar/NobetciNoterBul.aspx')
    time.sleep(5)
    tarih_ = browser.find_element_by_name('ctl00$ctl48$g_dfd472f4_0bcb_41d8_8b8b_adbe9855f370$ctl00$txtTarih')
    sehir_ = browser.find_element_by_name('ctl00$ctl48$g_dfd472f4_0bcb_41d8_8b8b_adbe9855f370$ctl00$ddlSehirler')
    btn_ara = browser.find_element_by_name('ctl00$ctl48$g_dfd472f4_0bcb_41d8_8b8b_adbe9855f370$ctl00$btnAra')

    tarih_.send_keys(tarih)
    sehir_.send_keys(sehir)

    btn_ara.click()
    time.sleep(5)
    content = browser.page_source
    browser.close()
    return content


def data_split(data):
    liste = []
    soup = bs(data, 'html.parser')
    tables = soup.find_all('table', attrs={'class': 'table'})
    for table in tables:
        data = table.find_all('td')
        for d in data:
            liste.append(d.text)
            print(d.text)
    return liste