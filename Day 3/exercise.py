a = list(map(int, input("Nhập dãy số: ").split()))

prefix = []

for i in range(len(a)):
    if i == 0:
        prefix.append(a[0])
    else:
        prefix.append(prefix[i-1] + a[i])

print(prefix)