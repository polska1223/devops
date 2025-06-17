#!/usr/bin/env python3

getal = -1  # start met een willekeurig getal dat niet 0 is

while getal != 0:
    getal = int(input("Voer een getal in (0 om te stoppen): "))
    if getal > 0:
        print("Dat is een positief getal! Goed bezig 😊")
    elif getal < 0:
        print("Dat is een negatief getal.")
    elif getal == 0:
        print("Je hebt 0 ingevoerd. Het programma stopt.")
