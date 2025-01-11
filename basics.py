num = int(input("Enter an integer: "))
print("You entered:", num)

num1 = int(input("Enter another integer: "))
print("You entered:", num1)

sum_result = num + num1
print("Addition of two numbers is:", sum_result)

sub_result = num - num1
print("Subtraction of two numbers is:", sub_result)

if num1 != 0:
    div_result = num / num1
    print("Division of two numbers is:", div_result)
else:
    print("Division by zero is not allowed.")

if num1 != 0:
    rem_result = num % num1
    print("Remainder is:", rem_result)
else:
    print("Cannot compute remainder with zero.")

if num1 != 0:
    flt_result = num // num1
    print("Integer division result is:", flt_result)
else:
    print("Cannot perform integer division by zero.")

pow_result = num ** num1
print("Power result is:", pow_result)

a = 10
b = 10.5
c = a + b
print(c)

x = 3.14
y = int(x)
print(y)

a = 21
b = 13
c = 40
d = 37
p = (a - b) <= (c + d)
print(p)

P = (9 == 9)
Q = (7 > 5)
R = P and Q
S = P or Q
T = not P
print(R)
print(S)
print(T)

a = 12
x = a >> 2
y = a << 1
print(x, y)

a = 16
b = 12
c = a + (b >> 1)
print(c)

name = 'Roshan'
print(name)