
a= 1.2
print(a, type(a))
print(isinstance(a, float))

b = 2.0
print(b, type(b))
# 객체 함수 is_intager()는 값이 정수 인지 실수 인지 확인하는 함수
# 타입을 확인하는 함수가 아니다.
print(b.is_integer())

# 다른 언어와 마찬기지로 e, E사용한 부동소수점 표기가 가능하다.
b = 2e3
c = 0.2e-4
print(b, c)