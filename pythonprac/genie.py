import requests
from bs4 import BeautifulSoup


from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 기본 코드
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N', headers=headers)
# 가져올 사이트 url
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
for tr in trs:
     a_title = tr.select_one('td.info > a.title.ellipsis')
     a_rank = tr.select_one('td.number')
     a_singer = tr.select_one('td.info > a.artist.ellipsis')
     if int(a_rank.text.strip()[0:2]) < 10:
         print(a_rank.text.strip()[0], a_title.text.strip(), a_singer.text.strip())
     else:
         print(a_rank.text.strip()[0:2], a_title.text.strip(), a_singer.text.strip())
