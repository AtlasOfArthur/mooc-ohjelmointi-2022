# tee ratkaisu tänne
def muotoile(liukuluvut):
    muotoillut = [f'{luku:.2f}' for luku in liukuluvut]
    return muotoillut

# Malli vastaus
'''
def muotoile(lista: list):
    tulos = []
 
    for luku in lista:
        tulos.append(f"{luku:.2f}")
 
    return tulos

'''


if __name__ == "__main__":
    lista = [1.234, 0.3333, 0.11111, 3.446]
    muotoiltuLista = muotoile(lista)
    print(muotoiltuLista)