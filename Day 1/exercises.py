name = "Han"
age = 20
university = "BKU"
major = "Computer Science"
gpa = 3.9

print("My name is:", name)
print("I'm", age, "years old")
print("I study", major, "at", university)
print("My GPA is:", gpa)

print(type(name))
print(type(age))
print(type(gpa))

name = input("Enter your name: ")
age = int(input("Enter your age: "))
university = input("Enter your university: ")
major = input("Enter your major: ")
gpa = float(input("Enter your GPA: "))

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Sum:", a+b)
print("Difference:", a-b)
print("Product:", a*b)
print("Division:", a/b)
print("Integer division:", a//b)
print("Remainder:", a%b)

gpa = float(input("Enter your GPA: "))
if gpa >= 8.5:
    print("Excellent")
elif gpa >= 7.0:
    print("Good")
elif gpa >= 5.0:
      print("Pass")
else: 
    print("Fail")

def is_prime(n):
    if (n < 2):
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if (n % i == 0):
                return False
    return True

n = int(input("Enter n: "))
count = 0
for i in range(2, n + 1):
    if is_prime(i):
        count += 1
print(count)

n = int(input("input: "))
a = list(map(int, input("Nhập dãy số: ").split()))

max = float('-inf')
second_max = float('-inf')
for i in range(1, n):
    if a[i] >= max:
        second_max = max
        max = a[i]
    elif a[i] > second_max and a[i] != max:
        second_max = a[i]

print("Số lớn nhất:", max)
print("Số lớn thứ hai:", second_max)