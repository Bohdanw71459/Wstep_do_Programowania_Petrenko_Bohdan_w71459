
# W Pythonie nie ma bezpośredniego odpowiednika instrukcji switch (znanej z innych języków programowania, takich jak C++ czy Java).
# W Pythonie podobny efekt można uzyskać za pomocą wielu instrukcji `elif`, co umożliwia przejście przez różne przypadki.
# Począwszy od wersji 3.10, Python wprowadził `match-case`, co jest pewnym odpowiednikiem switch, ale `elif` wciąż jest popularnym rozwiązaniem.

def calculator(num1, num2, operation):
    if operation == "+": return num1 + num2
    elif operation == "-": return num1 - num2
    elif operation == "*": return num1 * num2
    elif operation == "/":
        if num2 != 0: return num1 / num2
        else: return "Błąd: Dzielenie przez zero!"
    elif operation == "**": return num1 ** num2
    else: return "Błąd: Nieznana operacja."

try:
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))
    oper = input("Wybierz operację (+, -, *, /, ** dla potęgowania): ")

    print("Wynik:", calculator(num1, num2, oper))

except ValueError:
    print("Błąd: Wprowadzono niepoprawne dane.")
