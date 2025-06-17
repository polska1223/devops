
import random


COLORS = ['R', 'G', 'B', 'Y', 'O', 'P']  

def generate_code(length=4):
    """Genereer een geheime code van kleuren"""
    return [random.choice(COLORS) for _ in range(length)]

def get_feedback(secret, guess):
    """Geef feedback in zwarte en witte pins (correcte plaats/ verkeerde plaats)"""
    black_pegs = sum(s == g for s, g in zip(secret, guess))

    secret_counts = {}
    guess_counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_counts[s] = secret_counts.get(s, 0) + 1
            guess_counts[g] = guess_counts.get(g, 0) + 1

    white_pegs = sum(min(secret_counts.get(color, 0), guess_counts.get(color, 0)) for color in guess_counts)

    return black_pegs, white_pegs

def is_valid_guess(guess, length=4):
    """Controleer of de invoer geldig is"""
    if len(guess) != length:
        return False
    for c in guess:
        if c not in COLORS:
            return False
    return True

def play_mastermind():
    print("Welkom bij Mastermind!")
    print(f"Raad de geheime code van {len(COLORS)} kleuren: {', '.join(COLORS)}")
    print("De code bestaat uit 4 kleuren. Probeer hem te raden in maximaal 10 beurten.")
    print("Voer je gok in als een reeks van 4 letters, bv. RGBY")

    secret_code = generate_code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
        while True:
            guess = input(f"Beurt {attempt}: ").strip().upper()
            if is_valid_guess(guess):
                break
            else:
                print(f"Ongeldige invoer! Gebruik precies 4 letters uit {COLORS}")

        black, white = get_feedback(secret_code, list(guess))
        print(f"Zwarte pins (juiste kleur en plaats): {black}")
        print(f"Witte pins (juiste kleur, verkeerde plaats): {white}")

        if black == 4:
            print(f"Gefeliciteerd! Je hebt de code geraden: {''.join(secret_code)}")
            return

    print(f"Helaas, je hebt alle pogingen gebruikt. De juiste code was: {''.join(secret_code)}")

def main():
    while True:
        play_mastermind()
        again = input("Wil je opnieuw spelen? (J/N): ").strip().upper()
        if again != 'J':
            print("Bedankt voor het spelen!")
            break

if __name__ == "__main__":
    main()
