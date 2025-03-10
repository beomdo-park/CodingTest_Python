N, M = map(int, input().split())
card = list(map(int, input().split()))
result = 0

card.sort()  # card를 오름차순으로 정렬

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum = card[i] + card[j] + card[k]
            if sum <= M:
                result = max(result, sum)

print(result)
