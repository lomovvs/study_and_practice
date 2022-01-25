a = int(input())
b = int(input())
if a < b:
    c = 1
elif a > b:
    c = -1
else:
    c = 1
    print(a)
for num in range(a, b, c):
    print(num, end=' ')
