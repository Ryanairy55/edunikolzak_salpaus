# Tämä ohjelma pyytää käyttäjää syöttämään luvuy a, b ja c
# ja kertoo näiden perusteella onko yhtälöllä
# x=(-b+-(b**2-4*a*c)**0.5)/(2*a)
# nolla, yksi vai kaksi ratkaisua
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = 0
#x1 = (-b-(b**2-4*a*c)**0.5)/(2*a)
#x2 = (-b+(b**2-4*a*c)**0.5)/(2*a)
if a == 0:
    d=0
elif (b**2-4*a*c)**0.5 == 0:
    d=1
else:
    d=2
print(d)
