# Tämä ohjelma laskee 4 merkkiä pitkän binääriluvusta desimaaliluvun
bl = str(input("Anna 4-bittinen binääriluku: "))
luku = 0
if len(bl) != 4:
    print("Syötteesi ei ollut nelimerkkinen.")
else:
    i = 3
    a = 1
    while i != -1:
        if (bl[i] != "1") and (bl[i] != "0"):
            print("Luku ei ole binääri")
            break
        else:
            luku += a * int(bl[i])
            a *= 2
            i -= 1
print(luku)
