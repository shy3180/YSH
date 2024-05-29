S = list(input().split())

C1 = 0
C2 = 0
vouwl1 = ["a", "e", "i", "o", "u"]
vouwl2 = ["a", "e", "i", "o", "u", "y"]


for i in S:
    if i in vouwl1:
        C1 += 1
    if i in vouwl2:
        C2 += 1

print(C1, C2)
