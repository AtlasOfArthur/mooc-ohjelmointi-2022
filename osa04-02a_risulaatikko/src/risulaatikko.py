# kopioi edellisestä tehtävästä funktion viiva koodi tänne.
def viiva(leveys, merkkijono):
    print(merkkijono[0] * leveys)


def risulaatikko(korkeus):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    for _ in range(korkeus):
        viiva(10, "#")

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)
