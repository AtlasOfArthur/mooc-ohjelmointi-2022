# Tee ohjelma, joka kysyy käyttäjältä, mikä editori on käytössä.
# Ohjelma jatkaa, kunnes vastaus on Visual Studio Code.

while True:
    editori = input("Editori: ")
    if editori.lower() == "visual studio code":
        print("loistava valinta!")
        break
    elif editori.lower() in ["word", "notepad"]:
        print("surkea")
    else:
        print("ei ole hyvä") 
