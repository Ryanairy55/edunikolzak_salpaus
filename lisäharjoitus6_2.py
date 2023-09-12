pelinumerot = [1,4,7,11,22,23,32]
oikeat = [1,6,11,22,29,33,35]
def tarkistaLotto(pelinumerot, oikeat):
    count = 0 # oikeiden numerojen määrä
    for pelinumero in pelinumerot:
        count += oikeat.count(pelinumero) # se lisää oikeiden numerojen määrän
    return count
print(tarkistaLotto(pelinumerot, oikeat)) # tulostaa 3
