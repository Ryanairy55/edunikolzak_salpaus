# Tämä ohjelma löytää toisen sanan lauseesta
print("Anna lause: ")
lause = str(input())
raja1 = lause.find(" ")
raja2 = raja1 + 1
while True:
    if lause[raja2] == " ":
        break
    else:
        raja2 += 1
print(lause[raja1:raja2])
