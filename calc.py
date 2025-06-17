#!/usr/bin/env python3

getal1 = float(input("Voer het eerste getal in: "))
getal2 = float(input("Voer het tweede getal in: "))

print("\n--- Resultaten ---")
print(f"{getal1} + {getal2} = {getal1 + getal2}")
print(f"{getal1} - {getal2} = {getal1 - getal2}")
print(f"{getal1} * {getal2} = {getal1 * getal2}")
if getal2 != 0:
    print(f"{getal1} / {getal2} = {getal1 / getal2}")
else:
    print("Delen door nul is niet mogelijk.")
