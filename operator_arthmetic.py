
print(2 * 3)
print(2 + 3)
print(2 - 3)
print(2 / 3)
print(2 / 3.0)
print(2.0 / 3)
print(2.0 / 3.0)

# //(몫), **(지수승), %(나머지 연산)
print(2 // 3)
print(2 ** 3)
print(2 % 3)

# divmod 연산
print(divmod(2, 3))

# 연산자 우선 순위
print(2 + 3 * 4)
print(-2 + 3 * 4)
print(-(2 + 3) * 4)

print(4 / 2 * 2) # 나누기는 결과값이 정수일 경우에도 항상 float로 표기 됨

# 결합순서 주의
print(2 ** 3 ** 4) # 2의 81승
print((2 ** 3) ** 4) # 8의 4승
print(2 ** (3 ** 4)) # 2의 81승

# 객체의 대소 비교
print(1 > 3)
print(2 < 4)

print(4 <= 5)
print(4 >= 5)

print(6 == 9)
print(6 != 9)

# 복합 관계식
a = 6
print(0 < a and a < 10) # 자바에서&& 는 파이썬에서 and or 등으로 표시함 and를 쓰지 않고 아래와같이도 표시가능
print(0 < a < 10)

# 수치형 이외의 다른 타입의 객체 비교
print("abcd" > "abc")

# 동질성 비교 : ==, 동일성 비교 : is
a = 10
b = 20
c = a

print(a == b)
print(a is b)
print(a is c)
print(a == c)

