# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
def viiva(viivankoko, merkkijono):
    if merkkijono == "": # Jos merkkijono on tyhjä, määrittää merkkijonoksi *
        merkkijono = "*" # en kyllä tiedä miten tarpeellinen tämä on, kun toimii ilmankin
    print(merkkijono[0] * viivankoko)

# Määritellään funktio kolmio, joka käyttää while-silmukkaa
def kuvio(koko, merkki1, koko2, merkki2):
    i = 1  # Alustetaan laskuri i yhdellä, koska ensimmäisen rivin leveys on 1
    while i <= koko:  # Silmukka jatkuu niin kauan kuin laskuri ei ole suurempi kuin annettu koko
        viiva(i, merkki1)  # Kutsutaan viiva-funktiota tulostamaan yksi rivi risuaitoja
        i += 1  # Kasvatetaan laskuria yhdellä, jotta siirrytään seuraavalle riville

    j = 1  # Alustetaan toinen laskuri j yhdellä
    while j <= koko2:  # Silmukka jatkuu niin kauan kuin laskuri ei ole suurempi kuin annettu korkeus
        viiva(koko, merkki2)  # Kutsutaan viiva-funktiota tulostamaan yksi rivi toista merkkiä
        j += 1  # Kasvatetaan toista laskuria yhdellä, jotta siirrytään seuraavalle riville

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kuvio(10, "^Ylänuoli", 4, "Iiiii")
# ottaa ekan merkin, koska: merkkijono[0] < indeksi 0


#Malli vastaus:

'''
def viiva(koko, merkki):
    if merkki == "":
        merkki = "*"
    print(merkki[0] * koko)
 
def kuvio(y_korkeus, y_merkki, a_korkeus, a_merkki):
    i = 1
    while i <= y_korkeus:
        viiva(i, y_merkki)
        i += 1
    i = a_korkeus
    while i > 0:
        viiva(y_korkeus, a_merkki)
        i -= 1

'''