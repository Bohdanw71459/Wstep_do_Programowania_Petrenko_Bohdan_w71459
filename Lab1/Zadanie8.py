while True:
    age = input("\nIle masz lat?: ")

    if age.isdigit():
        age = int(age)
        if 0 <= age <= 130:
            print("Użytkownik jest pełnoletni." if age >= 18 else "Użytkownik nie jest pełnoletni.")
            break
        else:
            print("Podaj poprawne liczbę.")
    else:
        print("Podaj liczbę całkowitą.")
