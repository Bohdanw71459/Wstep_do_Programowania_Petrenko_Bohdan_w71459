import random
import string

n = int(input("Podaj liczbę ciągów znakowych (n): "))
x = int(input("Podaj długość ciągu znakowego (x): "))
s = int(input("Podaj wartość s: "))

# ttworzenie listy n-elementowej z losowymi ciągami
lista = [''.join(random.choices(string.ascii_lowercase, k=x)) for _ in range(n)]
print("Wygenerowana lista:", lista)

# konwersja na krotkę
krotka = tuple(lista)
print("Krotka:", krotka)

# a) wypisanie ilości znaków w liście
ilosc_znakow = sum(len(ciag) for ciag in krotka)
print("Ilość znaków w liście:", ilosc_znakow)

# b) wypisanie ilości liter 'k' w całej liście
ilosc_k = sum(ciag.count('k') for ciag in krotka)
print("Ilość liter 'k':", ilosc_k)

# c) wypisanie ilości ciągów znaków zawierających 'kt'
ilosc_kt = sum(1 for ciag in krotka if 'kt' in ciag)
print("Ilość ciągów zawierających 'kt':", ilosc_kt)

# d) wypisanie ilości ciągów dłuższych niż s
ilosc_dluzszych_niz_s = sum(1 for ciag in krotka if len(ciag) > s)
print("Ilość ciągów dłuższych niż s:", ilosc_dluzszych_niz_s)
