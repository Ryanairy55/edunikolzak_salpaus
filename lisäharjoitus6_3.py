lukulista = [] # yleinen lukulista
while True:
    luku = int(input("Anna luku: "))
    if luku == 0: # lopetta jos luku on 0
        break
    lukulista.append(luku)
def poistaDuplikaatit(lista):
    uusiLista = [] # lista ilman duplikaatioita
    for i in lista:
        if uusiLista.count(i) != 1: # jos listassa ilman duplikaatiota ei ole samaa merkkijonoa/lukua
            uusiLista.append(i) # lisää sen listaan
    return uusiLista
print("Lista ennen: "+str(lukulista))
print("Lista jälkeen: "+str(poistaDuplikaatit(lukulista))) # lukulista ilan duplikaateja
