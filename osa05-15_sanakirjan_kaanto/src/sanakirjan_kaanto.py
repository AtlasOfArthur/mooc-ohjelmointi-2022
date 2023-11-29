# tee ratkaisu tänne
def kaanna(sanakirja: dict):
    kaannetty_sanakirja = {}
    
    for avain, arvo in sanakirja.items():
        kaannetty_sanakirja[arvo] = avain
    
    sanakirja.clear()
    sanakirja.update(kaannetty_sanakirja)

# Malli ratkaisu
'''
def kaanna(sanakirja: dict):
	kopio = {}
	for avain in sanakirja:
		kopio[avain] = sanakirja[avain]
	for avain in kopio:
		del sanakirja[avain]
	for avain in kopio:
		sanakirja[kopio[avain]] = avain

'''
if __name__ == "__main__":
    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)