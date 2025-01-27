# Progetto Bioinformatica: Visualizzazione del Pangenoma

## Struttura del progetto
- `inputFiles/`: Contiene i file scaricati in formato XML
- `fastaFiles/`: Contiene i file convertiti in formato FASTA
- `outputFiles/`: Contiene i risultati delle analisi
- `scripts/`: Contiene gli script di elaborazione e analisi
- `interfaccia.py`: GUI per la gestione del workflow

## Istruzioni per l'uso
1. Scaricare il file XML da NCBI con `python scripts/downloader.py`
2. Convertire il file XML in FASTA con `python scripts/converter.py`
3. Eseguire l'analisi del pangenoma con `python scripts/analysis.py`
4. Visualizzare i risultati con `python scripts/visualization.py`
5. Utilizzare la GUI per la gestione semplificata con `python interfaccia.py`

## Requisiti
- Python 3.x
- Librerie: `requests`, `biopython`, `matplotlib`, `tkinter`

## Esecuzione del progetto completo
```bash
python scripts/main.py
