pred_max_znachenie = 0
max_znacenie = 0
a = 1
while a > 0:
    a = int(input())
    if a == 0:
        a = 0
    else:
        if a > max_znacenie:
            pred_max_znachenie = max_znacenie
            max_znacenie = a
        elif a > pred_max_znachenie:
            pred_max_znachenie = a
print(pred_max_znachenie)
print(max_znacenie)
