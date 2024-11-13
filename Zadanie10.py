try:
    x = float(input("Podaj x: "))
    y = float(input("Podaj y: "))
    z = float(input("Podaj z: "))
    
    # "bez użycia wbudowanych funkcji."
    if x <= y and x <= z:
        first = x
        if y <= z:
            second = y
            third = z
        else:
            second = z
            third = y
    elif y <= x and y <= z:
        first = y
        if x <= z:
            second = x
            third = z
        else:
            second = z
            third = x
    else:
        first = z
        if x <= y:
            second = x
            third = y
        else:
            second = y
            third = x

    print("Liczby od najmniejszej do największej:", first, second, third)

except ValueError:
    print("Wprowadzono niepoprawne dane.")
