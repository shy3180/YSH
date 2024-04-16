S = int(input())

for i in range(1, S + 1):
    print(" " * (i - 1) + "*" * (S - i + 1))
