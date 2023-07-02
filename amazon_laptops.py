from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36'}
html_text = requests.get('https://www.amazon.in/HP-3-3250U-Graphics-64Q84PA-ACJ/dp/B09RMQXSZT/ref=sr_1_7?crid=24EN3COVO4NII&keywords=laptops&qid=1662224046&sprefix=laptops%2Caps%2C216&sr=8-7', headers=headers)
soup = BeautifulSoup(html_text.content,'lxml')
table = soup.find('table', id="productDetails_techSpec_section_1")
brand = []
resolution = []
p_speed = []
r_size = []
m_c_speed =[]
hdd_size = []
hdd_desc = []
column = []
for item in table.find_all('tr'):
    detail = item.th.text
    if (detail) == ' Brand ':
        b = item.td.get_text(strip=True)
        brand.append(b)
        column.append(' Brand ')

    if (detail) == ' Resolution ':
        b = item.td.get_text(strip=True)
        resolution.append(b)
        column.append(' Resolution ')

    if (detail) == ' Processor Speed ':
        b = item.td.get_text(strip=True)
        p_speed.append(b)
        column.append(' Processor Speed ')

    if (detail) == ' RAM Size ':
        b = item.td.get_text(strip=True)
        r_size.append(b)
        column.append(' RAM Size ')

    if (detail) == ' Memory Clock Speed ':
        b = item.td.get_text(strip=True)
        m_c_speed.append(b)
        column.append(' Memory Clock Speed ')

    if (detail) == ' Hard Drive Size ':
        b = item.td.get_text(strip=True)
        hdd_size.append(b)
        column.append(' Hard Drive Size ')

    if (detail) == ' Hard Disk Description ':
        b = item.td.get_text(strip=True)
        hdd_desc.append(b)
        column.append(' Hard Disk Description ')

lap = {'Brand':brand,'Resolution': resolution, ' Processor Speed ':p_speed, ' RAM Size ':r_size, ' Memory Clock Speed ':m_c_speed, ' Hard Drive Size ': hdd_size, ' Hard Disk Description ': hdd_desc  }
df = pd.DataFrame(lap)
print(df)




