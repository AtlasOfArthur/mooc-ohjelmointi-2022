# tee ratkaisu tänne
def joulukuusi(koko):
    print("joulukuusi!")

    i = 1
    while i <= koko * 2 - 1:
        tyhjat = " " * ((koko * 2 - i) // 2)
        tahtia = "*" * i
        print(tyhjat + tahtia)
        i += 2

    # Lisätään vielä pohja
    jalka = " " * (koko - 1)
    print(jalka + "*")
    
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    joulukuusi(4)

# Malli vastaus
    '''
    def joulukuusi(korkeus):
    print("joulukuusi!")
    i = 1
    while i <= korkeus:
        tyhjaa = korkeus - i
        tahtia = 2 * i - 1
        print(" " * tyhjaa + "*" * tahtia)
        i += 1
    print(" " * (korkeus - 1) + "*")
    
    ''' 