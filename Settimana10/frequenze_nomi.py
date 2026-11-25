# Voglismo contare quante volte ciascun nome compare
# e associare la conta di ciascun nome al nomme stesso
nomi = ["Anna", "Mario", "Marta", "Andrea", "Anna", "Mario", "Gino", "Andrea"]

dict_nomi = dict()

for nome in nomi:
    if nome in dict_nomi.keys():
        dict_nomi[nome] += 1
    else:
        dict_nomi[nome] = 1
        
print(dict_nomi)
