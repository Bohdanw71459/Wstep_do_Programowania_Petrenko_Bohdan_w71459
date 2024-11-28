import random

# losowe wartości
a = random.randint(3, 7)
b = random.randint(3, 7)

# zbiory
X = set(random.randint(0, 10) for _ in range(a))
Y = set(random.randint(0, 10) for _ in range(b))

print(f"Zbiór X: {X}")
print(f"Zbiór Y: {Y}")

# a) czy zbiór X zawiera liczbę 5
print("Czy zbiór X zawiera liczbę 5?", 5 in X)

# b) czy zbiór X jest podzbiorem zbioru Y
print("Czy zbiór X jest podzbiorem zbioru Y?", X.issubset(Y))

# c) czy zbiór Y jest podzbiorem zbioru X
print("Czy zbiór Y jest podzbiorem zbioru X?", Y.issubset(X))

# d) suma zbiorów XY
print("Suma zbiorów X i Y:", X | Y)

# e) różnica zbiorów XY
print("Różnica zbiorów X - Y:", X - Y)

# f) różnica zbiorów YX
print("Różnica zbiorów Y - X:", Y - X)

# g) ilozcyn zbiorów XY
print("Iloczyn zbiorów X i Y:", X & Y)

# h) hajwyższy element w obu zbiorach
max_element = max(X | Y)
print("Najwyższy element w obu zbiorach:", max_element)

if X:
    pierwszy_element = next(iter(X))  # pobranie pierwszego elementu
    X.remove(pierwszy_element)
    Y.add(pierwszy_element)
    print(f"Po przeniesieniu {pierwszy_element} ze zbioru X do Y:")
    print("Zbiór X:", X)
    print("Zbiór Y:", Y)

# j) przekopiowanie wszystkich elementów ze zbioru X do zbioru Y
Y.update(X)
print("Po przekopiowaniu elementów zbioru X do Y:")
print("Zbiór X:", X)
print("Zbiór Y:", Y)

# k) wyczyszczenie obu zbiorów
X.clear()
Y.clear()
print("Po wyczyszczeniu:")
print("Zbiór X:", X)
print("Zbiór Y:", Y)
