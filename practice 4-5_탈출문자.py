# 탈출문자 1)   \n : 줄바꿈

print("백문이 불여일견\n백견이 불여일타")


# 탈출문자 2)   \" \" or \' \' : 문장 내 따옴표

# ex. 저는 "나도코딩" 입니다
print("저는 '나도코딩' 입니다")
print("저는 \"나도코딩\" 입니다")


# 탈출문자 3)   \\ : 문장 내에서  \
#print("C:\Users\9\Desktop\PhythonWorkSpace")    # 경로 지정 시 역슬래쉬가 탈출문자로 인식되어 에러 발생
print("C:\\Users\\9\\Desktop\\PhythonWorkSpace") # 경로 역슬래쉬에 역슬래쉬를 추가해서 2개로 만들면 에러 X


# 탈출문자 4)   \r : 커서를 맨 앞으로 이동 후 \r 뒤의 단어가 맨 앞 단어를 대체

print("Red Apple \rPine")
print("Red Whale \rBlue")


# 탈출문자 5)   \b : 백스페이스 역활 (한 글자 삭제)

print("P\bRed Apple")


# 탈출문자 6)   \t : 탭 역활
print("Red\tApple")




# Quiz 3. 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예제. http://naver.com

# 규칙1 : http:// 부분은 제외 -> naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 규칙3 : 남은 글자 중 처음 3자리(nav) + 글자 개수(5) + 글자 내 'e' 개수(1) + "!"(!)로 구성


# 예시 : 생성된 비밀번호 : nav51!





 



address = "http://naver.com"
rule1 = address.replace("http://", "")     #규칙1   rule1 = address[7:] 로 표시해도 동일 효과
print(rule1)

rule2 = rule1[:rule1.index(".")]           #규칙2   rule2 = rule1[:5] 로 표시해도 동일 효과 (0, 1, 2, 3, 4)
# rule2 = rule1[:5]
print(rule2)

rule3 = rule2[:3] + str(len(rule2)) + str(rule2.count("e")) + "!" # len(rule2) : rule2의 글자 개수, str() : 숫자를 문자로 인식


print("{}에서 생성된 비밀번호는 {} 입니다".format(rule2, rule3))    # 문자열 포맷 방법 2로 표시

print(f"{rule2}에서 생성된 비밀번호는 {rule3} 입니다")              # 문자열 포맷 방법 3으로 표시