# 11-6 pip install

# pip로 패키지 설치하는 방법

# 파이썬은 모든 구문을 작성하는 것 이상으로 이미 잘 작성된 패키지를 가져와서 사용하는 것이 중요함

# 구글에서 'pypi' 검색 / 접속 -> beautifulsoup4 검색 -> copy -> Visual Studio Code의 Terminal에 paste

# beautifulsoup : 파이썬으로 웹을 크롤링 하기 위한 필수 라이브러리 중 하나

# beautifulsoup 설치 불가 -> pip 버전 업데이트 (코드 : pip install --upgrade beautifulsoup4) -> 재설치
# (업그레이드 삭제 코드 : pip uninstall beautifulsoup4)

# 코드 예제 복붙
from bs4 import BeautifulSoup                                       # bs4 : beautifulsoup4 이름
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())



# pip list 확인 방법 : terminal 입력창에 pip list 입력 후 엔터

# beautifulsoup4 정보 확인 방법 : pip show beautifulsoup4