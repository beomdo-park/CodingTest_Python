import sys

N = int(sys.stdin.readline())
a = 1
count = 1

if N == 1:
    print(1)
else:
    while True:
        if a * 6 - 4 <= N < (a + count) * 6 - 4:
            print(count+1)
            break
        a += count
        count += 1
