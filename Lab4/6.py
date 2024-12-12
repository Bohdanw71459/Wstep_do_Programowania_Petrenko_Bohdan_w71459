

def func(imie, wiek=20):
    """
    Funkcja wypisuje imie i wiek podanych z input'a
    Jesli wiek nie zostanie podany - uzywana jest wartosc domyslna: 20
    """
    print(f"Imie: {imie}, Wiek: {wiek}")


print(func.__doc__)

imie = input("Podaj imie: ")
wiek = int(input("Podaj wiek: "))

func(imie, wiek)