import requests
#res = requests.get("http://naver.com")
res = requests.get("http://google.com")
res.raise_for_status() # 문제가 생기면 오류를 보여주고 프로그램을 종료시킴

print(len(res.text))
print(res.text)
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)