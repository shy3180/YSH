lec = input()
N = int(input())
result = 0

for _ in range(N):
    re_lec = input()
    if lec[:5] == re_lec[:5]:
        result += 1

print(result)
