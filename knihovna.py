import unicodedata


prihlasen = ""


seznam_uzivatelu = {
    1: {"jmeno": "Jana", "heslo": "kocka", "pujcene_knihy": []},
    2: {"jmeno": "Martin", "heslo": "auto", "pujcene_knihy": [ "1984"]},
    3: {"jmeno": "Lucie", "heslo": "strom", "pujcene_knihy": ["velkygatsby"]},
    4: {"jmeno": "Petr", "heslo": "pes", "pujcene_knihy": []},
    5: {"jmeno": "Jirka", "heslo": "sova", "pujcene_knihy":  ["zlocinatrest"]},
    6: {"jmeno": "Hana", "heslo": "leto", "pujcene_knihy": []},
    7: {"jmeno": "Eva", "heslo": "kytka", "pujcene_knihy": ["annakarenina"]},
    8: {"jmeno": "Tomáš", "heslo": "slon", "pujcene_knihy": [ "duna"]},
    9: {"jmeno": "Alena", "heslo": "kava", "pujcene_knihy": ["prideandprejudice"]},
    10: {"jmeno": "Filip", "heslo": "more", "pujcene_knihy": [ "velkygatsby", "hobit"]}
}


seznam_knih = {
    "duna": {"autor": "Frank Herbert", "ISBN": "9780399128967", "pujceno": False},
    "1984": {"autor": "George Orwell", "ISBN": "9780451524935", "pujceno": False},
    "hobit": {"autor": "J.R.R. Tolkien", "ISBN": "9780261103344", "pujceno": False},
    "zlocinatrest": {"autor": "Fjodor Dostojevskij", "ISBN": "9780143058144", "pujceno": True},
    "velkygatsby": {"autor": "F. Scott Fitzgerald", "ISBN": "9780743273565", "pujceno": False},
    "prideandprejudice": {"autor": "Jane Austen", "ISBN": "9781503290563", "pujceno": True},
    "annakarenina": {"autor": "Lev Tolstoj", "ISBN": "9780199232086", "pujceno": False}
}

def odstranit_knihu():
    nazev = input("Zadej název knihy kterou chceš odstranit: ")



def vyhledat():

    global prihlasen


    hledat = input("Zadej název knihy: ")

    text = unicodedata.normalize('NFD', hledat)
    text_bez_diakritiky = ''.join(char for char in text if unicodedata.category(char) != 'Mn')
    text_bez_diakritiky_mala_pismena = text_bez_diakritiky.lower().replace(" ", "")


    if text_bez_diakritiky_mala_pismena in seznam_knih.keys() and seznam_knih[text_bez_diakritiky_mala_pismena]["pujceno"] == False :
        seznam_knih[text_bez_diakritiky_mala_pismena]["pujceno"] = True
        for uzivatel in seznam_uzivatelu.values():
            if uzivatel["jmeno"] == prihlasen:
                uzivatel["pujcene_knihy"].append(text_bez_diakritiky_mala_pismena)
        print("kniha byla půjčena")
        print (seznam_uzivatelu)

    elif text_bez_diakritiky_mala_pismena in seznam_knih.keys() and seznam_knih[text_bez_diakritiky_mala_pismena]["pujceno"] == True:
        print("Tato kniha je bohužel již půjčena")
        return vyhledat()
    elif text_bez_diakritiky_mala_pismena not in seznam_knih.keys():
        print("Takovou knihu tu nemáme")
        return vyhledat()


def menu():
    volba = int(input("[1] Půjčit  knihu [2] Odstranit knihu [3 přidat knihu]: "))
    if volba == 1:
        vyhledat()
    elif volba = 2:
        


def login():
    global prihlasen

    jmeno = input("Zadej své jméno: ")
    heslo = input("Zadej heslo: ")

    for uzivatel in seznam_uzivatelu.values():
        if jmeno == uzivatel["jmeno"] and heslo == uzivatel["heslo"]:
            prihlasen = jmeno
            print("Přihlášení proběhlo úspěšně")
        
    vyhledat()
        
 
    


def register():
    global prihlasen
    jmeno = input("Zadej své jméno: ")

    for uzivatel in seznam_uzivatelu.values():
        if uzivatel["jmeno"] == jmeno:
            print("Toto jméno je již obsazeno")
            return register()
    
    heslo_1 = input("Zadej heslo: ")
    heslo_2 = input("Znovu heslo: ")

    if heslo_1 != heslo_2:
        print("Hesla se neshodují!")
        return register()
    
    else:
        seznam_uzivatelu[len(seznam_uzivatelu) + 1] = {"jmeno": jmeno, "heslo": heslo_1, "pujcene_knihy": []}
        print("registrace proběhla v pořádku")
        print(seznam_uzivatelu)
        
while True:
    volba = int(input("[1] Přihlásit se [2] Zaregistrovat se: "))
    if volba == 1:
        login()
    elif volba == 2:
        register()
    else:
        print("špatná volba")
        continue


