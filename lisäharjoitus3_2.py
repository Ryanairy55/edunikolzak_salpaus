# Tämä ohjelma tarkistaa lämpötilaa ja ilmankosteusta tomaatille
# Sopiva lämpötila on 22-25 Celsius astetta ja
# sopiva ilmankosteus on 60-80 prosenttia
def lh32():
    lt = int(input("Anna lämpötila (C): "))
    ltstatus = ""
    ik = int(input("Anna ilmankosteus (%): "))
    ikstatus = ""
    if lt < 22:
        ltstatus = "liian alhainen"
    elif (lt >= 22) and (lt <= 25):
        ltstatus = "sopiva"
    else:
        ltstatus = "liian korkea"
    if ik < 60:
        ikstatus = "liian alhainen"
    elif (ik >= 60) and (lt <= 80):
        ikstatus = "sopiva"
    else:
        ikstatus = "liian korkea"
    return "Lämpötila on "+ltstatus+" ja ilmankosteus on "+ikstatus+"."
print(lh32())
