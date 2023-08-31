# Tämä ohjelma kysyy käyttäjältä neljä lukua (x1, y1,x2, y2)
# ja laskee niiden perusteella pisteiden (x1, y2) ja (x2, y2)
# välisen janan pituuden kaavalla
print("Anna x1")
x1 = int(input())
print("Anna y1")
y1 = int(input())
print("Anna x2")
x2 = int(input())
print("Anna y2")
y2 = int(input())
pituus = ((x2-x1)**2+(y2-y1)**2)**0.5
print(pituus)
