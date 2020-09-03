# 정규식
import re # 정규식 라이브러리

# ca?e
# care, cafe, case, cave, ...
p = re.compile("ca.e") 
# . : 하나의 문자를 의미함 > cafe, care, cave (o) | caffe(x)
# ^(^de) : 문자열 시작 > desk, destination (o) | fade(x)
# $($se) : 문자열의 끝 > case, base (o) | face(x)

def print_match(m):
    if m:
        print("m.group() :",m.group()) # 매치되지 않으면 에러가 발생, 일치하는 문자열 반환
        print("m.string :", m.string) # 입력받은 문자열
        print("m.start() : ", m.start()) # 일치하는 문자열의 시작 인덱스 
        print("m.end() :", m.end()) # 일치하는 문자열의 끝 인덱스
        print("m.span() :", m.span()) # 일치하는 문자열의 시작과 끝 인덱스
    else:
        print("Not match")

# m = p.match("good care")
# print_match(m)

#m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인

# lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(lst)
