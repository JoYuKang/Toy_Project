import requests
from bs4 import BeautifulSoup


from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 기본 코드
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)
# 가져올 사이트 url
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')

# for tr in trs:
#     a_tag = tr.select_one('td.title > div > a')
#     a_rank = tr.select_one('td:nth-child(1) > img')
#     star = tr.select_one('td.point')
#     if a_tag is not None:
#         title = a_tag.text
#         rank = a_rank['alt']
#         star = star.text
#         doc = {
#             'rank': rank,
#             'title': title,
#             'star': star
#         }
#         db.movies.insert_one(doc)
user = db.movies.find_one({'title': '매트릭스'})
print(user['star'])
same_star = list(db.movies.find({'star':'9.39'},{'_id':False})) #깔끔한 출력
for i in same_star:
    print(i['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})