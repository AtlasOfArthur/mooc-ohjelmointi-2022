# tee ratkaisu tänne
def summa(lista1, lista2):
    tulos = []
    for i in range(len(lista1)):
        tulos.append(lista1[i] + lista2[i])
    return tulos

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    tulos = summa(a, b)
    print(tulos)

# Toinen vaihtoehto olisi hyödyntää zip funktiota:

'''
def summa(lista1, lista2):
    tulos = []
    for a, b in zip(lista1, lista2):
        tulos.append(a + b)
    return tulos

'''
# malli vastaus oli epäselvä, joten siistin siitä oman version (Yllä) 
''' 'zip' funktiota ei selitetty missään, joten tässä selitys:

'zip' on Pythonin sisäänrakennettu funktio, joka yhdistää kaksi (tai useampia) listaa
tai muita iteroitavia objekteja pareiksi.
Se muodostaa uuden listan, jossa jokainen alkio on muodostettu
vastaavien alkioden parista alkuperäisistä listoista.

a = [1, 2, 3]
b = ['a', 'b', 'c']

[(1, 'a'), (2, 'b'), (3, 'c')]

Voit nähdä, että zip on yhdistänyt vastaavat elementit listoista a ja b
pareiksi, eli tupleiksi. 
Tätä voidaan käyttää tehokkaasti esimerkiksi silloin,
kun haluat käydä läpi kaksi listaa samanaikaisesti.


'''