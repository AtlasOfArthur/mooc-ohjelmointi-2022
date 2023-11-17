# Tee ratkaisu tänne
def anagrammi(sana1, sana2):
    # Poistaa välilyönnit ja muuta kaikki kirjaimet pieniksi
    sana1 = sana1.replace(" ", "").lower()
    sana2 = sana2.replace(" ", "").lower()

    # Tarkista, ovatko järjestetyt merkkijonot samat
    return sorted(sana1) == sorted(sana2)

if __name__ == "__main__":
    print(anagrammi("talo", "tola")) # True
    print(anagrammi("talo", "lato")) # True
    print(anagrammi("talo", "olat")) # True
    print(anagrammi("tammi", "mitta")) # False
    print(anagrammi("python", "java")) # False