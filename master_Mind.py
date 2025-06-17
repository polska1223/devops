import random

COLORS = ['R', 'G', 'B', 'Y', 'O', 'P']  # 6 kleuren

def generate_Code(length=4):
    return [random.choice(COLORS) for _ in range(length)]

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))

    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)

    return black_Pegs, white_Pegs

def play_Mastermind():
    print("Welkom bij Mastermind!")
    print("Raad de 4 kleuren code. Kies uit: R, G, B, Y, O, P")
    print("Bijvoorbeeld: RGBY")
    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_Guess = False
        while not valid_Guess:
            guess = input(f"Poging {attempt}: ").strip().upper()
            valid_Guess = len(guess) == 4 and all(c in COLORS for c in guess)
            if not valid_Guess:
                print("Ongeldige invoer. Gebruik 4 letters van R, G, B, Y, O, P.")

        black, white = get_Feedback(secret_Code, guess)
        print(f"Zwarte pinnen (juiste kleur & positie): {black}, Witte pinnen (juiste kleur, verkeerde plek): {white}")

        if black == 4:
            print(f"Gefeliciteerd! Je hebt de code geraden: {''.join(secret_Code)}")
            return

    print(f"Helaas, je hebt verloren. De juiste code was: {''.join(secret_Code)}")

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y':
        play_Mastermind()
        again = input("Opnieuw spelen? (Y/N): ").upper()
