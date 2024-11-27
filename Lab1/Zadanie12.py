# funkcja a
def a(x):
    if x > 0:
        return 2 * x
    elif x == 0:
        return 0
    else:
        return -3 * x

# funkcja b
def b(x):
    if x >= 1:
        return x ** 2
    else:
        return x

# funkcja c
def c(x):
    if x > 2:
        return 2 + x
    elif x == 2:
        return 8
    else:
        return x - 4

try:
    x = float(input("Podaj wartość x: "))

    print("a(x) =", a(x))
    print("b(x) =", b(x))
    print("c(x) =", c(x))

except ValueError:
    print("Wprowadzono niepoprawną wartość.")
