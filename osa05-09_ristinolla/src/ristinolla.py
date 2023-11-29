# tee ratkaisu tänne
def pelaa_siirto(lauta, x, y, nappula):
    if 0 <= x < 3 and 0 <= y < 3: # Tarkistaa sallittu alue (indeksit 0-2)
        if lauta [y][x] == "": # Tarkistetaan onko koordinaatti tyhjä
            lauta[y][x] = nappula # Jos on, asetetaan nappula y-x koordinaattiin

            return True
            
    return False

# Malli vastaus
'''
def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
    if x < 0 or y < 0 or x > 2 or y > 2:
        return False
 
    # Huomaa, että y-koordinaatti annetaan ensin
    if lauta[y][x] == "":
        lauta[y][x] = nappula
        return True
 
    return False

'''

if __name__ == "__main__":
    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta, 1, 1, "X")) # Kaskelle tietty, koska se on paras aloitus siirto!
    print(lauta)
    print(pelaa_siirto(lauta, 0, 1, "O"))
    print(lauta) # Lisätty varmistamaan, ettei rivit ja sarakkeet mene ristiin