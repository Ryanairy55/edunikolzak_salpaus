def listaMerkkijonoksi(lista):
    merkkijono = ""
    for i in range(0,len(lista)-1):
        merkkijono += str(i) + ", " # ensimmäisesta viidenteen
    merkkijono = merkkijono[:len(merkkijono)-2] # poista ", "-merkkijonot
    merkkijono += " ja " + str(lista[len(lista)-1]) # lisää viimeisen merkkijonon listasta
    return merkkijono
testilista = [1,2,3,4,5,6]
print(listaMerkkijonoksi(testilista)) # tulostaa 1, 2, 3, 4, 5 ja 6
