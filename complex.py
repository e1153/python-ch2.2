# 복소수 = 실수부 + 허수부
# 허수부 i, j 를 숫자뒤에 붙인다.


a = 4 + 5j
print(type(a))
print(isinstance(a, complex))

b = 7-2j
print(a + b)
print(b.real, b.imag)

# complex
p = 2.5
q = -3
print(complex(p, q))
