# 표준 입출력
''' print("Python", "Java", sep=",", end="\t")
print("hi") '''

''' import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr) '''

# 시험 성적
''' scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # key, value
    #print(subject, score)
    print(subject.ljust(4), str(score).rjust(4), sep=": ") # ljust(8) : 8개 공간을 만들고 왼쪽 정렬 / rjust : 오른쪽 정렬 (문자열만 가능함) '''
''' 
# 은행 대기순번표 : 001, 002, ...
for num in range(1, 21):
    print("대기번호 : "+ str(num).zfill(3)) # zfill(3) : 3만큼 공간을 확보하고, 빈공간에 대해 0으로 채워라 '''

''' answer = input("아무 값이나 입력하세요 : ") #input으로 입력받으면 숫자를 입력해도 항상 문자열 형태로 저장된다.
print("입력하신 값은 " + answer + "입니다.") '''

''' # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 때는 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))
# 3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000))
print("{0:+,}".format(100000000))
print("{0:+,}".format(-100000000))
# 소수점 표시
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3)) '''

# 파일 입출력
''' score_file = open("score.txt", "w", encoding="utf8") #utf8 is for Korean
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() '''

# "a" mode is append
''' score_file = open("score.txt", "a", encoding="utf8") #utf8 is for Korean
score_file.write("과학 : 80\n") # file.write는 자동 줄바꿈 안됨.
score_file.write("코딩 : 100")
score_file.close() '''

# "r" mode is read
''' score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close() '''

''' score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close() '''

''' score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close() '''

''' score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
print(lines)
for line in lines:
    print(line, end="")
score_file.close() '''

import pickle
''' profile_file = open("profile.pickle", "wb") # pickle을 위해 binary mode 필요함
profile = {"이름":"박명수", "나이":30, "취미":["축구","골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close() '''

''' profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close() '''

''' with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file)) '''

with open("study.txt","w", encoding="utf8") as study_file:
    study_file.write("파이썬 열심히 공부중")  
