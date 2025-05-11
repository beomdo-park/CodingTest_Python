import sys

T = int(sys.stdin.readline())
for i in range(T):
    sum = 0
    count = 0

    a = list(map(int, sys.stdin.readline().split()))

    for j in range(a[0]):
        sum += a[j + 1]
    avg = sum / a[0]

    for j in range(a[0]):
        if a[j + 1] > avg:
            count += 1

    print(f"{count / a[0] * 100:.3f}%")
