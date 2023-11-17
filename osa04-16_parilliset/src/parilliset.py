# tee ratkaisu tänne
def parilliset(lista):
    return [luku for luku in lista if luku % 2 == 0]

if __name__ == "__main__":
    lista = [4, -2, 21, -4, 7, 3, 8 ]
    uusi_lista = parilliset(lista)
    print("alkuperäinen", lista)
    print("uusi", uusi_lista)