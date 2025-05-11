import sys

T = sys.stdin.readline().strip().lower()  # 입력받은 값을 소문자로 변환
lst = []
for i in range(ord("a"), ord("z") + 1):
    if T.count(chr(i)) == 0:
        pass
    else:
        lst.append("{0}{1}".format(chr(i), T.count(chr(i))))
lst2 = []

for i in lst:
    lst2.append(int(i[1:]))


if lst2.count(max(lst2)) >= 2:
    print("?")

else:
    print((lst[lst2.index(max(lst2))])[0].upper())
