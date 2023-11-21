# tee ratkaisu tänne
def poista_isot(lista):
    uusimerkkijono_lista = [merkkijono for merkkijono in lista if not merkkijono.isupper()] # lisää merkkijonon (jos ei ole) täysin isoista kirjaimista koostuva
    return uusimerkkijono_lista


# Malli vastaus
'''
def poista_isot(merkkijonot: list):
    ilman_isoja = []
 
    for merkkijono in merkkijonot:
        if not merkkijono.isupper():
            ilman_isoja.append(merkkijono)
 
    return ilman_isoja

'''

if __name__ == "__main__":
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    uusi_lista = poista_isot(lista)
    print(uusi_lista)