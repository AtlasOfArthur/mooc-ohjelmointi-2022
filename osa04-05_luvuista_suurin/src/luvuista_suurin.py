# tee ratkaisu tänne
def luvuista_suurin(luku1, luku2, luku3):
    if luku1 > luku2 and luku1 > luku3:
        return luku1
    elif luku2 > luku1 and luku2 > luku3:
        return luku2
    elif luku3 > luku1 and luku3 > luku2:
        return luku3
    elif luku1 == luku2 == luku3:
        return luku1
    elif luku1 > luku2 == luku3:
        return luku1
    elif luku1 < luku2 == luku3:
        return luku3
    elif luku1 == luku3 < luku2:
        return luku2
    elif luku1 == luku3 > luku2:
        return luku1
    elif luku1 == luku2 < luku3:
        return luku3
    elif luku1 == luku2 > luku3:
        return luku1
    
    
    
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    suurin = luvuista_suurin(1, 2, 2)
    print(suurin)

# Malli vastaus

'''
def luvuista_suurin(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

'''
