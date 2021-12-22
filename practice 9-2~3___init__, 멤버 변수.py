# 9-2 __init__

# __init__ 위치에 들어가는 걸 파이썬에서는 "생성자" 라고 함

# 클래스로부터 만들어지는 것을 "객체(object)"라고 함 (Marine1 등)

# 객체를 생성할 때는 __init__ 에 정의된 argument 개수와 동일하게 표시해야 함 (self 빼고)

# class를 사용할 때는 기존처럼 변수를 미리 지정할 필요가 없음 (class 선언 후 내부 함수에서 변수 지정하면 됨)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name                                                # class에서 전달 받은 값을 매개변수로 변환
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 데미지 : {1}".format(self.hp, self.damage))

Marine1 = Unit("마린", str(40), str(5))                 
Marine2 = Unit("마린", "40", "5")
Tank1 = Unit("탱크", 150, 35)                                   
#Marine3 = Unit("탱크")                      # ~~ missing 2 required positional argument -> argument 2개 빠져서 에러남




#################################################################################################################




# 9-3 멤버 변수

# 위 class 값 내에서 self.변수 로 적은 것이 멤버 변수

# 멤버 변수 : 클래스 내에서 정의된 변수, 해당 변수를 가지고 초기화 등에서 활용 가능




# 스타크래프트 비유 예제

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음) (위에 정의된 class 값을 사용하여 코딩)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
#                                       위에서 정의한 wraith1 뒤에 .argument 값을 붙이면 wraith1에 설정한 값이 표시됨



# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True                         # 원래 없었던 .clocking 변수를 추가로 작성함!

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))

# 파이썬에서는 어떤 객체에 추가로 변수를 외부에서 만들어서 사용 가능!!!
# (대신 class 내부에서 만든 변수가 아니므로, 특정 변수에서만 사용 가능하고, 그 외 변수에서는 사용 불가)