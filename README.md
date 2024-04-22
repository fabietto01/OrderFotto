# Nome del Progetto

Questo progetto si occupa di spostare e riordinare le immagini presenti in una cartella, suddividendole in sotto-cartelle divise per anno e mese. 

## Indice

- [Installazione](#installazione)
- [Utilizzo](#utilizzo)

## Installazione

Segui questi passaggi per installare il progetto:

1. Clona il repository: `git clone https://github.com/fabietto01/OrderFotto.git`
2. Entra nella directory del progetto: `cd OrderFotto`
3. Crea un ambiente virtuale Python: `python3 -m venv env`
4. Attiva l'ambiente virtuale: 
    - Su Windows: `.\env\Scripts\activate`
    - Su Unix o MacOS: `source env/bin/activate`
5. Installa le dipendenze dal file requirements.txt: `pip install -r requirements.txt`

## Utilizzo

Per utilizzare il progetto, è sufficiente avviare il file main.py e passare gli argomenti richiesti: `--input`, `--output` e `--multi-thread`. L'argomento `--multi-thread` non è obbligatorio e di default è impostato su false. Gli altri due argomenti, `--input` e `--output`, rappresentano rispettivamente la cartella di origine dove sono presenti tutte le foto e la cartella di destinazione dove lo script inserirà le immagini.

Ad esempio:

1. Esegui il comando: `python main.py --input percorso/alla/cartella/delle/foto --output percorso/alla/cartella/di/destinazione`
2. Se desideri utilizzare il multi-threading, aggiungi l'argomento `--multi-thread`: `python main.py --input percorso/alla/cartella/delle/foto --output percorso/alla/cartella/di/destinazione --multi-thread`
3. Segui le istruzioni visualizzate sulla console.