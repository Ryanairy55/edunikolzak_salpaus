mjono1 = str(input("Anna eka sana: "))
mjono2 = str(input("Anna toka sana: "))
onkoanagrammi = True # tämä boolean muuttuja on tehty, jotta voi kertoa ovatko sanat ovat anagrammit ohjelman lopussa
if len(mjono1) != len(mjono2):
    onkoanagrammi = False
for i in range(0, len(mjono1)-1):
    if mjono1.count(mjono1[i]) != mjono2.count(mjono1[i]):
        onkoanagrammi = False
        break # break jos kirjainten määrä erottaa
if onkoanagrammi: # jos muuttuja on tosi
    print("Sana "+mjono1+" on sanan "+mjono2+" anagrammi!")
else:
    print("Sana "+mjono1+" ei ole sanan "+mjono2+" anagrammi!")
