# tee ratkaisu tänne
def eniten_kirjainta(merkkijono):
    eniten_esiintyva_kirjain = merkkijono[0]
    eniten_esiintymiset = merkkijono.count(eniten_esiintyva_kirjain)

    for kirjain in merkkijono:
        if merkkijono.count(kirjain) > eniten_esiintymiset:
            eniten_esiintyva_kirjain = kirjain
            eniten_esiintymiset = merkkijono.count(kirjain)

    return eniten_esiintyva_kirjain


# Malli vastaus
'''
def eniten_kirjainta(mjono: str):
    yleisin = mjono[0]
    for kirjain in mjono:
        if mjono.count(kirjain) > mjono.count(yleisin):
            yleisin = kirjain
 
    return yleisin

'''



if __name__ == "__main__":
    jono = "esimerkkkkimerkkkkijonokkkki"
    print(eniten_kirjainta(jono))