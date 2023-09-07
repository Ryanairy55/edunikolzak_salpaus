eka = int(input("Anna eka luku: "))
toka = int(input("Anna toka luku: "))
print("Luvut ovat "+str(eka)+" ja "+str(toka))
i = 1
while (i <= eka) and (i <= toka):
    if (eka % i == 0) and (toka % i == 0):
        tekija = i
    i += 1
print("Lukujen suurin yhteinen tekijä on "+str(tekija))
i = 1
while True:
    if (i % eka == 0) and (i % toka == 0):
        jaettava = i
        break
    i += 1
print("Lukujen pienin yhteinen jaettava on "+str(jaettava))
