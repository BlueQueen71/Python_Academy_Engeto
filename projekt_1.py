'''
author = BlueQueen71
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

ODDELOVAC = "-" * 79
registrovani = {
    "bob": "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

print(
    ODDELOVAC,
    "Vítejte v aplikaci textový analyzátor. Prosím přihlaste se:",
    sep="\n",
)
prihlasovaci_jmeno = input("Přihlašovací jméno: ")
heslo = input("Heslo: ")

if registrovani.get(prihlasovaci_jmeno) != heslo:
    print(
        "PŘÍSTUP ODEPŘEN!",
        "Neplatné uživatelské jméno nebo heslo.",
        sep="\n",
    )
    quit()
else:
    print(ODDELOVAC)

print("Máme zde 3 texty, které se dají analyzovat.")
vyber_textu = int(input("Zvolte si prosím číslo 1 až 3: "))
print(ODDELOVAC)

text = TEXTS[vyber_textu - 1]
rozdelit_text = text.split()

slova = []

for slovo in rozdelit_text:
    slovo = slovo.strip(".,")
    slova.append(slovo)

print(f"Počet slov ve vybraném textu: {len(slova)}.")

zacina_velkym_pismem = 0
slova_psana_velkymi_pismeny = 0
slova_psana_malymi_pismeny = 0
cisla = 0
cetnost_delek_slov = {}
soucet_cisel = 0

for slovicko in slova:
    if slovicko.istitle():
        zacina_velkym_pismem += 1
    elif slovicko.isupper():
        slova_psana_velkymi_pismeny += 1
    elif slovicko.islower():
        slova_psana_malymi_pismeny += 1
    elif slovicko.isnumeric():
        cisla += 1
        soucet_cisel = soucet_cisel + float(slovicko)

    lenght = len(slovicko)
    cetnost_delek_slov[lenght] = cetnost_delek_slov.get(lenght, 0) + 1

print(
    f"Počet slov začínajících velkým písmenem: {zacina_velkym_pismem}.",
    f"Počet slov napsaných velkými písmeny: {slova_psana_velkymi_pismeny}.",
    f"Počet slov napsaných malými písmeny: {slova_psana_malymi_pismeny}.",
    f"Počet slov napsaných číslicemi: {cisla}.",
    ODDELOVAC,
    sep="\n",
)

delka_slov = sorted(cetnost_delek_slov)

for i, delka in enumerate(delka_slov):
    delka = delka_slov[i]
    frekvence = cetnost_delek_slov[delka]

    str_delka = " " + str(delka) if len(str(delka)) == 1 else str(delka)

    print(str_delka, "*" * frekvence, frekvence)

print(
    ODDELOVAC,
    f"Když sečteme všechna čísla ve vybraném textu dostaneme: {soucet_cisel}.",
    ODDELOVAC,
    sep="\n",
)