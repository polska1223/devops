import random

COLORS = ['R', 'G', 'B', 'Y', 'O', 'P']  # 6 kleuren

def generate_code(length=4):
    return [random.choice(COLORS) for _ in range(length)]

def get_feedback(secret, guess):
    black_pegs = sum(s == g for s, g in zip(secret, guess))

    secret_counts = {}
    guess_counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_counts[s] = secret_counts.get(s, 0) + 1
            guess_counts[g] = guess_counts.get(g, 0) + 1

    white_pegs = sum(min(secret_counts.get(d, 0), guess_counts.get(d, 0)) for d in guess_counts)

    return black_pegs, white_pegs

def play_mastermind():
    print("Welkom bij Mastermind!")
    print("Raad de 4 kleuren code. Kies uit: R, G, B, Y, O, P")
    print("Bijvoorbeeld: RGBY")
    debug_mode = False
    secret_code = generate_code()
    if debug_mode:
        print(f"[DEBUG] Geheime code: {''.join(secret_code)}")
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_guess = False
        while not valid_guess:
            guess = input(f"Poging {attempt}: ").strip().upper()
            
            if not guess:
                print("Je hebt niets ingevuld. Probeer opnieuw.")
                continue

            valid_guess = len(guess) == 4 and all(c in COLORS for c in guess)
            if not valid_guess:
                print("Ongeldige invoer. Gebruik 4 letters van R, G, B, Y, O, P.")

        black, white = get_feedback(secret_code, guess)
        print(f"Zwarte pinnen (juiste kleur & positie): {black}, Witte pinnen (juiste kleur, verkeerde plek): {white}")

        if black == 4:
            print(f"Gefeliciteerd! Je hebt de code geraden: {''.join(secret_code)}")
            return

    print(f"Helaas, je hebt verloren. De juiste code was: {''.join(secret_code)}")

if __name__ == "__main__":
    play_again = 'Y'
    while play_again == 'Y':
        play_mastermind()
        play_again = input("Opnieuw spelen? (Y/N): ").upper()