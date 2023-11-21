# tee ratkaisu tänne
def pisin_naapurijono(lista):
    pituus = 1
    pituus_tilapainen = 1

    for indx in range(1, len(lista)):
        if lista[indx] == lista[indx - 1] + 1:
            pituus_tilapainen += 1
        else:
            pituus_tilapainen = 1

        if pituus_tilapainen > pituus:
            pituus = pituus_tilapainen

    return pituus

if __name__ == "__main__":
    lista = [1, 2, 3, 5, 6, 7, 6, 5, 6, 7, 10, 11, 10] # antaa virheen: Tulos 3 ei vastaa mallivastausta 7 testisyötteellä (1, 2, 3, 5, 6, 7, 6, 5, 6, 7, 10, 11, 10)
    print(pisin_naapurijono(lista))                    # Silmämääräisesti katsomalla listaa, vastaus 3 on oikein, tai sitten en tajua jotain oleellista...
                                                       # Epäilen jo virhettä tarkistuksessa!