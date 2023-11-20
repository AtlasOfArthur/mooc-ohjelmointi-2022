# tee ratkaisu tänne
def pisimmat(lista):
    pisimmat_sanat = []
    pisimman_pituus = 0

    for sana in lista:
        sananpituus = len(sana)
        if sananpituus > pisimman_pituus:
            pisimmat_sanat = [sana]
            pisimman_pituus = sananpituus
        elif sananpituus == pisimman_pituus:
            pisimmat_sanat.append(sana)

    return pisimmat_sanat

# Malli vastaus
'''
def pisimmat(nimet: list):
    tulos = []
 
    for nimi in nimet:
        if tulos == [] or len(nimi) > len(tulos[0]):
            tulos = [nimi]
        elif len(nimi) == len(tulos[0]):
            tulos.append(nimi)
 
    return tulos

'''

if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani", "Arthur"]
    print(pisimmat(lista))