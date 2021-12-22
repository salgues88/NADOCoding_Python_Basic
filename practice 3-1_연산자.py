

# [나도코딩 설명] https://www.youtube.com/watch?v=kWiCuklohdY&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9

# terminal font 변경 : File -> Preference -> Setting -> "terminal font" 입력 후 폰트 크기 변경

print(1 + 1) #2
print(2 - 3) #-1
print(5 * 2) #10
print(6 / 3) #2


print(2 ** 3) # 2^3 = 8   (** = ^)
print(5 % 3) # 2          (나누기 후 몫이 아닌 나머지 값)
print(10 % 3) #1
print(5 // 3) #1          (나누기 후 몫)
print(10 // 3) #3


print(10 > 3) #True
print(4 >= 7) #False
print(10 > 3) #True
print(5 <= 5) #True     (=< 이렇게는 인식 안됨!!!)


print(3 == 3) # True    ('==' : 앞과 뒤의 값이 똑같다 라는 뜻)
print(4 == 2) # False
print(3+4 == 7) # True


print(1 != 3) #True     (!= : 앞과 뒤가 같지 않음)
print(not(1 != 3)) #False


print((3 > 0) and (3 < 5))  #True (and는 둘 다 만족해야 True)
print((3 > 0) & (3 < 5))    #True (& 는 and 와 동일)
print((3 > 0 ) or (3 < 5))  #True (or는 하나만 만족해도 True)

print(3 > 2 > 1)    #True
print(5 > 3 > 7)    #False