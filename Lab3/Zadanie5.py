lista_zakupow = {
    "Chleb": 4.50,
    "Mleko": 3.20,
    "Masło": 8.30,
    "Ser": 12.50,
    "Jajka": 10.00
}

print("Lista zakupów:")
for artykul, kwota in lista_zakupow.items():
    print(f"- {artykul}: {kwota:.2f} zł")

# p;odsumowanie wydatków
suma = sum(lista_zakupow.values())
print(f"\nCałkowity koszt zakupów: {suma:.2f} zł")
