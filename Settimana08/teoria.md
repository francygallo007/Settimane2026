# 128

I registri rappresentanpo una picola uantità di memoria interna alla CPU, direttamente
connessi alla ALU e alla FPU. Sonon il tipo di memoria più veloce. ervono per memorizzare
i dati di lavoro del programma e gli operandi/risultati delle operazioni della ALU

il porgram counter non contiene dati di lavoro bensì contiene l'indirizzo di meomoria
della prossima istruzione che la CPU dovrà eseguire. Normalmente si incrementa da solo dopo
aver letto il codice dell'istruzione da eseguire.

# 127

Unità di controllo
    Program counter(PC): contiene l'indirizzo della prossima istruzione da eseguire
    Instruction Register(IR): contiene il codice binario della istruzione in corso di esecuzione
    Flag: registro che memorizza una serie di bit che rappresentano l'esito dell'ultima operazione calcolata dall'ALU
    (positiva, negatova, overflow, carry, zero, ...)
    logica di controllo : legge il valore dell'IR e determina quali operazione devono essere eseguite e
    su quali dati

# 126

n_celle = dimensione_mem / dimensione_cella = 8 kB / 2 B = 4 k celle
quantti bit servono nell'ABUS per indirizzare 4k celle?
2 ^ ABUS  = 4 k ?? ABUS = 12

# 125

ALU = unità aritmetico logica

svolge le oprazioni tra numeri interi (binario puro o compplemento due), sulla base dei comandi
che provengono dalla logica di controllo dell'unità di controllo 
e dei dati presenti nei regitri. Salva il risultato in un registro a aggiorna il registro dei flag

# 124

ABUS = 10 bit (b)
Dimensione_cella = 2 Byte (B)
Max Memoria?
MEM = 2 ^ ABUS * dim_cella = 2 ^ 10 * 2 = 2 kB

Se ABUS fosse di 11 b:
MEM = 2 ^ 11 * 2 = 4 kB

# 123

Esecuzione di un'istruzione di base si compone di 3 fasi:
- Fetch (reperimento)
    IR = MEM(PC)
    La CPU chiede alla memoria di leggere il contenuto della cella il cui indirizzo è presente nel program counter e salva il risultato nell'instruction register.
    PC = PC + 1
- Decode
    La logica di controllo nella CU legge contenuto IR e definisce quale operazione 
    la ALU/FPU debba eseguire, e su quali operandi.
    In pratica decide i comandi da dare all'ALU
- Execute
    La ALU/FPU esegue i comandi ricevuto e salva i risultati.

# 121

- Registri della CPU: [t = ns, D = 100 B] volatili
- Memoria cache(eventualmente 1° livello e 2° livello): [t ~ 100 ns, D = ~ MB] volatile
- Memoria centrale (RAM): [t ~ 1 ms, D ~ 10 GB] volatile
- Memoria di massa: non volatile
    - Flash (SSD Solid State Disk) [t ~ 10-20 ms, D ~ 500 GB]
    - Hard Disk [t ~ 50-100 ms, D ~ 4-8 TB]

# 120

ABUS = 32 b
Dim_celle = 8 B

MEM = 2 ^ ABUS * dim_celle = 2 ^ 32 * 8 = 2 ^ 35 B
1 M = 2 ^ 20
MEM = 2 ^ 35 = 2 ^ 15 MB = 32768 MB
= 2 ^ 5 GB = 32 GB

# 117

Esistono più memorie per permettere alla CPU di lavorare alla massima velocità con le memorie più vicine 
a lei (Regsitri, Cache), ma allo stesso tempo non avere limitazioni alla dimesnione della memoria, che sarebbe 
troppo costoso ampliare a questi livelli.
Quindi aggiungiamo memoria meno costosa ma più capiente. Soprattutto la memoria centrale (RAM) e solitamente memoria di massa.

# 116

Cosa sono i registri? v. sopra

Nel ciclo di esecuzione intervengono PC e IR nella fase di fetch, ed i registri dati nella fase
di execution

# 114

La FPU (Floating Point Unit) svolge le operazioni tra numeri reali (floating point), solitamente
richiede un tempo di calcolo maggiore rispetto all'ALU

# 113

Clock = un segnale periodico a frequenza fissa che definisce il cadenzamento di tutte
le operazioni interne alla CPU e corrisponde alla durata delle operazioni più semplici
(elementari) che la CPU può svolgere (leggi registro, scrivi registro, decodifica istruzione,
fai calcolo ALU, ...).

# 112

Unità operativa =
    Registri
    ALU
    FPU
# 108

ABUS = 28 b
DBUS = 32 b

dimensione dei registri = 32 b come il DBUS come la memoria
numero dei registri --> non possiamo dire niente

# 106

- fetch
    ABUS = valore del PC
    CBUS = leggi
    DBUS = dato della memoria, che finisce in IR
- Decode
    I bus non fanno nulla
- Execute
    sono usati se l'istruzione corrente prevede lettura o scrittura della memoria

# 103

MEM = 4 GB
cella = 32 b
ABUS = ?

MEM = 2 ^ ABUS * DBUS
4 GB = 2 ^ ABUS * 32 b

4 2^30 B = 2 ^ ABUS * 4 B

2^30 = 2^ABUS

ABUS = 30

# 84

f_clock = 2 GHz
    T_ck = 1 / f_ck = 0.5 ns
n_op = 10^7
CPI = 4 (cicli di clock per istruzione)
T = ?

T = n_op * CPI * T_ck = 10^7 * 4 * 0.5 = 2 * 10^7 = 20 ms
