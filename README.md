# Pipeline_ETL_ELT

# Pipeline ETL / ELT Modulare in Python e SQLite

Una pipeline di Data Engineering modulare, interattiva e orientata alla scalabilità, sviluppata in **Python**. Il sistema consente di gestire flussi di dati eterogenei (CSV) scegliendo dinamicamente tra un approccio **ETL** (Extract, Transform, Load) in memoria con Pandas o un approccio **ELT** (Extract & Load) con creazione dinamica di tabelle di staging e tabelle dedicate direttamente nel database.

---

## Stack & Strumenti
* **Linguaggio:** Python
* **Manipolazione Dati:** Pandas
* **Database & Storage:** SQLite, SQLAlchemy / SQLite3 nativo
* **Configurazione & Log:** `python-dotenv`, `logging` (gestione centralizzata dei log)
* **Architettura:** Modulare (separazione netta tra Estrazione, Trasformazione, Caricamento e Orchestrazione)

---

## 📁 Struttura del Progetto

```text
Pipeline_ETL_ELT/
├── data/
│   ├── raw/            <-- Posiziona qui i file CSV grezzi di input
│   ├── processed/      <-- Archivio automatico dei file elaborati
│   └── warehouse.db    <-- Database SQLite centrale
├── logs/
│   └── pipeline.log    <-- Registro dettagliato delle attività (INFO, WARNING, ERROR)
├── sql/
│   └── create_tables.sql <-- Schema SQL di riferimento per le tabelle strutturate
├── src/
│   ├── extract.py      <-- Modulo di estrazione e lettura file
│   ├── transform.py    <-- Modulo di pulizia, casting e calcoli (ETL)
│   ├── load.py         <-- Modulo di caricamento (statico e dinamico)
│   ├── logger.py       <-- Configurazione del sistema di logging
│   └── main.py         <-- Script di orchestrazione interattivo da terminale
├── .env                <-- Variabili d'ambiente (DATABASE_URL)
└── README.md
```

---

## Funzionalità Principali

1. **Interfaccia Interattiva da Terminale:** Scansiona automaticamente la cartella `data/raw/`, mostra i file disponibili e permette di selezionare quale elaborare.
2. **Scelta Architetturale Dinamica:**
   - **Modalità 1 (ETL):** Legge il file, applica la pulizia e le trasformazioni in Python (Pandas) e carica i dati strutturati.
   - **Modalità 2 (ELT Dinamico):** Ingerisce il file grezzo direttamente nel database creando al volo una tabella dedicata basata sul nome del file (`metadata-driven`), ideale per gestire dataset con schemi differenti.
3. **Automazione del File Lifecycle:** Una volta completato il caricamento con successo, il file CSV viene spostato automaticamente in `data/processed/` per evitare duplicazioni.
4. **Logging Avanzato:** Ogni operazione, successo o errore viene tracciato sia su console che nel file di log persistente (`logs/pipeline.log`).

---

## Installazione e Avvio in Locale
1. **Clona la repository:
    ```git clone [https://github.com/tuo-utente/nome-repository.git](https://github.com/tuo-utente/nome-repository.git)
    cd nome-repository```

2. **Crea e attiva un ambiente virtuale:
    ```
    python -m venv venv
    source venv/bin/activate  # Su Windows: venv\Scripts\activate
    ```

3. **Installa le dipendenze:
    ```
    pip install -r requirements.txt
    ```

4. **Crea il file .env nella root del progetto:
    ```DATABASE_URL=sqlite:///data/warehouse.db```

5. **Esegui la pipeline:
    Metti un file CSV in data/raw/ e avvia lo script principale:
    ```python src/main.py```

