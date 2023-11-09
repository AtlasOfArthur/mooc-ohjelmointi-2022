# kopioi edellisestä tehtävästä funktion viiva koodi tänne.
def viiva(leveys, merkkijono):
    print(merkkijono[0] * leveys)

def risunelio(koko):
    for _ in range(koko):
        viiva(koko, "#")

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)

# Mallivastaus
"""
def viiva(koko, merkki):
    if merkki == "":
        merkki = "*"
    print(merkki[0] * koko)
 
def risunelio(koko):
    i = 0
    while i < koko:
        viiva(koko, "#")
        i += 1
"""