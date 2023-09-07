def poistaDuplikaatit(lista):
    uusiLista = [] # lista ilman duplikaatioita
    for i in lista:
        if uusiLista.count(i) != 1: # jos listassa ilman duplikaatiota ei ole samaa merkkijonoa/lukua
            uusiLista.append(i) # lisää sen listaan
    return uusiLista
lista = ["Petra", "Heidi", "Janne", "Petra", "Heidi", "Petra", 
"Petra"]
print(poistaDuplikaatit(lista))
