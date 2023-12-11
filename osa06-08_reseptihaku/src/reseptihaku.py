# Tehdään kaksiulotteinen lista tiedoston sisällöstä

def tiedosto_to_list():
    try: # Laitetaan try blockiin koko ohjelma virheiden varalta
        with open('reseptit1.txt', 'r') as file: # Avataan tiedosto ja luetaan sisältö
            resepti_lista = [] # Alustetaan tyhjä lista resepteille
            alilista = [] # Alusta tyhjä alilista, johon lisätään kukin resepti

            
            for line in file: # Käy tiedosto rivi kerrallaan läpi
                line = line.strip() # Poista rivinvaihto merkki

                
                if not line: # Jos rivi on tyhjä, lisää alilista resepti_listaan ja alusta uusi alilista
                    resepti_lista.append(alilista)
                    alilista = [] # Eli siis, kun ylempänä alilista on lisätty resepti_listaan, 'tyhjennetään' alustamalla alilista muuttuja
                else:
                    alilista.append(line) # Muussa tapauksessa lisää rivin osat alilistaan

            resepti_lista.append(alilista)  # Lisätään viimeinen resepti listaan (Jos vaikka korjaisi vian) Yksi resepti puuttui.
        
        # resepti_lista tulostus poistettu, koska testaus tapahtuu nyt alhaalla (Tämä tarkoittaa, että toimii tähän asti)
        return resepti_lista # palautetaan resepti_lista käyttöä varten

    except FileNotFoundError:
        print(f"Tiedostoa 'reseptit1.txt' ei löytynyt.")
        return None
    except Exception as e:
        print(f"Virhe tiedoston 'reseptit1.txt' käsittelyssä: {e}")
        return None



# Nimi perusteinen

def hae_nimi(tiedosto: str, sana: str):
    reseptit = tiedosto_to_list() # Tässä haetaan meidän lista ja tallennetaan se muuttujaan reseptit
    loydetyt_nimi = []            # Tämä osoittautuikin paljon järkevämmäksi ratkaisuksi kuin edellinen

    for resepti in reseptit:
        nimi = resepti[0].lower()  # Haetaan reseptin nimi ja muutetaan pieniksi kirjaimiksi
        if sana.lower() in nimi: # Tarkastetaan, onko sana löytynyt reseptin nimestä
            loydetyt_nimi.append(nimi.strip())

    return loydetyt_nimi



# Aika perusteinen

def hae_aika(tiedosto: str, aika: int):
    reseptit = tiedosto_to_list()
    loydetyt_reseptit = []

    for resepti in reseptit:
      #  print("Alkuperäinen resepti:", resepti)  # Tulosta alkuperäinen resepti

        # Muunnetaan valmistusajat suoraan int-muotoon
        valmistusaika_list = [int(valmistusaika) for valmistusaika in resepti[1].split(', ')]
       # print("Valmistusajat (kokonaisluvut):", valmistusaika_list)  # Tulostaa valmistusajat kokonaislukuina (int)

        for valmistusaika_int in valmistusaika_list:
         #   print("Käsitelty valmistusaika:", valmistusaika_int)

            if valmistusaika_int <= aika:
                nimi = resepti[0]
                valmistusaineet = ", ".join(resepti[2:])  # Ainesosat erotetaan pilkulla toisistaan
                loydetyt_reseptit.append(f"{nimi}, valmistusaika {valmistusaika_int} min")
              #  print("Lisätty löydettyjen reseptien listaan:", f"{nimi}, valmistusaika {valmistusaika_int} min")
            else:
                pass # Valmistusaika ei täyttänyt kriteerejä, ei lisätä löydettyjen reseptien listaan

    return loydetyt_reseptit



if __name__ == "__main__":
# Tarkistan että tiedostosta luotu lista tulostuu oikein
    print(tiedosto_to_list()) # Print oli unohtunut. Ei näy konsolissa ilman sitä 


# Nimi perusteinen   
    loydetyt_nimi = hae_nimi("reseptit1.txt", "tofu")

    for resepti in loydetyt_nimi:
        print(resepti)  # Tulostaa nimen perusteella löydetyt reseptit (pulla)


# Aika perusteinen
    loydetyt = hae_aika("reseptit1.txt", 50) # Arvolla 50 tulostuu 3 reseptiä ja niiden ajat

    for resepti in loydetyt:
        print(resepti)  # Tulostaa haetut reseptit aikaperusteella




    '''
    loydetyt_aika = hae_aika("reseptit1.txt", 50)

    for resepti in loydetyt_aika:
        print(resepti)

    [[Lettutaikina 15, maito, kananmuna, jauho, sokeri, suola, voi],
    [Lihapullat, 45, jauheliha, kananmuna, korppujauho],
    [Tofurullat, 30, tofu, riisi, vesi, porkkana, kurkku, avokado, wasabi],
    [Pullataikina, 60, maito, hiiva, kananmuna, suola, sokeri, kaardemumma, voi]]

    '''