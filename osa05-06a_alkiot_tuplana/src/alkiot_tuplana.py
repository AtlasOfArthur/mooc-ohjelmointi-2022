# tee ratkaisu tänne
def tuplaa_alkiot(luvut):
    tuplattu_lista = []
    for alkio in luvut:
        tuplattu_lista.append(alkio *2)
    return tuplattu_lista

# Voisi toteuttaa myös näin: (käyttäen comprehension metodia)
'''
def tuplaa_alkiot(luvut):
    return [alkio * 2 for alkio in luvut]

'''
# tai
'''
def tuplaa_alkiot(luvut):
    tuplattu_lista = [alkio * 2 for alkio in luvut]

'''
# Comprehension-menetelmä palauttaa suoraan uuden listan, joten erillistä return-lauseketta ei välttämättä tarvita.
# Tämä johtuu siitä, että comprehension-menetelmä itsessään luo uuden listan ja palauttaa sen.

# Malli vastaus
'''
def tuplaa_alkiot(luvut: list):
    tupla = luvut[:]
    for i in range(len(tupla)):
        tupla[i] *= 2
    
    return tupla

'''

if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)