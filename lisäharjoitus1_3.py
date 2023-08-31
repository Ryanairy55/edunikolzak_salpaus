# Tämä ohjelma tulostaa annetun luvun mukainen tikku-ukkoja
print("Kuinka monta tikku-ukkoa tulostetaan?")
num = int(input())
string1 = ""
string2 = ""
string3 = ""
i = 1
while i <= num:
    string1 = string1 + " 0  "
    string2 = string2 + "-+- "
    string3 = string3 + "/ \\ "
    i = i + 1
print(string1)
print(string2)
print(string3)
