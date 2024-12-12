import math

def func(a, b, h):
    return (a + b) * h / 2

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
h = float(input("Podaj h: "))

print(func(a, b, h))