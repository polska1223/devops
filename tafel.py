#!/usr/bin/env python3

getal = int(input("Voer een getal in tussen 1 en 10: "))

if 1 <= getal <= 10:
    print(f"Tafel van {getal}:")
    for i in range(1, 11):
        print(f"{getal} x {i} = {getal * i}")
else:
    print("Ongeldig getal. Voer een getal in tussen 1 en 10.")
