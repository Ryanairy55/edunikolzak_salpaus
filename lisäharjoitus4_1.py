from random import randint
luku = randint(1, 10) # Arpoo luvun 1 ja 10 väliltä

a = True # käyttäjän pitää arvioida luvun
while a: # kun a on True
    usernumber = int(input("Arvaa luku: "))
    if usernumber > luku:
        print("Luku on pienempi!")
    elif usernumber < luku:
        print("Luku on suurempi!")
    else:
        print("Oikein!")
        a = False # a on False, käyttäjän ei enää kannatta arvioida lukua
