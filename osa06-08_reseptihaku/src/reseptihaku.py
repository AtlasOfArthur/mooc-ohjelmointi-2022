# Tehdään kaksiulotteinen lista tiedoston sisällöstä

def tiedosto_to_list():
    # Avataan tiedosto ja luetaan sisältö
    with open('reseptit1.txt', 'r') as file:

        # Alustetaan tyhjä lista resepteille
        resepti_lista = []
        # Alusta tyhjä alilista, johon lisätään kukin resepti
        alilista = []

        # Käy tiedosto rivi kerrallaan läpi
        for line in file:
            # Poista rivinvaihto merkki
            line = line.strip()

            # Jos rivi on tyhjä, lisää alilista resepti_listaan ja alusta uusi alilista
            if not line:
                resepti_lista.append(alilista)
                alilista = []
            else:
                # Muussa tapauksessa lisää rivin osat alilistaan
                alilista.append(line)

    # Tulosta lopullinen resepti_lista
    print(resepti_lista)
    return resepti_lista




'''
# Reseptin haku nimen perusteella
def hae_nimi(tiedosto: str, sana: str):
    loydetyt_nimi = []

    try:
        with open(tiedosto, encoding='utf-8') as reseptitiedosto:
            for rivi in reseptitiedosto:
                if sana.lower() in rivi.lower():
                    loydetyt_nimi.append(rivi.strip())

        return loydetyt_nimi

    except FileNotFoundError:
        print(f"Tiedostoa '{tiedosto}'  ei löytynyt.")
        return None
    except Exception as e:
        print(f"Virhe tiedoston '{tiedosto}' käsittelyssä: {e}")
        return None



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

'''
    reseptit = lue_resptit("reseptit1.txt")

    for resepti in reseptit:
        print(resepti)

        

    loydetyt_nimi = hae_nimi("reseptit1.txt", "pulla")

    for resepti in loydetyt_nimi:
        print(resepti)

    loydetyt_aika = hae_aika("reseptit1.txt", 50)

    for resepti in loydetyt_aika:
        print(resepti)

[[Lettutaikina 15, maito, kananmuna, jauho, sokeri, suola, voi],
[Lihapullat, 45, jauheliha, kananmuna, korppujauho],
[Tofurullat, 30, tofu, riisi, vesi, porkkana, kurkku, avokado, wasabi],
[Pullataikina, 60, maito, hiiva, kananmuna, suola, sokeri, kaardemumma, voi]]

'''