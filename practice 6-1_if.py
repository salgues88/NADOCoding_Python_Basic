# if (분기)

# [나도코딩 설명] https://www.youtube.com/watch?v=kWiCuklohdY&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9

#if 조건:
#   실행명령문

weather = "비"

if weather == "비":
    print("우산을 챙기세요")                    # 조건과 변수가 같으면 실행명령문이 출력됨

if weather == "맑음":
    print("우산을 챙기세요")                  # 조건과 변수가 다르면 실행명령문이 출력 안됨

##################################################################################################################

weather2 = "미세먼지"

if weather2 == "비":
    print("우산을 챙기세요")

elif weather2 == "미세먼지":
    print("마스크를 챙기세요")                  # 조건이 if에 해당 안되고 elif에 해당되므로 elif 실행명령문이 출력됨

else:
    print("준비물 필요 없어요")

##################################################################################################################

weather3 = "맑아요"

if weather3 == "비":
    print("우산을 챙기세요")

elif weather3 == "미세먼지":
    print("마스크를 챙기세요")

else:
    print("준비물 필요 없어요")                 # 조건이 if, elif 둘 다 해당 안되므로 else 실행명령문이 출력됨

##################################################################################################################

# weather4 = input("오늘 날씨는 어때요? ")        # input 내부에 문자열 넣고 출력하면 ~어때요? 뒤에 커서가 뜸 
                                               #  -> 해당 커서에 비 or 미세먼지 등을 입력하면 해당되는 실행명령문이 출력됨

# if weather3 == "비":
#     print("우산을 챙기세요")

# elif weather3 == "미세먼지":
#     print("마스크를 챙기세요")

# else:
#     print("준비물 필요 없어요")

##################################################################################################################

temp = int(input("오늘 기온 어때요? "))          # temp는 정수값이라 정수형으로 만들어주는 int()로 감싸줌

if 30 <= temp:
    print("너무 더워요")

elif 10 <= temp and temp < 30:
    print("날씨가 괜찮아요")

else:
    print("너무 추워요")

########################################################



# if와 else를 이용하여 가위바위보 게임 만들기
# (else, if가 구분되었을 때와, elif로 썼을 때의 간편함 비교)

scissors = "가위"
rock = "바위"
paper = "보"

win = "이겼다!!!"
draw = "비겼네"
lose = "졌어..."



mine = "보"
yours = "바위"


# 가위 바위 보 코딩1 -> if, else로만 구현하니 헷깔림 -> else와 if를 합친 elif를 사용하면 더 깔끔해짐
if mine == yours:
    result = draw

else:
    if mine == scissors:
        if yours == rock:
            result = lose
        else:
            result = win

    else:
        if mine == rock:
            if yours == paper:
                result = lose
            else:
                result = win

        else:
            if mine == paper:
                if yours == scissors:
                    result = lose
                else:
                    result = win

            else:
                print("이상해요")

print(result)


# 가위 바위 보 코딩2 (elif 사용)
if mine == yours:
    result = draw

else:                                               # 이 부분은 코드를 읽는 사람의 이해를 돕기 위해 일부로 합치지 않고 남겨둠
    if mine == scissors:
        if yours == rock:
            result = lose
        else:
            result = win

    elif mine == rock:
        if yours == paper:
            result = lose
        else:
            result = win

    elif mine == paper:
        if yours == scissors:
            result = lose
        else:
            result = win

    else:
        print("이상해요")

print(result)



# 가위 바위 보 코딩3 (최대한 elif 사용)
if mine == yours:
    result = draw

elif mine == scissors:
    if yours == rock:
        result = lose
    else:
        result = win

elif mine == rock:
    if yours == paper:
        result = lose
    else:
        result = win

elif mine == paper:
    if yours == scissors:
        result = lose
    else:
        result = win

else:
    print("이상해요")

print(result)