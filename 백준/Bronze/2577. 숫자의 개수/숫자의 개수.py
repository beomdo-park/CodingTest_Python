import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
mult = str(a * b * c)
lst = ",".join(mult).split(",")
lst = list(map(int, lst))
for i in range(10):
    print(lst.count(i))
