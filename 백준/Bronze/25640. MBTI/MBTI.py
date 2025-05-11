import sys
Jinho = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
count =0
for i in range(N):
    if sys.stdin.readline().rstrip()==Jinho:
        count+=1
print(count)