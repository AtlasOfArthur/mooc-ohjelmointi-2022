# tee ratkaisu tänne
def positiivisten_summa(lista):
    return sum([luku for luku in lista if luku > 0]) # comprehension -rakenne

if __name__ == "__main__":
    lista = [4, -2, 21, -4, 7]
    vastaus = positiivisten_summa(lista)
    print("vastaus", vastaus)

    # Perinteinen tapa ja malli

    '''
    def positiivisten_summa(lista: list):
    summa = 0
    for alkio in lista:
        if alkio > 0:
            summa += alkio
    return summa
    
    '''