# 9-5 상속


# [테크보이 워니 설명] https://www.youtube.com/watch?v=M6kQTpIqpLs&ab_channel=TeccboiWonie

class Person:
    def __init__(self, name, age):                         # class 내부 전체에서 공용으로 사용되는 인자 
        self.name = name                                   # class 공용인자를 매개변수로 변환
        self.age = age

    def say_hello(self, to_name):                          # class 내부 함수에서 별도로 설정한 인자 (to_name)
        print("안녕! " + to_name + "야 나는 " + self.name)  # class 공용 인자는 'self.이름' 형태로 적음
                                                           # class 내부 함수 설정 인자는 '이름' 형태로 적음

    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + "살이야")



# 새로 경찰이라는 class와 프로그래머라는 class를 만들고 싶음
# 그런데 경찰, 프로그래머는 기존 Person이 할 수 있는건 다 할 수 있어야함 -> 상속 기능 사용

class Police(Person):                                      # Person을 상속받기 위해 Police 뒤에 (Person) 추가
    def arrest(self, to_arrest):
        print("넌 체포됐다. " + to_arrest)



# 상속을 안받고 Police 내에 Person 함수들 까지 사용하려면 아래와 같이 표현해야 함
# -> 코드가 길어짐!!! -> 상속 사용 시 위 Person 내 함수들을 (Person)으로 간소화 가능

# class Police:                                     
#     def __init__(self, name, age):                        
#         self.name = name                                  
#         self.age = age
#     def say_hello(self, to_name):                          
#         print("안녕! " + to_name + "야 나는 " + self.name)  
#     def introduce(self):
#         print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + "살이야")
#     def arrest(self, to_arrest):
#         print("넌 체포됐다. " + to_arrest)



class Programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들어야 겠다: " + to_program)


wonie = Person("워니", 20)
jenny = Police("경찰", 18)
michael = Programmer("프로그래머", 30)

# wonie.arrest("michael")                                  # 워니는 Person 클래스 -> Police 상속 X -> arrest 함수 사용 X

jenny.introduce()                                          # 제니는 경찰 클래스 -> introduce 함수 없음 (그러나 상속으로 사용 가능)
jenny.arrest("워니")
# jenny.program("교통정보앱")                               # 제니는 경찰 클래스, 퍼슨 클래스 상속 받음
#                                                            그러나 프로그래머 클래스는 상속 X -> program 함수 사용 X

michael.introduce()
michael.program("나만의 앱")


print("\n")




# [나도코딩 설명] https://www.youtube.com/watch?v=kWiCuklohdY&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 메딕 : 의무병 (공격기능 X -> damage 삭제)


# 공격 유닛                                                      # 공격유닛에서 일반 유닛과 겹치는 부분 존재 -> 상속 사용
class AttackUnit(Unit):                                         # class 자식변수 뒤에 '(부모변수)' 입력
    def __init__(self, name, hp, damage):                       
        Unit.__init__(self, name, hp)                           # 일반 유닛의 변수 사용을 위해 Unit._init__(self, name, hp) 입력
        self.damage = damage

    def attack(self, location):                                         
        print("{0} : {1}시 방향으로 적군을 공격합니다. [공격력  {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 받았습니다".format(self.name, damage))  # damage는 방금 정의해서 self 없이 사용
        
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 사망했습니다".format(self.name))


# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)

# 파이어뱃이 공격함
firebat1.attack(5)                                                      # def attack 함수를 사용하여 결과값 출력 (5시 방향)

# 파이어뱃이 공격 2번 받음
firebat1.damaged(25)                                                    # def damaged 함수를 사용하여 결과값 출력
firebat1.damaged(25)                                                    # (적에게 25 데미지로 2번 공격 받음)