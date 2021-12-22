# 4-1 문자열

# [나도코딩 설명] https://www.youtube.com/watch?v=kWiCuklohdY&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9

sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)
                                # """ : 줄바꿈 표시

sentence3 = """                  
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)


print("\n")



##############################################




# 4-2 슬라이싱 (시작값이 0 또는 1이므로 헷깔릴 수 있음!!!)

jumin = "881122-3456789"

print("성별 : " + jumin[7])                                         # [] : 문자열에서 x번째 정보를 가져오는 기능 (1부터 시작)
print("연 : " + jumin[0:2])                                         # [0:2] : 0 ~ 2 직전 까지 (0, 1) (0부터 시작) 
print("월 : " + jumin[2:4])                                         # [2:4] : 2 ~ 4 직전 까지 (2, 3) (0부터 시작)
print("일 : " + jumin[4:6])
print()

print("생년월일 : " + jumin[:6])                                    # [:6] : 처음부터 ~ 6 직전 까지 (0, 5) (= [0:6])
print("뒤 7자리 : " + jumin[7:])                                    # [7:] : 7 ~ 마지막 까지   (7, 마지막) (= [7:13])
print()

print("뒤 7자리 중 맨 뒤 첫번째 제외하고 표시 :", jumin[7:-1])           # [7:-1] : 7 ~ 마지막-1 자리 까지 (=[7:13])
print(jumin[7:13])
print("뒤 7자리 중 맨 뒤 두번째 제외하고 표시 :", jumin[7:-2])           # [7:-1] : 7 ~ 마지막-1 자리 까지 (=[7:12])
print(jumin[7:12])
print()

print("뒤 7자리 (뒤에부터) : " + jumin[-7:])                        # [-7:] : 맨 뒤 7번째부터 끝까지 (-1부터 시작?)
print()

print(jumin[7]) 