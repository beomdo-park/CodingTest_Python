import sys
lst = [i+1 for i in range(30)]
for _ in range(28):
    user = int(sys.stdin.readline().rstrip())
    if user in lst:
        lst.pop(lst.index(user))
print(*lst,sep="\n")