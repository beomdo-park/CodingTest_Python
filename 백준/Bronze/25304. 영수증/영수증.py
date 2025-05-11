import sys
total = int(sys.stdin.readline().rstrip())
N= int(sys.stdin.readline().rstrip())

sum = 0
for i in range(N):
    a,b = map(int,sys.stdin.readline().split())
    sum+=a*b
print("Yes" if sum==total else "No")