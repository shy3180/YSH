unique_num = map(int, input().split())
sum = 0

for i in unique_num:
    sum += i**2

result = sum % 10
print(result)
