# tee ratkaisu tänne 

def pisimman_pituus(lista):
    pisimman_pituus = 0
    
    for sana in lista:
        sananpituus = len(sana)
        if sananpituus > pisimman_pituus:
            pisimman_pituus = sananpituus
    return pisimman_pituus 


# Malli vastaus (toimii myös, mutta ei ollut niin helppo ymmärtää kuin oma versioni)
'''
def pisimman_pituus(pituus: list):
    pisin = 0
 
    for nimi in pituus:
        if len(nimi) > pisin:
          pisin = len(nimi)
 
    return pisin

'''

if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
    print(pisimman_pituus(lista))
