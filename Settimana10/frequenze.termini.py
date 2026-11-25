import string


def conta_occorenze(file):
    with open("alice_in_wonderland.txt", 'r', encoding='utf-8') as f:
        conta_parole = dict()
        riga = f.readline()
        while riga != "":
            riga = riga.replace("--", " ")
            riga = riga.replace("-", " ")
        
            parole_riga = riga.lower().strip(string.punctuation).rstrip().split()
            for parola in parole_riga:
                parola.strip(string.punctuation)
                if parola not in conta_parole.keys():
                    conta_parole[parola] = 1
                else:
                    conta_parole[parola] += 1
              
            riga = f.readline()
        print(conta_parole) 
        return conta_parole

conta_parole = conta_occorenze("alice_in_wonderland.txt")

print(conta_parole)