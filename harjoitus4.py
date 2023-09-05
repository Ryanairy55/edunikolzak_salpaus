luku = int(input("Anna luku: "))
def onkoAlkuLuku():
    for i in range(2, luku - 1):
        if luku % i == 0:
            return False
    return True
if onkoAlkuLuku() == True:
    print("Luku on alkuluku")
else:
    print("Luku ei ollut alkulu")
