# tee ratkaisu tänne
def pisin_naapurijono(lista):
    pituus = 1
    pituus_tilapainen = 1

    for indx in range(1, len(lista)):
        if lista[indx] == lista[indx - 1] + 1 or lista[indx] == lista[indx - 1] - 1:
            pituus_tilapainen += 1
        else:
            pituus_tilapainen = 1

        if pituus_tilapainen > pituus:
            pituus = pituus_tilapainen

    return pituus

if __name__ == "__main__":
    lista = [1, 5, 4, 3, 4, 2, 5, 7, 6, 5, 6, 3, 4, 5, 6, 1, 0, 1, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 6, 7, 10, 11, 10] 
    print(pisin_naapurijono(lista))                     # ^-------------------15--------------------^
                                                                       # Johan tajusin