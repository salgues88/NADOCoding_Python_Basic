# 9-1 클래스 (좀 어렵지만 파이썬 코딩에서 절대 빼놓을 수 없는 매우 중요한 개념 (붕어빵 틀 로 비유), 스타크래프트 예시로 설명)



# 클래스 : 함수 + 변수 모아놓은 것

# 오브젝트 : 클래스를 이용해서 만들어낸 것 (= 인스턴스)

# 클래스 == 빵틀

# 오브젝트 == (빵틀을 이용해서 찍어낸) 빵



# [테크보이 워니 설명] (클래스 ~ 메소드 까지 한번에 설명함) https://www.youtube.com/watch?v=M6kQTpIqpLs&ab_channel=TeccboiWonie


# class Person:
#     name = "워니"

#     def say_hello(self):
#         print("안녕! 나는 " + self.name)

# wonie = Person()
# michael = Person()
# jenny = Person()


# wonie.say_hello()
# michael.say_hello()
# jenny.say_hello()

# 위 케이스의 경우 name을 "워니"로 고정시켜서 name값이 변하지 않음 -> __init__ 사용 필요


class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("안녕! 나는 " + self.name)

wonie = Person("워니")
michael = Person("마이클")
jenny = Person("제니")

wonie.say_hello()
michael.say_hello()
jenny.say_hello()


print("\n")


# class 내부 함수에 인자를 추가했을 경우

class Person:
    def __init__(self, name, age):                         # class 내부 전체에서 공용으로 사용되는 인자 
        self.name = name                                   # class 공용인자를 매개변수로 변환
        self.age = age

    def say_hello(self, to_name):                          # class 내부 함수에서 별도로 설정한 인자 (to_name)
        print("안녕! " + to_name + "야 나는 " + self.name)  # class 공용 인자는 'self.이름' 형태로 적음
                                                           # class 내부 함수 설정 인자는 '이름' 형태로 적음

    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + "살이야")

wonie = Person("워니", 13)                                 # class 공용 인자(name, age) 값 설정
michael = Person("마이클", 16)                             # 16은 정수(int)여서 문자(str)로 변환해야 함 
jenny = Person("제니", 18)


wonie.say_hello("철수")                                    # class 내부 함수에서 to_name 인자 설정 (여기선 철수)
michael.say_hello("영희")
jenny.say_hello("둘리") 

wonie.introduce()


print("\n")




# [나도코딩 설명] https://www.youtube.com/watch?v=kWiCuklohdY&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9

# (클래스 없이) 스타크래프트 유닛 정의, 움직임
print("[(클래스 없이) 스타크래프트 유닛 정의, 움직임")

# 마린 : 공격 유닛, 군인, 총
name = "마린"                                       # 유닛 이름
hp = 40                                             # 유닛 체력
damage = 5                                          # 유닛 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))


# 탱크 : 공격 유닛, 탱크, 포, 일반모드 / 시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage= 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))


tank2_name = "탱크2"
tank2_hp = 150
tank2_damage= 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))


def attack(name, location, damage):
    print("{0} : {1}시 방향으로 적군을 공격합니다. [데미지 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "3시", tank_damage)
attack(tank2_name, "3시", tank2_damage)

# 동일 유닛이 수십, 수백개가 되면 기존 코딩 방식으로 적기에는 불가능 -> 이럴 때 클래스 기능을 사용!


print("\n")



# (클래스를 사용하여) 여러 개의 스타크래프트 유닛 정의, 움직임
print("\n\n[(클래스를 사용하여) 스타크래프트 유닛 정의, 움직임]")

# 클래스 관련 자세한 내용은 다음장에서 다룰 예정 (지금은 위 코딩을 클래스로 바꾸면 어떻게 되는지에 집중!!)


class Unit:                                                             # class 뒤 변수 첫글자는 대문자 (확인필요)
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 데미지 : {1}".format(self.hp, self.damage))

Marine1 = Unit("마린", str(40), str(5))                                 # 클래스로부터 만들어지는 것을 "객체"라고 함
Marine2 = Unit("마린", "40", "5")
Tank1 = Unit("탱크", 150, 35)                                   