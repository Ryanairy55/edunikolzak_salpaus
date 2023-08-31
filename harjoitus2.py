# Tämä ohjelma pyytää käyttäjältä 2 merkkijonoa a ja b
# ja etsii b:n toisen esiintyämän merkkijonosta a
print("Anna merkkijono: ")
merkkijono = str(input())
print("Anna alijono: ")
alijono = str(input())
numero = merkkijono[merkkijono.find(alijono)+1:(len(merkkijono)-1)].find(alijono)+merkkijono.find(alijono)+1
print("Alijonon " + alijono + " toinen esiintymä löytyy merkkijonosta " + merkkijono + " indeksistä " + str(numero) + " alkaen")
