a = int(input())
print(
    a * 0.01 + 25
    if 100 <= a * 0.01 + 25 <= 2000
    else 100 if a * 0.01 + 25 < 100 else 2000
)
