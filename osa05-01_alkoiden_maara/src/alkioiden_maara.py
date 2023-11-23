# tee ratkaisu tänne
def laske_alkiot(matriisi: list, alkio: int):
    maara = 0
    for rivi in matriisi:
        for elementti in rivi:
            if elementti == alkio:
                maara += 1
    return maara




if __name__ == "__main__":
      # ↓------------Matriisi-----------↓
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    #    ↑--Rivi-↑   ↑-Alkio (elementti)
    print(laske_alkiot(m, 1))
    vastaus = laske_alkiot(m, 1)
    print(vastaus)