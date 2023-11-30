# tee ratkaisu tänne

def suurin():
    try:
        with open ("luvut.txt") as numerotiedosto:
            suurin_luku = float('-inf') # Alustetaan äärettömällä negatiivisella luvulla, koska mikä tahansa luku voi olla tätä suurempi.
            # Olisin myös voinut listata kaikki tiedostossa olevat luvut tpleen 
            # (Ps. tuple on listaa ~10 kertaa nopeampi. Materiaalissa ei kerrottu tätä ja se on suurin syy miksi tupleja käytetään. Se vie myös puolet vähemmän muistia.)
            '''
            luvut = tuple(int(rivi) for rivi in tiedosto)
            if luvut:
                suurin_luku = luvut[0]
                for luku in luvut[1:]:
                    '''
            # Mutta valitsemani vaihtoehto on parempi

            for rivinluku in numerotiedosto:
                muunnettu_luku = int(rivinluku) # Tiedostosta luetut luvut ovat oletuksena muodossa ('str'), siksi on hyvä muuntaa ne muotoon ('int')
                if muunnettu_luku > suurin_luku:
                    suurin_luku = muunnettu_luku

            return suurin_luku

    except FileNotFoundError:
        print("Tiedostoa 'luvut.txt' ei löytynyt.")
        return None
    except Exception as e:
        print(f"Virhe tiedoston käsittelyssä: {e}")
        return None
    
if __name__ == "__main__":
    print(suurin())