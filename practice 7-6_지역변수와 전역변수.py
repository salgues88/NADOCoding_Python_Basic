# 지역변수 : 함수 내에서만 사용 가능한 것
# 전역변수 : 모든 프로그램 내에서 사용 가능


print("[지역변수 예시]")

gun = 10

def checkpoint(soldiers):                           # 경계 근무
    gun = 20
    gun = gun -soldiers                             # gun = gun - soldiers에서 가운데 gun이 지역 변수 -> 함수 내부에 gun 값이 존재해야함
    print("'함수 내' 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)                                       # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))



print("\n[전역변수 예시]")

gun = 10

def checkpoint(soldiers):                           
    global gun                                      # global 변수명 : 전역 공간에 있는 변수 gun을 함수로 들고옴
    gun = gun -soldiers                             
    print("'함수 내' 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)                                       
print("남은 총 : {0}".format(gun))                  



# 전역변수를 사용하면 프로그램 속도가 느려지고 전체 부하 증가 -> 반환 방법 추천

print("\n[Return 함수를 이용한 예시]")

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("'함수 내' 남은 총 : {0}".format(gun))
    return gun                                      # 함수에서 계산된 gun 값을 외부로 내보내는 기능

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)                        # 위 함수에서 계산되어서 반환된 값을 받음
print("남은 총 : {0}".format(gun))






# Quiz6. 표준 체중을 구하는 프로그램을 만드시오

print("\n[Quiz6]")

# 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         *함수명 : std_weight
#         *전달값 : 키(height), 성별(gender)

# 조건2 : 표준 체중은 소수점 둘째자리 까지 표시

# (출력 예시)
# 키 175cm 남자의 표준 체중은 67.38kg 이다








# 해답1 (나도코딩)

def std_weight(height, gender):                         # 키 : m 단위 (실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175                                            # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)     # m 단위로 변경,     round(값, 2) : 소수점 2쨰자리까지 표시, 반올림

print("키 {0}cm {1}의 표준 체중은 {2} 이다.".format(height, gender, weight))




# 해답2 (나) (풀다가 실패, 조건2는 모르겠음)

# height = 175
# gender = "남자"

# man_std_weight = height * height * 22
# woman_std_weight = height * height * 21

# def std_weight(height, gender):
#     if height >= 170:
#         global man_std_weight
#         return(man_std_weight)
#     elif height < 170:
#         global woman_std_weight
#         return(woman_std_weight)

# std_weight()
# print("키 {0}cm {1}의 표준 체중은 {2} 이다.".format(height, gender, man_std_weight))

    
