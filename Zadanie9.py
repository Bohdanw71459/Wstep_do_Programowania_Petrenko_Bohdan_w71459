def calculate(age, is_student=False):
    if not (0 <= age <= 130):
        return "Wprowadzony wiek jest poza zakresem (0-130 lat)"

    if age < 4: return 0
    elif age < 18: return 10
    elif is_student: return 20 * 0.75 # 25% znizka
    else: return 20

try:
    age = int(input("Ile masz lat?: "))
    student_input = input("Czy jesteś uczniem/studntem? (tak/nie): ").strip().lower()

    price = calculate(age, student_input == "tak")
    if isinstance(price, str): print(price)  # Wyświetlanie błędu
    else: print(f"Cena biletu wynosi: {price} zł")
    
except ValueError:
    print("Podaj liczbę całkowitą.")
