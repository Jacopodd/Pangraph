# Pangraph: Visualizzatore di Grafi Pangenomici

Pangraph è un progetto di bioinformatica progettato per visualizzare, analizzare ed esportare grafi pangenomici. Grazie a un'interfaccia intuitiva basata su Dash, gli utenti possono esplorare grafi pangenomici, evidenziare varianti genetiche (bolle) e esportare dati in formato CSV per ulteriori analisi.

---

## Caratteristiche Principali
- **Caricamento di grafi pangenomici** da file in formato GFA.
- **Visualizzazione interattiva del grafo** con nodi cliccabili e pannello laterale per i dettagli.
- **Evidenziazione delle bolle genetiche**, che rappresentano varianti come SNP o inserzioni/delezioni.
- **Esportazione dei dati dei nodi** in formato CSV.

---

## Prerequisiti
Per utilizzare Pangraph, è necessario avere installato:
- **Python 3.8 o superiore**
- **Git** per clonare il repository (opzionale, in alternativa puoi scaricare il file .zip)

---

## Installazione e Avvio

Seguire questi passaggi per scaricare, installare e avviare il progetto.

### 1. Scarica il progetto
#### Opzione 1: Clonare il repository da GitHub
Apri il terminale e inserisci il seguente comando:
```bash
git clone https://github.com/TUO-USERNAME/Pangraph.git
cd Pangraph
```

#### Opzione 2: Scarica il file ZIP
1. Vai alla pagina del repository su GitHub.
2. Clicca su **Code** > **Download ZIP**.
3. Estrai il file ZIP e apri la cartella estratta nel terminale.

---

### 2. Crea l'ambiente virtuale
Crea un ambiente virtuale per isolare le dipendenze del progetto:
```bash
python -m venv venv
```

Attiva l'ambiente virtuale:
- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

---

### 3. Installa le dipendenze
Installa tutte le librerie richieste usando il file `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

### 4. Avvia l'applicazione
Esegui l'applicazione con il seguente comando:
```bash
python -m src.app
```

Dopo qualche secondo, l'app sarà disponibile nel browser all'indirizzo:
```
http://127.0.0.1:8050
```

---

## Utilizzo

1. **Carica un file GFA**:
   - Inserisci il percorso di un file GFA (esempio: `data/example_1.gfa`) e clicca su "Carica Grafo".

2. **Interagisci con il grafo**:
   - Clicca su un nodo per vedere i dettagli nel pannello laterale.

3. **Evidenzia le bolle**:
   - Clicca su "Evidenzia Bubbles" per evidenziare le varianti genetiche.
   - Usa "Reset Evidenziazione" per tornare al grafo iniziale.

4. **Esporta i dati in CSV**:
   - Clicca su "Esporta in CSV" per scaricare un file con i dettagli dei nodi.

---

## File di Esempio
All'interno della cartella `data`, troverai diversi file GFA di esempio da utilizzare per testare l'applicazione:
- `example_1.gfa`: Grafo semplice.
- `example_10.gfa`: Grafo complesso con più bolle e cicli.

---

## Problemi Comuni

### 1. L'app non si avvia
- Assicurati di aver attivato l'ambiente virtuale.
- Verifica di avere Python 3.8 o superiore installato.

### 2. Errore "ModuleNotFoundError"
- Assicurati di aver eseguito il comando `pip install -r requirements.txt`.

### 3. Il grafo non si carica
- Controlla che il percorso del file GFA sia corretto e che il file esista.

---

## Contributi
Se vuoi contribuire al progetto, sentiti libero di fare un fork del repository, apportare modifiche e inviare una pull request.

---

## Licenza
Questo progetto è distribuito sotto la licenza MIT. Consulta il file LICENSE per maggiori dettagli.

