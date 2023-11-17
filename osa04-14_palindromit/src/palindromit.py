# tee ratkaisu tänne
def palindromi(sana):
    sana = sana.lower()  # Muutetaan kaikki kirjaimet pieniksi
    sana = sana.replace(" ", "")  # Poistetaan välilyönnit
    return sana == sana[::-1]  # Tarkistetaan, onko sana palindromi käänteisenä

while True:
    käyttäjän_syöte = input("Anna palindromi: ")
    if palindromi(käyttäjän_syöte):
        print(f"{käyttäjän_syöte} on palindromi!")
        break
    else:
        print("ei ollut palindromi")
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!


# Malli vastaus

'''
def palindromi(sana: str):
    for i in range(len(sana)//2):
        if sana[i] != sana[len(sana)-i-1]:
            return False
    return True
 
while True:
    sana = input("Anna sana: ")
    if palindromi(sana):
        print(sana, "on palindromi!")
        break
    print("ei ollut palindromi")

'''