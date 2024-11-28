ciag = input("Podaj ciąg znaków: ")

# usunięcie spacji i zmiana na małe litery
czysty_ciag = ''.join(ciag.lower().split())

if czysty_ciag == czysty_ciag[::-1]: print("Podany ciąg jest palindromem!")
else: print("Podany ciąg nie jest palindromem.")
