import imp


import sys

N = int(sys.stdin.readline())
count = 1

sum = 1
while True:
    if sum <= N < sum + count:
        if count % 2 == 0:
            m = count
            n = 1
        elif count % 2 == 1:
            m = 1
            n = count
        break
    sum += count
    count += 1


for i in range(N - sum):
    if count % 2 == 1:
        if m == count:
            m = count + 1
            n = 1
            count += 1
        else:
            n -= 1
            m += 1

    elif count % 2 == 0:
        if n == count:
            n = count + 1
            m = 1
            count += 1
        else:
            m -= 1
            n += 1

print(f"{n}/{m}")
