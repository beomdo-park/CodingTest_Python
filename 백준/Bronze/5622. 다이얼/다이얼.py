import sys

time = 0
A = sys.stdin.readline().strip()

lst = ["3ABC", "4DEF", "5GHI", "6JKL", "7MNO", "8PQRS", "9TUV", "10WXYZ"]

for i in A:
    for j in lst:
        if i in j:
            if int(j[0]) == 1:
                time += 10
            else:
                time += int(j[0])
print(time)
