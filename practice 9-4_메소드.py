# 9-4 메소드 : 클래스 안에서 사용하는 함수

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 데미지 : {1}".format(self.hp, self.damage))

Marine1 = Unit("마린", str(40), str(5))                 
Marine2 = Unit("마린", "40", "5")
Tank1 = Unit("탱크", 150, 35)


# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):                                         # class 내 함수 -> 메소드 (확인 필요)                                 
        print("{0} : {1}시 방향으로 적군을 공격합니다. [공격력  {2}]"\
            .format(self.name, location, self.damage))                  # location은 방금 정의한 거라서 self가 붙지 X

# class에서 __init__ 함수 선언 한 다음에 작성하는 함수는 평소대로 적으면 됨 
# (단, 뒤 함수에서 __init__함수에서 설정한 변수를 사용할 땐 'self.변수'로 적어야 함)

    def damaged(self, damage):
        print("{0} : {1} 데미지를 받았습니다".format(self.name, damage))  # damage는 방금 정의해서 self 없이 사용
        
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 사망했습니다".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)

# 파이어뱃이 공격함
firebat1.attack(5)                                       # def attack 함수를 사용하여 결과값 출력 (5시 방향)

# 파이어뱃이 공격 2번 받음
firebat1.damaged(25)                                     # def damaged 함수를 사용하여 결과값 출력
firebat1.damaged(25)                                     # (적에게 25 데미지로 2번 공격 받음)