a = 10
b = 20

sum = a + b
print("sum=", sum)

num = 15

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
 
num = 5
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial of", num, "=", factorial)
  
n = 10

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    
text = "Python"

reversed_text = text[::-1]

print("Original String:", text)
print("Reversed String:", reversed_text)

word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

num = 153

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")