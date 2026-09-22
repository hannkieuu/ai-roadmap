n = int(input("n: "))
a = list(map(int, input("Nhập dãy số: ").split()))
b = []

for i in range(n):
    b.append(a[n-i+1])

n = int(input("n: "))
a = list(map(int, input("Nhập dãy số: ").split()))

maxcount = 0
number = a[0]
count = 1

for i in range(n-1):
    if a[i] == a[i+1]:
        count += 1
    else:
        if count > maxcount:
            maxcount = count
            number = a[i]
        count = 1

if count > maxcount:
    maxcount = count
    number = a[n-1]

a = [12, 5, 8, 3, 17, 6]
x = int(input("Nhập x: "))

for i in range(len(a)):
    if a[i] == x:
        print("Vị trí của x trong mảng là:", i)
        found = True
        break

if not found:
    print(-1)

a = [1, 3, 5, 7, 9, 12]
target = 10
L = 0
R = len(a) - 1

while L < R:
    total = a[L] + a[R]

    if total == target:
        print("Found:", a[L], a[R])
        break
    elif total < target:
        L +=1
    else:
        R -= 1