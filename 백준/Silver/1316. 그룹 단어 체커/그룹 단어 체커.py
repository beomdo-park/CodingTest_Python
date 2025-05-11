import sys

lst = []
result = 0
N = int(sys.stdin.readline())


def list_overlap_del(lst):
    result_list = []

    for i in range(len(lst)):
        if i == 0:
            result_list.append(lst[i])

        elif result_list[-1] != lst[i]:
            result_list.append(lst[i])
    return result_list


for i in range(N):
    lst.append(sys.stdin.readline().strip())

for i in lst:
    T = 0
    i = ",".join(i).split(",")
    i = list_overlap_del(i)

    for j in range(len(i)):
        if i.count(i[j]) >= 2:
            T += 1
    if T == 0:
        result += 1
print(result)
