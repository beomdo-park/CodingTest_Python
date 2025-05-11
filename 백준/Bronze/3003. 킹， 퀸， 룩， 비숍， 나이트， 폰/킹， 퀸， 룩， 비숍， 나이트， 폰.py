import sys
lst = list(map(int,sys.stdin.readline().split()))
data = [1,1,2,2,2,8]
for i in range(6):
    print(data[i]-lst[i],end=" ")