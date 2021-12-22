# 9-8 pass : 아무것도 안하고 통과시킴

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):                        # speed 추가
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):                                   # move 메소드 추가
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


# 공격 유닛                                                      # 공격유닛에서 일반 유닛과 겹치는 부분 존재 -> 상속 사용
# class AttackUnit(Unit):                                         # class 자식변수 뒤에 '(부모변수)' 입력
#     def __init__(self, name, hp, speed, damage):                       
#         Unit.__init__(self, name, hp, speed)                           # 일반 유닛의 변수 사용을 위해 Unit._init__(self, name, hp) 입력
#         self.damage = damage

#     def attack(self, location):                                         
#         print("{0} : {1}시 방향으로 적군을 공격합니다. [공격력  {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 받았습니다".format(self.name, damage))  # damage는 방금 정의해서 self 없이 사용
        
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 사망했습니다".format(self.name))




# # 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송, 공격 X

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):   
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다 [속도 {2}] ".format(name, location, self.flying_speed))


# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)          # 날라가기 때문에 지상 speed = 0
#         Flyable.__init__(self, flying_speed)                    # Flyable의 변수 가져옴

#     def move(self, location):                                   # move, fly 구분없이 사용하기 위해 move 재정의
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)                           # name은 위에서 빌려서 self.name, location은 위에 있어서 그대로 location





# 건물 
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass                                                    # pass : 일단은 아무것도 안하고 그냥 넘어간다는 뜻  
                                                                #        (적다가 말아도 완성된 것처럼 인식)


# 서플라이 디폿 : 건물, 건물 1개마다 8개의 유닛 생성
supply_depot =  BuildingUnit("서플라이 디폿", 500, "7시")





def game_start():
    print("[알림] 새로운 게임을 시작합니다")

def game_over():
    pass


game_start()
game_over()