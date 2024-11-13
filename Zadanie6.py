distance = int(input("Ile kilometrów przejechał samochód? (n.p. 250): "))
fuel_cons = float(input("Ile paliwa zużywa samochód na 100 km? (n.p. 8.5): "))
fuel_price = 6.5

need = (distance / 100) * fuel_cons
cost = need * fuel_price

print("Koszt:", cost, "suma potrzebnego paliwa:", need)
