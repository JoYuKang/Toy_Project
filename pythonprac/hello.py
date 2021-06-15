import requests
from bs4 import BeautifulSoup
#기본 코드
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)
                        # 가져올 사이트 url
soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
print(soup)
