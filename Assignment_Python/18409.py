N = int(input())
S = input()
M = 0

for i in S:
    if i in ["a", "e", "i", "o", "u"]:
        M += 1
print(M)
