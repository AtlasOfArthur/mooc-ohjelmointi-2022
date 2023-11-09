# tee ratkaisu tänne 
def viiva(leveys, merkkijono=""):
    if not merkkijono:
        merkkijono = "*"
    print(merkkijono[0] * leveys)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    leveys = int(input("Anna merkkijonon pituus: "))
    merkkijono = input("Anna merkkijono: ")
    viiva(leveys, merkkijono)
