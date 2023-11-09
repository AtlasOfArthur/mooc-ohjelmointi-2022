# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(leveys, merkkijono):
    print(merkkijono[0] * leveys)
    
# Määritellään funktio kolmio, joka käyttää while-silmukkaa
def kolmio(koko):
    i = 1  # Alustetaan laskuri i yhdellä, koska ensimmäisen rivin leveys on 1
    while i <= koko:  # Silmukka jatkuu niin kauan kuin laskuri ei ole suurempi kuin annettu koko
        viiva(i, "#")  # Kutsutaan viiva-funktiota tulostamaan yksi rivi risuaitoja
        i += 1  # Kasvatetaan laskuria yhdellä, jotta siirrytään seuraavalle riville

"""
Jokaisen silmukan aikana i kasvaa yhdellä,
mikä tarkoittaa sitä, että jokaisella kierroksella viiva-funktiota kutsutaan kasvaneella leveydellä.
    Ensimmäisellä silmukalla i on 1, toisella silmukalla se on 2, ja niin edelleen. 
Näin ollen tulostetaan risuaitakolmio, jossa jokainen rivi on yhden merkin leveämpi kuin edellinen.

"""


# testataan funktiota
if __name__ == "__main__":
    kolmio(5)

# Malli vastaus
'''
def viiva(koko, merkki):
    if merkki == "":
        merkki = "*"
    print(merkki[0] * koko)
 
def kolmio(koko):
    i = 0
    while i < koko:
        i += 1
        viiva(i, '#')

'''