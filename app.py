import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.


# select를 이용해서, 팀순위 표를 가져오기

# print(news)

# news (dt들) 의 반복문을 돌리기
for news_url in news:
    # print('######', ranking_info)
    url0 = news_url.select_one('dt > a').text

    print(url0)
