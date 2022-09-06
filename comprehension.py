getallen = [123, 456, 789]

squares  =[getal ** 2 for getal in getallen]

print(squares)

#join met : ertussen

print(':'.join([str(x) for x in squares]))

# 30 getallen tussen 1 en 100

import random
getallen =[random.randint(1,100) for i in range(30)]
print(getallen)

# andere niet zo'n mooie manier van bovenstaande

getallen = []
for i in range(30):
    getallen.append(random.randint(1,100))

#kwadraten

kwadraten = [getal ** 2 for getal in getallen]
print(kwadraten)

# alleen getallen groter dan 20 en kleiner dan 30

# kwadraten = [getal ** 2 for getal in getallen if getal >= 20 and < 100]
# print(kwadraten)

# duizendtallen scheiden

x = 12122341235
print(f'{x:,}')

#dict comprehension

kwadraten = {getal ** 2 for getal in getallen if getal >= 20}
print(kwadraten)

# sorteren

sorted(getallen)

# set maken (om bv unieke getallen te zoeken)

set(getallen)

# dict

d = {'nl': '31', 'de': '+41'}
print(d)

# generator (doet niks tot je het gaat gebruiken) staat ook tussen ()

kwadraten = (getal ** 2 for getal in getallen if getal >= 20)
print(kwadraten)

for x in kwadraten:
    print(x)

# getallen

huge = list(range(400,10000,50))
print(huge)

#build in function

woorden = 'de kat krapt de krullen van de trap.'.lower().split()
print(woorden)

print('_'.join(woorden))

print(sorted(woorden))
#omdraaien
print(sorted(woorden, reverse=True))
# op lengte sorteren
print(sorted(woorden, key=len, reverse=True))
# grootste 3
print(sorted(woorden, key=len, reverse=True)[:3])
#sorteren op a
def aantal_a(woord):
    return woord.count('a')
print(sorted(woorden, key=aantal_a, reverse=True))
# lambda voor het gebruik van directe functie icm argumenten en return
print(sorted(woorden, key=lambda woord: woord.count('l'), reverse=True))
# filter alles met k
print(list( filter(lambda woord: 'k' in woord, woorden)))
#map verander k in uppercase
print(list( map(lambda woord: woord.upper() if 'k' in woord else woord, woorden)))






