# tee ratkaisu tänne
def samat(merkkijono,index1,index2):
    try:
        return merkkijono[index1] == merkkijono[index2]
    except IndexError:
        return False


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    print(samat("koodari", 1, 2)) 


    # Malli vastaus
    '''
    def samat(mjono, a, b):
    if a >= len(mjono) or b >= len(mjono):
        return False
    return mjono[a] == mjono[b]

    '''
    