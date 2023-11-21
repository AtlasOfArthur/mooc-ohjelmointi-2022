# tee ratkaisu tänne
def kaikki_vaarinpain(merkkijono_lista): 
    '''
    kaikki_vaarinpain = [merkki[::-1] for merkki in merkkijono_lista] ''' # Tuottaa tuloksen: ['ioM', 'ikkiak', 'ikkremise', 'isky äleiv']
    # Selvisi juuri, että tätä^ kutsutaan 'comprehension'-rakenteeksi
    kaikki_vaarinpain = [merkki[::-1] for merkki in reversed(merkkijono_lista)] # reversed korjaa tilanteen
    return kaikki_vaarinpain

# Malli vastaus
'''
def kaikki_vaarinpain(lista: list):
    uusi = []
    for mjono in lista:
        uusi.append(mjono[::-1])
    return uusi[::-1]

'''
# Halusin käyttää comprehension rakenteessa .append metodia, mutta: 
'''
Valitettavasti comprehension-rakenteessa ei voida suoraan käyttää append-metodia,
sillä comprehension on suunniteltu luomaan uusi lista suoraan.
Comprehensionissa on omat syntaksinsa, 
eikä siihen ole mahdollista lisätä append-metodia.

'''

if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)