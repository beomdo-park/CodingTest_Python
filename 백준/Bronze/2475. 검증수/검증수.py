import sys
lst = list(map(int,sys.stdin.readline().split()))
sum = 0
for i in lst:
    sum +=i**2
print(sum%10)