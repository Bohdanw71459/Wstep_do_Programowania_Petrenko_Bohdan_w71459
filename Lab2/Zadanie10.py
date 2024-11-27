liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))

mniejsza = min(liczba1, liczba2)
wieksza = max(liczba1, liczba2)

print("Liczby od mniejszej do większej:")
for i in range(mniejsza, wieksza + 1):
    print(i)
