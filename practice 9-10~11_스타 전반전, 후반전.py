# 9-10~11 스타크래프트 전반전, 후반전


from random import *                                                    # 피격 데미지를 랜덤으로 표시 -> 랜덤 함수 불러옴

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):                        
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):        
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):                                          # 일반 유닛도 공격받을 수 있어서 Unit으로 이동
        print("{0} : {1} 데미지를 받았습니다".format(self.name, damage))  # damage는 방금 정의해서 self 없이 사용
        
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 사망했습니다".format(self.name))


# 공격 유닛                                                      # 공격유닛에서 일반 유닛과 겹치는 부분 존재 -> 상속 사용
class AttackUnit(Unit):                                         # class 자식변수 뒤에 '(부모변수)' 입력
    def __init__(self, name, hp, speed, damage):                       
        Unit.__init__(self, name, hp, speed)                           # 일반 유닛의 변수 사용을 위해 Unit._init__(self, name, hp) 입력
        self.damage = damage

    def attack(self, location):                                         
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력  {2}]"\
            .format(self.name, location, self.damage))






# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
        
    
    # 마린은 스팀팩 기능이 있음, 일정 시간 이동 및 공격 속도 증가, 체력 10 감소
    def steampack(self):
        if self.hp >= 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))



# 탱크
class Tank(AttackUnit):
    seize_developed = False                                     # 시즈모드 개발 여부 : 안되어 있음

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False                            # 시즈 모드 선언
        

    def set_seize_mode(self):
        if Tank.seize_developed == False:                       # 시즈모드가 개발 안됬을 때는 아무것도 안하고 리턴
            return
        
        # 현재 시즈모드가 아닐 떄 -> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


    
    



    




# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송, 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):   
        self.flying_speed = flying_speed

    def fly(self, name, location):   
        print("{0} : {1} 방향으로 날아갑니다 [속도 {2}] ".format(name, location, self.flying_speed))


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):                   # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)          # 날라가기 때문에 지상 speed = 0
        Flyable.__init__(self, flying_speed)                    # Flyable의 변수 가져옴

    def move(self, location):                                   # move, fly 구분없이 사용하기 위해 move 재정의
        self.fly(self.name, location)                           # name은 위에서 빌려서 self.name, location은 위에 있어서 그대로 location


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__( self, "레이쓰", 80, 20, 5)
        self.clocked = False                                    # 클로킹 해제 상태

    def clocking(self):
        if self.clocked == True:                                # 클로킹 상태 -> 해제
            print("{0} : 클로킹 모드를 해제합니다".format(self.name))
            self.clocked = False 
        else:                                                   
            print("{0} : 클로킹 모드를 설정합니다".format(self.name))
            self.clocked = True



def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : GG")
    print("[Player] 님이 게임에서 퇴장하였습니다.")





# 실제 게임 시작
game_start()


# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()


# 탱크 2기 생성
t1 = Tank()
t2 = Tank()


# 레이스 1기 생성
w1 = Wraith()



# 유닛 일괄 관리 (생성된 모든 유닛을 append 처리)                  
attack_units = []                                               # 공격 유닛 변수 생성 
attack_units.append(m1)                                         #   및 모든 유닛을 리스트에 집어넣고 일괄적으로 컨트롤
attack_units.append(m2)
attack_units.append(m3)                                         # 변수.append("문자열") : 리스트 맨 뒤에 문자열 추가
attack_units.append(t1)                                         # 마린, 탱크, 레이쓰라는 서로 다른 class의 변수 입력
attack_units.append(t2)
attack_units.append(w1)


# 전군 이동
for unit in attack_units:
    unit.move('1시')

# 탱크 시즈모드 개발
Tank.seize_developed = True                                    # 시즈 모드 개발됨 -> True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")


# 공격 준비 모드 (마린 : 스팀팩, 탱크 : 시즈 모드, 레이쓰 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):                                # isinstance : 인스턴스가 해당 클래스의 자료가 맞는지 확인
        unit.steampack()                                        # Marine이면 스팀팩을 써라
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()


# 전군 공격
for unit in attack_units:
    unit.attack("1시")


# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20))                                # 랜덤 피격 데미지 (데미지 범위 : 5이상 ~20 미만)


# 게임 종료
game_over()