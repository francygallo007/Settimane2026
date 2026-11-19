try:
    with open("film.csv", encoding='utf-8') as f:
        print(f.readline())

    n = int(input("Inserisci un numero: "))
except FileNotFoundError as error: #Salva l'errore che andrebbe a stampare
    print('Il file non è stato trovato')

except ValueError as ve:
    print('Non hai inserito un numero')