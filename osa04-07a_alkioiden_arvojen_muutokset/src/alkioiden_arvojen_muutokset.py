# Kirjoita ratkaisu tähän
lista = [1,2,3,4,5]
# Listan voi tehdä myös näin: lista = [i for i in range(5)] >>> Kätevää jos pitää muodostaa massiivisia listoja

while True:
    indeksi = int(input("Anna indeksi: "))
    if indeksi in range(len(lista)):
       # korvaaja = int(input(f"Anna arvo: ({lista.pop(indeksi)})" )) # Tulostaa väärin: Anna arvo (indeksi):
        korvaaja = int(input("Anna arvo: "))
        lista[indeksi] = korvaaja
        print(lista)
    elif indeksi == -1:
        break
    elif indeksi > len(lista)-1:
        print("Virheellinen indeksi. anna olemassa oleva indeksi")

# Malli vastaus
        '''
        lista = [1, 2, 3, 4, 5]
while True:
    indeksi = int(input("Anna indeksi: "))
    if indeksi == -1:
        break
    if indeksi < 0 or indeksi >= len(lista):
        print("Indeksi on listan ulkopuolella")
        continue
    arvo = int(input("Anna arvo: "))
    lista[indeksi] = arvo
    print(lista)
    
        '''
