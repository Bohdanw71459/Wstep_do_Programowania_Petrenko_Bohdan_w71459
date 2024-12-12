

def func(a):
    if a == 0: return 0
    elif a == 1: return 1
    else: return func(a - 1) + func(a - 2)

print(func(10))