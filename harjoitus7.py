from random import choice

def lotto():
    lottoRivi = input("Anna lottorivi: ")
    lottoRiviLista = lottoRivi.split(",") # stringistä listaan
    if len(lottoRiviLista) != 7:
        print("Listassa pitää olla 7 numeroa")
        return
    for i in lottoRiviLista:
        if (int(i) > 39) or (int(i)<1): # numeron pitää olla 1-39
            print("Väärin numero "+i)
            return

    arvotaan = int(input("Kuinka monta riviä arvotaan: "))
    
    lottoArvot = [] # arvojen kerrat
    for i in range(arvotaan):
        rivi = [] # yksi lottorivi
        for a in range(7):
            rivi.append(choice([i for i in range(1,40) if i not in rivi]))
        number = 0 # voitojen kerrat
        for a in lottoRiviLista:
            for b in rivi:
                if str(b) == str(a):
                    number += 1
        lottoArvot.append(number) # lisää voittojen numerot arvojen kertojen listaan
            
    
    print(str(lottoArvot.count(4))+" kertaa neljä oikein!")
    print(str(lottoArvot.count(5))+" kertaa viisi oikein!")
    print(str(lottoArvot.count(6))+" kertaa kuusi oikein!")
    print(str(lottoArvot.count(7))+" kertaa seitsemän oikein!")
    
lotto()
