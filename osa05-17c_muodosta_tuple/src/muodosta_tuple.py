# tee ratkaisu tänne
def tee_tuple(x: int, y: int, z: int):
    pienin = min(x, y, z)
    suurin = max(x, y, z)
    summa = x + y + z
    
    return (pienin, suurin, summa)


if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))