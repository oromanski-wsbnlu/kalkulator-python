def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def mnoz(a, b):
    return a * b

def dziel(a, b):
    if b == 0:
        return "Błąd: dzielenie przez zero!"
    return a / b

print("=== Kalkulator ===")
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
print("Wybierz działanie: 1-Dodawanie, 2-Odejmowanie, 3-Mnożenie, 4-Dzielenie")
wybor = input("Twój wybór: ")

if wybor == "1":
    print("Wynik:", dodaj(a, b))
elif wybor == "2":
    print("Wynik:", odejmij(a, b))
elif wybor == "3":
    print("Wynik:", mnoz(a, b))
elif wybor == "4":
    print("Wynik:", dziel(a, b))
else:
    print("Nieznana opcja!")
