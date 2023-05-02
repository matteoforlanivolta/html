# HTML
Compiti HTML svolti dalla 3ID nell'A.S. 2022-2023
# Info
Questa repository rimarrà privata fino all'8/6/2023. Da quel giorno in poi la repo sarà pubblica ma in Modalità Archivio.

Tutti gli esercizi in questa repository sono forniti per scopo educativo.
# Guida
Prima di lavorare con questo codice, verifica di avere le seguenti componenti installate e funzionanti sul tuo computer:
- Un browser web moderno
- Un code editor
- Python 3.10 o versioni più recenti
- (Opzionale) `make` e `zip`
## Operazioni con `make` e `zip` installati
Dopo aver clonato questa repo in un modo qualsiasi, apriamo una Shell nella cartella di base del progetto (quella che contiene il Makefile).

Operazioni possibili:
- Per aprire l'index, digitiamo:
  ```sh
  make
  ```
- Per aggiungere una pagina, digitiamo:
  ```sh
  make new
  ```
  `(todo: aggiungere la pagina all'index HTML tramite script, per ora è necessario farlo manualmente)`
- Per creare un file zip con tutti gli esercizi e senza gli script Python, digitiamo: 
  ```sh
  make deliver
  ```
- Per eliminare il file zip, digitiamo:
  ```sh
  make clean
  ```

## Operazioni senza `make` e `zip` installati
Dopo aver clonato questa repo in un modo qualsiasi, apriamo una Shell nella cartella di base del progetto (quella che contiene il Makefile).

Operazioni possibili:
- Per aggiungere una pagina, digitiamo:
  ```sh
  python3 newpage.py
  ```
  `(todo: aggiungere la pagina all'index HTML tramite script, per ora è necessario farlo manualmente)`
  
- Se crei una pagina manualmente (es. tramite Esplora File) è necessario aggiornare gli script JS, per farlo digita:
  ```sh
  python3 generate.py
  ```
  `(todo: aggiungere la pagina all'index HTML tramite script, per ora è necessario farlo manualmente)`

Consiglio di usare VS Code per modificare il codice.

