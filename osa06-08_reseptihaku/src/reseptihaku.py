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

        
        # resepti_lista tulostus poistettu, koska testaus tapahtuu nyt alhaalla (Tämä tarkoittaa, että toimii tähän asti)
        return resepti_lista # palautetaan resepti_lista käyttöä varten

    except FileNotFoundError:
        print(f"Tiedostoa 'reseptit1.txt' ei löytynyt.")
        return None
    except Exception as e:
        print(f"Virhe tiedoston 'reseptit1.txt' käsittelyssä: {e}")
        return None


# Reseptin haku nimen perusteella
def hae_nimi(tiedosto: str, sana: str):
    reseptit = tiedosto_to_list() # Tässä haetaan meidän lista ja tallennetaan se muuttujaan reseptit
    loydetyt_nimi = []            # Tämä osoittautuikin paljon järkevämmäksi ratkaisuksi kuin edellinen

    for resepti in reseptit:
        for rivi in resepti:
            if sana.lower() in rivi.lower():
                loydetyt_nimi.append(rivi.strip())

        return loydetyt_nimi


'''
# Reseptin haku aika perusteella
def hae_aika(tiedosto: str, aika: int):
    loydetyt_aika = []

    try:
        with open(tiedosto) as reseptitiedosto:
            while True:
                resepti_nimi = reseptitiedosto.readline().strip()
                if not resepti_nimi:  # Tarkista, onko rivi tyhjä (reseptin loppu)
                    break

                valmistusaika_rivi = reseptitiedosto.readline().strip()
                # Tarkista, onko valmistusaika_rivi kelvollinen kokonaisluku
                try:
                    valmistusaika = int(valmistusaika_rivi)  # Muunnetaan valmistusaika kokonaisluvuksi
                except ValueError:
                    # Jos ei ole kelvollinen, siirry seuraavaan reseptiin
                    continue

                if valmistusaika <= aika:
                    loydetyt_aika.append(f"{resepti_nimi}, valmistusaika {valmistusaika} min")

        return loydetyt_aika

    except FileNotFoundError:
        print(f"Tiedostoa '{tiedosto}'  ei löytynyt.")
        return None
    except Exception as e:
        print(f"Virhe tiedoston '{tiedosto}' käsittelyssä: {e}")
        return None
'''



if __name__ == "__main__":
    tiedosto_to_list()
   
    loydetyt_nimi = hae_nimi("reseptit1.txt", "pulla")

    for resepti in loydetyt_nimi:
        print(resepti)
'''
    loydetyt_aika = hae_aika("reseptit1.txt", 50)

    for resepti in loydetyt_aika:
        print(resepti)

[[Lettutaikina 15, maito, kananmuna, jauho, sokeri, suola, voi],
[Lihapullat, 45, jauheliha, kananmuna, korppujauho],
[Tofurullat, 30, tofu, riisi, vesi, porkkana, kurkku, avokado, wasabi],
[Pullataikina, 60, maito, hiiva, kananmuna, suola, sokeri, kaardemumma, voi]]

'''