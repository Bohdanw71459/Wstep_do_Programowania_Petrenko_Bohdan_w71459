import string

zdanie = input("Podaj zdanie: ")

# a) wypisanie wszystkich występujących liter w kolejności alfabetycznej i brakujących liter alfabetu
wystepujace_litery = sorted(set(zdanie.lower()) & set(string.ascii_lowercase)) 
brakujace_litery = sorted(set(string.ascii_lowercase) - set(wystepujace_litery))
print("Występujące litery:", ''.join(wystepujace_litery))
print("Brakujące litery:", ''.join(brakujace_litery))

# b) usunięcie znaków o nieparzystych indeksach i wyświetlenie wyniku
pozostale_znaki = zdanie[::2]
print("Zdanie z usuniętymi znakami o nieparzystych indeksach:", pozostale_znaki)

# c) każdy wyraz zaczyna się i kończy wielką literą
wyrazy = zdanie.split()
wyrazy_zmienione = [slowo.capitalize()[:-1] + slowo[-1].upper() if len(slowo) > 1 else slowo.upper() for slowo in wyrazy]
print("Zdanie z każdym wyrazem rozpoczynającym i kończącym się wielką literą:", ' '.join(wyrazy_zmienione))

# d) najdlusze słowo i jego dlugość
najdluzsze_slowo = max(wyrazy, key=len) if wyrazy else ""
print("Najdłuższe słowo:", najdluzsze_slowo)
print("Długość najdłuższego słowa:", len(najdluzsze_slowo))

# e) zamiana powtarzających się znaków na '@'
unikalne_znaki = set()
zmienione_zdanie = ''
for znak in zdanie:
    if znak in unikalne_znaki:
        zmienione_zdanie += '@'
    else:
        zmienione_zdanie += znak
        unikalne_znaki.add(znak)
print("Zdanie z powtórzonymi znakami zamienionymi na '@':", zmienione_zdanie)
