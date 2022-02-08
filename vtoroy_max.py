def calculating_second_maximum(mnozhestvo):
    mnozhestvo_sort = mnozhestvo.copy()
    mnozhestvo_sort.sort()
    mnozhestvo_dlina = len(mnozhestvo)
    if mnozhestvo_dlina > 2:
        first_maximum = mnozhestvo_sort[1]
        second_maximum = mnozhestvo_sort[0]
        for chisla in mnozhestvo:
            if chisla > first_maximum:
                second_maximum = first_maximum
                first_maximum = chisla
            elif chisla == first_maximum:
                pass
            elif chisla > second_maximum:
                second_maximum = chisla
        return second_maximum
    elif mnozhestvo_dlina == 2:
        if mnozhestvo[0] == mnozhestvo[1]:
            return None
        elif mnozhestvo[0] > mnozhestvo[1]:
            second_maximum = mnozhestvo[1]
            return second_maximum
        else:
            second_maximum = mnozhestvo[0]
            return second_maximum
    else:
        return None


result1 = calculating_second_maximum([-2, 3, 3, 15, 111, 0, 10, 2, 100, 99])
assert result1 == 100, f'Wrong answer : {result1}'
result2 = calculating_second_maximum([100, 110])
assert result2 == 100, f'Wrong answer : {result2}'
result3 = calculating_second_maximum([100, 100])
assert result3 == None, f'Wrong answer : {result3}'
result4 = calculating_second_maximum([-2])
assert result4 == None, f'Wrong answer : {result4}'


