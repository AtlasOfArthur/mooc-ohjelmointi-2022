# tee ratkaisu tänne
def histogrammi(m_jono: str):
    kirjain_laskuri = {}
    
    # Laske kaikkien kirjainten esiintymät
    for kirjain in m_jono:
        if kirjain in kirjain_laskuri:
            kirjain_laskuri[kirjain] += 1
        else:
            kirjain_laskuri[kirjain] = 1
    
    # Tulostaa histogrammin
    for kirjain, lkm in kirjain_laskuri.items():
        print(f"{kirjain} {'*' * lkm}")

# Malli vastaus
'''
def histogrammi(merkkijono: str):
    merkit = {}
    for merkki in merkkijono:
        if not merkki in merkit:
            merkit[merkki] = 0
        merkit[merkki] += 1
 
    for merkki, lkm in merkit.items():
        tahdet = "*"*lkm
        print(f"{merkki} {tahdet}")

'''

if __name__ == "__main__":
    histogrammi("digitaalibanaanikauppias")