#
# VERSIO 1 manuaalinen
#

def rot13vaihda(kirjain): # tämä funktio vaihtaa kirjaimen rot13:n perusteella
    if kirjain == "a":
        return "n"
    if kirjain == "b":
        return "o"
    if kirjain == "c":
        return "p"
    if kirjain == "d":
        return "q"
    if kirjain == "e":
        return "r"
    if kirjain == "f":
        return "s"
    if kirjain == "g":
        return "t"
    if kirjain == "h":
        return "u"
    if kirjain == "i":
        return "v"
    if kirjain == "j":
        return "w"
    if kirjain == "k":
        return "x"
    if kirjain == "l":
        return "y"
    if kirjain == "m":
        return "z"
    if kirjain == "n":
        return "a"
    if kirjain == "o":
        return "b"
    if kirjain == "p":
        return "c"
    if kirjain == "q":
        return "d"
    if kirjain == "r":
        return "e"
    if kirjain == "s":
        return "f"
    if kirjain == "t":
        return "g"
    if kirjain == "u":
        return "h"
    if kirjain == "v":
        return "i"
    if kirjain == "w":
        return "j"
    if kirjain == "x":
        return "k"
    if kirjain == "y":
        return "l"
    if kirjain == "z":
        return "m"
    return kirjain # jos ei mitään ole vaihdettu
def rot13(sana):
    uusisana = ""
    for i in range(0, len(sana)):
        uusisana += rot13vaihda(sana[i])
    return uusisana
v1 = str(input("Kirjoita sana (v1): "))
print(rot13(v1))
#
# VERSIO 2 (codecs käyttäen)
#
import codecs
v2 = str(input("Kirjoita sana (v2): "))
print(codecs.encode(v2, 'rot_13'))
