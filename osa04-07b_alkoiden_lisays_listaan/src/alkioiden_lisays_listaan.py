# Kirjoita ratkaisu tähän
lista = [] 


lukumaara = int(input("Kuinka monta lukua: "))
monesko = 1

while lukumaara > 0:
    lisattava = int(input(f"Anna luku {monesko}: "))
    lista.append(lisattava)
    lukumaara -= 1
    monesko +=1

print(lista)

# Malli vastaus
'''
    lukuja = int(input("Kuinka monta lukua: "))
lista = []
 
while len(lista) < lukuja:
    luku = int(input(f"Anna luku {len(lista) + 1}: "))
    lista.append(luku)
 
print(lista)
    
'''