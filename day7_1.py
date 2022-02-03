import random
d = 0
e = []
while d < 10:
    d += 1
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = (a - b) * a
    e.append(c)
    f = list(e)
    e.sort()
print(f)
print(e)
