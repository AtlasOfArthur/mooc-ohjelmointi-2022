# tee ratkaisu tänne
def ilman_vokaaleja(merkkijono):
    vokaalit = "aeiouyåäö"
    vokaaliton_jono = "".join([merkki for merkki in merkkijono if merkki.lower() not in vokaalit]) # Lisää kunkin merkkijonossa olevan merkin vokaalittomaan merkkijonoon, jos merkki ei esiinny vokaalit muuttujassa
    return vokaaliton_jono

# Malli vastaus
'''
def ilman_vokaaleja(mjono: str):
    vokaalit = "aeiouyåäö"
    tulos = ""
 
    for kirjain in mjono:
        if kirjain not in vokaalit:
            tulos += kirjain
 
    return tulos

'''


if __name__ == "__main__":
    jono = "tämä on merkillinen esimerkki.. koska esimerkissä on merkkejä!"
    '''
    vokaaliton = ilman_vokaaleja(jono)
    print(vokaalitons)
    '''
    print(ilman_vokaaleja(jono))