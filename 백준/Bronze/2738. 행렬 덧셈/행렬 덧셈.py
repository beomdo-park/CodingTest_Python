import sys
M,N = map(int,sys.stdin.readline().split())
lst1=[0]*M
lst2=[0]*M
result=""
for i in range(M):
    lst1[i]=list(map(int,sys.stdin.readline().split()))
for i in range(M):
    lst2[i]=list(map(int,sys.stdin.readline().split()))
for col in range(M):
    for row in range(N):
        result+=str(lst1[col][row]+lst2[col][row])+" "
    result+="\n"
print(result,end="")