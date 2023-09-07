def osoitteenTarkistelu(osoite):
    if len(osoite) < 6:
        print("Osoite on liian lyhyt")
        return False
    if osoite.find("@") == -1:
        print("Osoitteessa ei ole @-merkkiä")
        return False
    if osoite[osoite.find("@"):].find(".") == -1:
        print("Osoitteessa ei ole pisteitä @-merkin jälkeen")
        return False
    if len(osoite[osoite.rfind("."):]) <= 2:
        print("asdasdasd")
        return False
    return True


osoite = str(input("Anna osoitteen: "))
print(osoitteenTarkistelu(osoite))
