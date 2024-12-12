
def func(masa, wzrost):
    bmi = masa / (wzrost * wzrost)
    print("Twoje BMI to", bmi)
    if bmi < 16: return "wygłodzenie"
    elif bmi < 17: return "wychudzenie"
    elif bmi < 18.5: return "niedowaga"
    elif bmi < 25: return "pożądana masa ciała"
    elif bmi < 30: return "nadwaga"
    elif bmi < 35: return "otyłość I stopnia"
    elif bmi < 40: return "otyłość II stopnia"
    else: return "otyłość III stopnia"

masa = float(input("Podaj masę ciała: "))
wzrost = float(input("Podaj wzrost ciała: "))
wzrost /= 100

print(func(masa, wzrost))