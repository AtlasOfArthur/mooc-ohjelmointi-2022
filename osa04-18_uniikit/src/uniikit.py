# tee ratkaisu tänne
def uniikit(lista):
    uniikit_luvut = []
    for luku in lista:
        if luku not in uniikit_luvut:
            uniikit_luvut.append(luku)
    return sorted(uniikit_luvut)

if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
  #  print(uniikit(lista))