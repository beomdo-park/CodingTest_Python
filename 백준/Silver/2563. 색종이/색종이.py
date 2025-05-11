import sys
N = int(sys.stdin.readline())

lst = [[0 for i in range(100)] for i in range(100)]

def a(x,y):
    for i in range(x, x+10):
        for j in range(y,y+10):
            lst[i][j] = 1
    
for i in range(N):
    x,y = map(int, sys.stdin.readline().split())
    a(x,y)

print(sum(map(lambda x: sum(x), lst)))