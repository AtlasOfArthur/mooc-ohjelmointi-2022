# Määritellään funktio viiva, joka tulostaa merkkijonon ensimmäisen merkin toistettuna leveyden verran
def viiva(leveys, merkkijono):
    print(merkkijono[0] * leveys)

# Määritellään funktio nelio, joka käyttää while-silmukkaa.
def nelio(koko, merkki):
    i = 0  # Alustetaan laskuri i nollaksi
    while i < koko:  # Silmukka jatkuu niin kauan kuin laskuri on pienempi kuin annettu koko
        viiva(koko, merkki)  # Kutsutaan viiva-funktiota tulostamaan yksi rivi neliötä
        i += 1  # Kasvatetaan laskuria yhdellä, jotta siirrytään seuraavalle riville

# Testataan funktiota
if __name__ == "__main__":
    nelio(5, "x")  # Kutsutaan nelio-funktiota, joka piirtää nelion leveydellä 4 ja käyttäen merkkiä 'x'
#     Koko^   ^Merkki