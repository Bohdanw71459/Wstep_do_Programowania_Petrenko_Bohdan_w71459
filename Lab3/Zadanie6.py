# słownik z rachunkami za prąd (miesiąc to jest wartość)
rachunki_prad = {
    "Styczeń": 120.50,
    "Luty": 150.20,
    "Marzec": 130.80,
    "Kwiecień": 140.00,
    "Maj": 135.60,
    "Czerwiec": 155.75
}

# wartośc maksymalna, minimalna, suma średnia
maksymalny_rachunek = max(rachunki_prad.values())
minimalny_rachunek = min(rachunki_prad.values())
suma_rachunkow = sum(rachunki_prad.values())
srednia_rachunkow = suma_rachunkow / len(rachunki_prad)

print(f"Najwyższy rachunek: {maksymalny_rachunek:.2f} zł")
print(f"Najniższy rachunek: {minimalny_rachunek:.2f} zł")
print(f"Suma rachunków: {suma_rachunkow:.2f} zł")
print(f"Średnia wartość rachunku: {srednia_rachunkow:.2f} zł")

# czy ostatni miesiąc przekroczył średnią?
ostatni_rachunek = list(rachunki_prad.values())[-1]
if ostatni_rachunek > srednia_rachunkow:
    print("Trzeba zacisnąć pasa")
else:
    print("Wszystko okay")
