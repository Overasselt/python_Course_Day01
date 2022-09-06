#dict comprehension
getallen = [123, 456, 789]

kwadraten = {getal : getal ** 2 for getal in getallen if getal >= 20}
print(kwadraten)