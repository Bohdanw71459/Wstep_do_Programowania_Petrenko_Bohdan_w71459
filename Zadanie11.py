import math

try:
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))

    if a == 0:
        print("To nie jest równanie kwadratowe (a nie może być 0).")
    else:
        # b^2 - 4ac
        delta = b**2 - 4 * a * c

        # a i obliczanie pierwiastków
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print("równanie ma dwa rozwiązania rzeczywiste: x1 =", x1, "oraz x2 =", x2)
        elif delta == 0:
            # jeden podwójny pierwiastek rzeczywisty
            x = -b / (2 * a)
            print("równanie ma jedno podwójne rozwiązanie rzeczywiste: x =", x)
        else:
            # brak rozwiązań rzeczywistych, rozwiązania zespolone
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(-delta) / (2 * a)
            x1 = complex(real_part, imaginary_part)
            x2 = complex(real_part, -imaginary_part)
            print("równanie ma dwa rozwiązania zespolone: x1 =", x1, "oraz x2 =", x2)

except ValueError:
    print("Wprowadzono niepoprawne dane.")
