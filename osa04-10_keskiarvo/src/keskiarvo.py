# tee ratkaisu tänne
def keskiarvo(lista):
    if not lista:
        return 0  # Palauttaa 0, jos lista on tyhjä välttääksemme jakolaskun nollalla
    return sum(lista) / len(lista)
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = keskiarvo(lista) 
    print(tulos)
