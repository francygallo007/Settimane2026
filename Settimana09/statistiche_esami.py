def statistica_esame(nome_file):
    totale = 0
    superamenti= 0
    try:
        with open(nomefile, encoding='utf-8') as f:
            for line in f:
                voto = int(line)
                totale += 1
                if voto >= 18:
                    superamenti += 1
        statistica = superamenti/totale
        
    except FileNotFoundError as error:
        print('Il file non è stato trovato')
    except ZeroDivisionError:
        print('Non si può dividere per zero')    

    return statistica

flag = True

while flag:
    nomefile= input('Inserisci il nome del file: ')
    mia_statistica = statistica_esame('esame_analisi.txt')
    if nomefile == '':
        flag = False


