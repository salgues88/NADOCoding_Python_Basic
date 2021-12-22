

print(2 + 3 * 4)        #14
print((2 + 3) *4)       #20

number = 2 + 3 * 4      #14
print(number)           #14

number = number + 2     #16
print(number)

number += 2             #18 (a += b 는 a = a + b)
print(number)           

number *= 2             #36 (a *= b 는 a = a * b)
print(number)

number /= 2             #18 (a /= b 는 a = a / b)
print(number)

number -= 2             #16 (a -= b 는 a = a - b)
print(number)

number %= 5             #1 (a %= b 는 a = a / b 계산 후 몫이 아닌 나머지값)
print(number)
