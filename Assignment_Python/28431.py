S = []

for i in range(5):
    N = int(input())

    if N in S:
        S.remove(N)
    else:
        S.append(N)

print(S[0])
