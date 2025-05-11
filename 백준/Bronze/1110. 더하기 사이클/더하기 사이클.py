import sys

N = int(sys.stdin.readline())
a = N // 10
b = N % 10
sum = 0
count = 0
while True:
    if a == 0:
        sum = b
        a = b
        b = sum % 10
        count += 1
    else:
        sum = a + b
        a = b
        b = sum % 10
        count += 1
    if N == 10 * a + b:
        break
print(count)
