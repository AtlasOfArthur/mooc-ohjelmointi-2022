# Kirjoita ratkaisu tähän
lista = []
sorted_lista =[]
userInput = ""


while True:

    userInput = input("Anna luku: ")
    lista.append(int(userInput))

    if userInput == '0':
        print("Moi!")
        break

    print(f"Lista: {lista}" )
    sorted_lista = sorted(lista)
    print(f"Järjestettynä: {sorted_lista}")

