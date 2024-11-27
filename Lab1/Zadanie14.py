filename = input("Podaj nazwę pliku: ")
if filename.endswith((".xls", ".xlsx", ".xlsm")):
    print("To jest plik arkusza Excel.")
else:
    print("To nie jest plik arkusza Excel.")
