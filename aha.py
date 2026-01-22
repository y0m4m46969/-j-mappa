import io
import string

#enyem (rossz)
"""adatok = ""
try:
    with open("F1_2000-2024.csv", encoding="utf-8") as fajl:
        for sor in fajl:
            adatok=fajl.read()
except IOError as ex:
    print(ex)

adatokx = adatok.strip().split(",")


print(f"{adatok} \n\n")
print(f"{adatokx} \n\n")

nevek = []
sor = 1

if adatokx[2] not in nevek:
    nevek.append(adatokx[2])
    
while sor<len(adatokx) and int(adatokx[1]) == 1:
    sor += 1
    
if sor<len(adatokx):
    print(f"Nem mindenki volt első helyen")
else:
    print(f"Mindenki volt első helyen")
    
    
if adatok[2] not in nevek:
    nevek.append(adatok[2])
    
while sor<len(adatok) and int(adatok[1]) == 1:
    sor += 1
    
if sor<len(adatok):
    print(f"Nem mindenki volt első helyen")
else:
    print(f"Mindenki volt első helyen")
    
print(nevek)"""

#---------------------------------------------

verseny_adatok = []

try:
    with open("F1_2000-2024.csv", encoding="utf-8") as fajl:
        fajl.readline()
        
        for sor in fajl:
            sornyi_adat = sor.strip().split(",")
            
            sornyi_adat[0] = int(sornyi_adat[0])
            sornyi_adat[1] = int(sornyi_adat[1])
            
            verseny_adatok.append(sornyi_adat)       
        
except IOError as ex:
    print(f"IO hiba: {ex}")

#print(verseny_adatok)

versenyzo_adatok = []

elso = [verseny_adatok[0][2], verseny_adatok[0][1]]
versenyzo_adatok.append(elso)

def listaval():
    for i in range(1, len(verseny_adatok)):
        j = 0
        while j < len(versenyzo_adatok) and versenyzo_adatok[j][0] != verseny_adatok[i][2]:
            j += 1

        if j >= len(versenyzo_adatok):
            uj = [verseny_adatok[i][2], verseny_adatok[i][1]]
            versenyzo_adatok.append(uj)
        else:
            if versenyzo_adatok[j][1] > verseny_adatok[i][1]:
                versenyzo_adatok[j][1] = verseny_adatok[i][1]

    #print(versenyzo_adatok)

    i = 0
    while i < len(versenyzo_adatok) and versenyzo_adatok[i][1] == 1:
        i +=1

    if i >= len(versenyzo_adatok):
        print(f"Minden versenyzo volt elso helyezett!")
    else:
        print(f"Nem minden versenyzo volt elso helyezett! Pl.: {versenyzo_adatok[i][0]}")

#---------------------------------------------

#listaval()

versenyzo_adatok_2 = {}

for sor in verseny_adatok:

    #megnezzuk benne van e hogy le tudjuk cserelni ha jobb a helyezet
    if sor[2] in versenyzo_adatok_2.keys():
        if versenyzo_adatok_2[sor[2]] > sor[1]:
            #ez megvaltoztatja a kulcs erteket
            versenyzo_adatok_2[sor[2]] = sor[1]
    else:
        #ez meg beleteszi a listaba
        versenyzo_adatok_2[sor[2]] = sor[1]
        
print(versenyzo_adatok_2)

mindenki = True

for ertek in versenyzo_adatok_2.values():
    if ertek > 1:
        mindenki = False
        break
        
if mindenki:
    print("mindenki volt első helyen")
else:
    print("NEM mindenki volt első helyen")
