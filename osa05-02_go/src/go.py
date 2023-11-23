# tee ratkaisu tänne
def kumpi_voitti(pelilauta):
    pelaaja1_pisteet = 0
    pelaaja2_pisteet = 0

    for rivi in pelilauta:
        for alkio in rivi:
            if alkio == 1:
                pelaaja1_pisteet += 1
            elif alkio == 2:
                pelaaja2_pisteet += 1

    if pelaaja1_pisteet > pelaaja2_pisteet:
        return 1
    elif pelaaja1_pisteet < pelaaja2_pisteet:
        return 2
    else:
        return 0
    

if __name__ == "__main__":
    pelilauta = [
    [1, 2, 1, 2],
    [2, 1, 2, 1],
    [1, 2, 1, 0],
    [0, 2, 0, 1]
    ]
    voittaja = kumpi_voitti(pelilauta)
    print(f"Voittaja: Pelaaja {voittaja}")