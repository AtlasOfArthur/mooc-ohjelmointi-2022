# tee ratkaisu tänne
def eka_sana(lause):
    sana = lause.split()  # Jakaa lauseen sanoihin välilyönnin perusteella
    return sana[0]   # Palauttaa ensimmäisen sanan

def toka_sana(lause):
    sana = lause.split()
    return sana[1]   # Palauttaa toisen sanan

def vika_sana(lause):
    sana = lause.split()
    return sana[-1]   # Palauttaa viimeisen sanan


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lause = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(lause))
    print(toka_sana(lause)) 
    print(vika_sana(lause))