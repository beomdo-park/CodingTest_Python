import sys

N = int(sys.stdin.readline())
su = sys.stdin.readline().split()


prime = []
li = [False, False] + [True] * 999
for j in range(2, 1001):
    if li[j]:
        prime.append(j)
        for k in range(2 * j, 1001, j):
            li[k] = False
count = 0

for i in range(N):
    if int(su[i]) in prime:
        count += 1
print(count)
