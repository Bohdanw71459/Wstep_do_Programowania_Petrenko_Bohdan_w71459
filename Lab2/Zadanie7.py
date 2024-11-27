imie = input("Podaj swoje imię: ")
print(f"Witaj, {imie}!")

wiek = input("Podaj swój wiek: ")
print(f"Twój wiek to: {wiek}")

imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
inicjaly = imie[0].upper() + nazwisko[0].upper()
print(f"Inicjały: {inicjaly}")

lancuch = input("Podaj jakiś łańcuch znaków: ")
print(lancuch * 5)

lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
polaczony = lancuch1 + lancuch2
print(f"Połączony łańcuch: {polaczony}")

lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
polowa1 = lancuch1[:len(lancuch1)//2]  # pierwsza połowa pierwszego 
polowa2 = lancuch2[len(lancuch2)//2:]  # druga połowa drugiego
nowy_lancuch = polowa1 + polowa2
print(f"Nowy łańcuch: {nowy_lancuch}")
