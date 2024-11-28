imiona = ["Anna", "Krzysztof", "Maria", "Zbigniew"]

# a) sortujemy liste alfabetycznie i wyświetlamy
imiona.sort()
print("Posortowana lista:", imiona)

# b) dodajemy na końcu dwie osoby i pobieramy ostatnią z nich poleceniem pop()
imiona.append("Jan")
imiona.append("Ewa")

ostatnia_osoba = imiona.pop()
print("Lista po dodaniu i usunięciu ostatniej osoby:", imiona)
print("Usunieta osoba:", ostatnia_osoba)

# c) na pozycji 3 dodajemy jeszcze jedną osobę
imiona.insert(2, "Piotr")  # Pozycja 3 to indeks 2 (liczenie od zera)
print("Lista po dodaniu osoby na pozycji 3:", imiona)

# d) odwracamy kolejność na liście i dublujemy ją
imiona.reverse()
imiona *= 2  # Dublujemy liste
print("Odwrócona i zdublowana lista:", imiona)
