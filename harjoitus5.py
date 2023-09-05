luku = input("Anna biitit: ")
pm = int(input("Anna pyöritysten määrä: "))
ps = input("Anna pyörityksen suunta (vasen/oikea): ")

def pyorittaminen(luku,pm,ps):
    uusiluku = "" # väliaikainen muuttuja
    lp = len(luku) # luvun pituus
    if ps == "vasen":
        for i in range(0,pm):
            uusiluku = luku[1:lp] + luku[0]
            luku = uusiluku
    elif ps == "oikea":
        for i in range(0,pm):
            uusiluku = luku[lp-1] + luku[0:lp-1]
            luku = uusiluku
    return luku

print("Pyöritettynä: "+pyorittaminen(luku,pm,ps))
