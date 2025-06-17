#!/usr/bin/env python3

afstand_mijlen = float(input("Hoe ver is Afrika (in mijlen)? "))
snelheid_kmph = float(input("Hoe snel vliegt de zwaluw (in km/u)? "))

afstand_km = afstand_mijlen * 1.60934  # conversie mijl naar km
tijd_uren = afstand_km / snelheid_kmph
tijd_minuten = tijd_uren * 60

print(f"\nDe zwaluw doet er ongeveer {tijd_minuten:.2f} minuten over.")
