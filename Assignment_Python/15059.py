Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())

C = 0
B = 0
P = 0

if Cr - Ca > 0:
    C == Cr - Ca
else:
    C == 0

if Br - Ba > 0:
    B == Br - Ba
else:
    B == 0

if Pr - Pa > 0:
    P == Pr - Pa
else:
    P == 0

Total = C + B + P
print(Total)
