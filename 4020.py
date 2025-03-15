# هدف: معرفی عملگرهای مختلف در پایتون شامل عملگرهای ریاضی، منطقی، انتساب و بیتی


# عملگرهای ریاضی (Arithmetic Operators)
a = 10
b = 7
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)

# عملگرهای منطقی (Logical Operators) :
# and
a = True
b = False
result = a and b
print(result)
# or 
print(a or b)
# not
b =  True
print(not b)

# عملگرهای انتساب (Assignment Operators) :
x = -10
x -= +5
print(x)
x = 7
x *= 3
print(x) 
x = 8
x /= 3
print(x)

# عملگرهای بیتی (Bitwise Operators) :
# AND & bit
x = 5
y = 3
print(x & y)
# OR | bit
x = 2
y = y
print(x | y)
# XOR ^ bit
x = 19
y = 84
print(x ^ y)
# NOT ~ bit
x = 19
result =~x
print(result)
# << (شیفت به چپ)
x = 5
result = x << 2
print(result)
# >> (شیفت به راست)
x = 5
result = x >> 1
print(result)
