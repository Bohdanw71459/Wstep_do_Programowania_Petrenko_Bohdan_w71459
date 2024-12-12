import math
def func(a, b, c):
    if a > b + c or b > c + a or c > a + b: print("Ne istneje trójkąta")
    elif a < 0 or b < 0 or c < 0: print("Ne istneje trójkąta")
    else:
        p = (a + b + c) / 2
        pole = math.sqrt(p * (p-a)*(p-b)*(p-c))
        print(f"trójkąta ma pole rowne: {pole}")

a = float(input("Podaj dlugosc 1 boku: "))
b = float(input("Podaj dlugosc 2 boku: "))
c = float(input("Podaj dlugosc 3 boku: "))

func(a, b, c)