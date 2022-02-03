a = 1
c = ()
while a > 0:
    a = int(input())
    if a > 0:
        b = tuple(a)
        c = c + b
        print(type(a))
        print(type(c))
        print(a)
        print(c)
    else:
        pass