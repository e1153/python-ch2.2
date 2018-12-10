# 2진, 8진, 10진, 16진 Literal

a = 23
print(type(a))

b = 0b1101
o = 0o23
h = 0x23

print(b, o, h)

e = 2**1024
print(e, type(e))
print(e.bit_length())
print(oct(38))
print(hex(38))
print(bin(38))
