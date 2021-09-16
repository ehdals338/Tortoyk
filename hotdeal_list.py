import requests
from bs4 import BeautifulSoup

#FM KOREA Hot Deal
url = "https://www.fmkorea.com/hotdeal"
#html 소스 가져오기
res = requests.get(url)

#html parsing
soup = BeautifulSoup(res.text, 'lxml')

#review list
ul = soup.find('div', "fm_best_widget _bd_pc")
lis = ul.find_all('h3')

#review title print
count = 0
for li in lis:
    count += 1
    print(f"[{count}th] ", li.a.string)

#추후에 가격까지 갖고오는걸로.....