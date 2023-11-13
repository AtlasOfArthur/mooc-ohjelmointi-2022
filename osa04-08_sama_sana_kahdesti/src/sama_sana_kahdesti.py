# Kirjoita ratkaisu tähän
sanat = []

while True:
    sana = input("sana: ")

    if sana in sanat:
        break
    
    sanat.append(sana)

eri_sanat = list(set(sanat))
print(f"Annoit {len(sanat)} eri sanaa")