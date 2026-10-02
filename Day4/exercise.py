a = [2, 4, 1, 5, 3, 2]
k = 3

window_sum = 0
for i in range(k):
    window_sum += a[i]
# tính tổng window đầu tiên
max_sum = window_sum
# bắt đầu trượt window
for i in range(k, len(a)):
    window_sum = window_sum - a[i - k] + a[i]
    if window_sum > max_sum:
        max_sum = window_sum

print(max_sum)

a = [2, 1, 5, 1, 3, 2]
target = 7

L = 0
window_sum = 0
min_length = len(a) + 1

for R in range(len(a)):
    window_sum += a[R]
    while window_sum >= target:
        min_length = min(min_length, R - L + 1)
        window_sum -= a[L]
        L += 1

print(min_length)