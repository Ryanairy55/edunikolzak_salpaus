# Tämä ohjelma tarkistaa, jos merkkijonot ovat
# toistensa käänteisjonoja
def lh31():
    eka = input("Anna eka merkkijono (4 merkkiä): ")
    if len(eka) != 4:
        return "Eka merkkijonossa ei ole 4 merkkiä."
    toka = input("Anna toka merkkijono (4 merkkiä): ")
    if len(toka) != 4:
        return "Toka merkkijonossa ei ole 4 merkkiä."
    a = 0
    b = 3
    while True:
        if eka[a] == toka[b]:
            a += 1
            b -= 1
        else:
            return "Merkkijonot eivät ole toistensa käänteisjonoja."
        if a == 4:
            return "Merkkijonot ovat toistensa käänteisjonoja!"
print(lh31())
