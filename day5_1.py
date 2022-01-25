b = 1
a = []
c = -1
d = 0
while b > 0:
    c += 1
    i = input().split()
    b = int(i[0])
    if b > 0:
        a.extend(i)
    else:
        pass
while d < c:
    print(a[d], end=',')
    d += 2