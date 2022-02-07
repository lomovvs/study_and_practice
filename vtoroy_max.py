def vtoroyMax(mnozhestvo):
    mnozhestvoSort = mnozhestvo.copy()
    mnozhestvoSort.sort()
    mnozhestvoDlina = len(mnozhestvo)
    if mnozhestvoDlina > 2:
        mn1 = mnozhestvo[1]
        mn2 = mnozhestvo[0]
        for chisla in mnozhestvo:
            if chisla > mn1:
                mn2 = mn1
                mn1 = chisla
            elif chisla == mn1:
                pass
            elif chisla > mn2:
                mn2 = chisla
        return mn2
    elif mnozhestvoDlina == 2:
        if mnozhestvo[0] == mnozhestvo[1]:
            return False
        elif mnozhestvo[0] > mnozhestvo[1]:
            mn2 = mnozhestvo[1]
            return mn2
        else:
            mn2 = mnozhestvo[0]
            return mn2
    else:
        return False

result1 = vtoroyMax([-2, 888, 3, 3, 15, 111, 0, 100, -15, 2, 0, 100, 99])
assert result1 == 111, f'Wrong answer : {result1}'
result2 = vtoroyMax([100, 110])
assert result2 == 100, f'Wrong answer : {result2}'
result3 = vtoroyMax([100, 100])
assert result3 == False, f'Wrong answer : {result3}'
result4 = vtoroyMax([-2])
assert result4 == False, f'Wrong answer : {result4}'


