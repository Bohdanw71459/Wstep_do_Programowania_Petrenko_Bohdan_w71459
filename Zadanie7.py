import random

fuel_price = 6.5
fuel_cons = float(input("Ile paliwa zużywa samochód na 100 km? (n.p. 8.5): "))
distance = random.randint(100, 500)

need = (distance / 100) * fuel_cons
cost = need * fuel_price

print("distance:", distance, "fuel_needed:", fuel_needed, "cost:", cost)
