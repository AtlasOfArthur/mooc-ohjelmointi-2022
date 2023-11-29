# tee ratkaisu tänne
def vanhin(henkilot: list):
    vanhin_henkilo = None
    
    for henkilo in henkilot:
        if vanhin_henkilo is None or henkilo[1] < vanhin_henkilo[1]:
            vanhin_henkilo = henkilo
    
    return vanhin_henkilo[0] if vanhin_henkilo is not None else None

if __name__ == "__main__":
    h1 = ("Arto", 1977)   # Tuplen voi tehdä myös näin: tuple = "Arto", 1977, 
    h2 = ("Einari", 1985) # Eli ilman sulkuja. Riittää että loppuun lisää vain pilkun.
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]

    print(vanhin(hlista))