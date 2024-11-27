liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))

mniejsza = min(liczba1, liczba2)
wieksza = max(liczba1, liczba2)

print("Liczby parzyste w przedziale:")
for i in range(mniejsza, wieksza + 1):
    if i % 2 != 0:  # jesli liczba jest nieparzysta - pomijamy ją3
        continue
    print(i)
