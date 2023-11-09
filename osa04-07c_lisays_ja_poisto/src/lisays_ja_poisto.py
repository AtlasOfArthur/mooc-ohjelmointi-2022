# Kirjoita ratkaisu tähän
lista = []
userInput = ""
laskija = 1

while True:
    print(f"Lista on nyt {lista}" )
    userInput = input("(l)isää, (p)oista vai e(x)it: ")

    if userInput == 'l':
        if len(lista) >= 0:
            lista.append(laskija)
            laskija += 1
    elif userInput == 'p':
        if len(lista) > 0:
            lista.pop()
            laskija -= 1
    elif userInput == 'x':
        print("Moi!")
        break

# Malli vastaus
    '''
    lista = []
while True:
    print(f"Lista on nyt {lista}")
    valinta = input("(l)isää, (p)oista vai e(x)it:")
    if valinta == "l":
        # alkion arvo on listan pituus + 1
        alkio = len(lista) + 1
        lista.append(alkio)
    elif valinta == "p":
        lista.pop(len(lista) - 1)
    elif valinta == "x":
        break
 
print("Moi!")

    '''