# 9-6 다중상속 : 하나의 부모 변수로부터 물려받는게 아니라 다양한 곳에서 물려 받을 때 사용

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


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




# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송, 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):   
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다 [속도 {2}]".format(name, location, self.flying_speed))


# 공중 공격 유닛 클래스

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)             # AttackUnit의 변수 가져옴
        Flyable.__init__(self, flying_speed)                    # Flyable의 변수 가져옴


# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")                              # fly함수의 class인 Flyable은 name 변수가 없어서 별도로 추가함

