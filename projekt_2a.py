import random

def predstaveni():
    print("""
    Hi there!,
    I've generated a secret random 4 digit number for you.
    Your task is to guess, what number it is.
    Enter a 4 digit number where 
        * the digits will not repeat and
        * the number can't begin with 0.
    If the matching digits:
        * are in their right positions, they are "bulls", 
        * if in different positions, they are "cows".
    Try to guess what number I'm thinking of.
    """)

def generace_cisla(delka):
    cislo = " "

    while len(set(cislo)) != delka and cislo[0] != 0:
        cislo = str(random.randint(1000,9999))

    return cislo

def spatny_vstup(inp):
    vysledek = False

    if not inp.isnumeric() or len(inp) != 4:
        vysledek = True

    if inp.startswith("0"):
        vysledek = True

    if len(set(inp)) != 4:
        vysledek = True

    if vysledek == True:
        print("""
        Please enter a whole 4-digit number.
        Please enter a number not repeating the digits.
        The number can't start with 0.
        """)

    return vysledek

def pocitat_bulls_cows(inp, nahodne_cislo):
    bulls = cows = 0

    for index, cisl in enumerate(inp):
        if cisl == nahodne_cislo[index]:
            bulls += 1

        elif cisl in nahodne_cislo:
            cows += 1

    return bulls, cows

def ukonceni_hry(bulls, cows, pocet_pokusu):
    konec = False

    if bulls == 4:
        koncovka = "es" if pocet_pokusu > 1 else ""
        print("Game Over, you found it after {} guess{}.".format(pocet_pokusu, koncovka))
        print("That's {}.". format(hodnoceni(pocet_pokusu)))
        konec = True

    else:
        print("| bulls: {} | cows: {} | guesses: {} |".format(bulls, cows, pocet_pokusu))

    return konec

def hodnoceni(pokusy):
    if pokusy <= 5:
        return "amazing"

    elif pokusy <= 10:
        return "good"

    return "not so good"

def main():
    predstaveni()
    pocitac_cislo = generace_cisla(4)
    pocet_pokusu = 0

    while True:
        tvoje_cislo = input("Enter your number: ")
        pocet_pokusu += 1

        if spatny_vstup(tvoje_cislo):
            continue

        bulls, cows = pocitat_bulls_cows(tvoje_cislo, pocitac_cislo)

        if ukonceni_hry(bulls, cows, pocet_pokusu):
            break

main()
