import requests
from bs4 import BeautifulSoup

# 테스트로 가져올 URL 설정 (간단히 예시 사이트 사용)
url = "https://www.naver.com"

# GET 요청으로 웹 페이지 가져오기
response = requests.get(url)

# 응답 결과를 HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 사이트의 <title> 태그 가져오기
print("Title 태그 내용:", soup.title.string)
