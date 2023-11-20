# tee ratkaisu tänne
def lyhin(lista):
    lyhin_sana = lista[0] # Alustetaan lyhin sana indeksiin 0
    lyhimman_pituus = len(lyhin_sana) # Alustetaan lyhimmän sanan pituus vastaamaan lyhin_sana muuttujaa

    for sana in lista:     
        if len(sana) < lyhimman_pituus: # Päivittää lyhin_sana muuttujan jos se on lyhyempi kuin edellinen
            lyhin_sana = sana # Tallentaa sanan indeksin muuttujaan sana jos ylläoleva ehto täyttyy
        lyhimman_pituus = len(sana) # Tallentaa sana muuttujan indeksissä olevan sanan pituuden lyhimman_pituus muuttujaan
    return lyhin_sana # Lopulta palauttaa lyhimmän sanan

# malli vastaus
'''
def lyhin(nimet: list):
    tulos = ""
 
    for nimi in nimet:
        if tulos == "" or len(nimi) < len(tulos):
            tulos = nimi
 
    return tulos

'''

if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani", "Ar"]
    print(lyhin(lista))