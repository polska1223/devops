
import random

def generate_Code(length=4, colors="RGBYOP"):
    """Genereert een geheime code met 4 willekeurige kleuren"""
    return [random.choice(colors) for _ in range(length)]

def get_Feedback(secret, guess):
    """Geeft aantal black pegs (juiste kleur en positie) en white pegs (juiste kleur, verkeerde positie)"""
    black_Pegs = sum(s == g for s, g in zip(secret, guess))

    
    secret_Counts = {}
    guess_Counts = {}
    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(c, 0), guess_Counts.get(c, 0)) for c in guess_Counts)
    
    return black_Pegs, white_Pegs

def play_Mastermind():
    print("Welkom bij Mastermind!")
    print("Raad de geheime code van 4 kleuren.")
    print("Mogelijke kleuren: R (rood), G (groen), B (blauw), Y (geel), O (oranje), P (paars)")
    print("Je hebt 10 pogingen.")

    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        valid_Guess = False
        while not valid_Guess:
            guess = input(f"Poging {attempt} - Voer je gok in (bv. RGBY): ").strip().upper()
            if len(guess) != 4:
                print(" Je invoer moet precies 4 tekens lang zijn.")
            elif not all(c in "RGBYOP" for c in guess):
                print(" Alleen de letters R, G, B, Y, O, P zijn toegestaan.")
            else:
                valid_Guess = True

        black, white = get_Feedback(secret_Code, guess)
        print(f" Black pegs (juiste kleur & positie): {black}")
        print(f" White pegs (juiste kleur, verkeerde positie): {white}")

        if black == 4:
            print(f" Gefeliciteerd! Je hebt de code geraden: {''.join(secret_Code)}")
            return

    print(f" Je hebt geen pogingen meer. De juiste code was: {''.join(secret_Code)}")

def test_get_Feedback():
    """Simpele testfunctie voor get_Feedback"""
    print(" Test 1:", get_Feedback(['R','G','B','Y'], 'RGBY'))  
    print(" Test 2:", get_Feedback(['R','G','B','Y'], 'YBGR'))  
    print(" Test 3:", get_Feedback(['R','G','B','Y'], 'RRRR')) 

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y':
        play_Mastermind()
        again = input("Wil je opnieuw spelen? (Y/N): ").strip().upper()
        while again not in ['Y', 'N']:
            again = input("Voer 'Y' of 'N' in: ").strip().upper()
