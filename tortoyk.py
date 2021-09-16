import requests
from bs4 import BeautifulSoup

#New world
url = "https://movie.naver.com/movie/bi/mi/review.naver?code=91031"
#html 소스 가져오기
res = requests.get(url)

#html parsing
soup = BeautifulSoup(res.text, 'lxml')

#review list
ul = soup.find('ul', class_="rvw_list_area")
lis = ul.find_all('li')

#review title print
count = 0
for li in lis:
    count += 1
    print(f"[{count}th] ", li.a.string)
