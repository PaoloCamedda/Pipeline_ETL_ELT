import os
import shutil
from pathlib import Path
from dotenv import load_dotenv

from extract import extract_data
from transform import transform_data
from load import load_data # Per la modalità ETL classica
# Importiamo la nuova funzione dinamica per l'ELT
import sys
sys.path.append("src")
from load import load_dynamic_data 

from logger import setup_logger

load_dotenv()
logger = setup_logger()

def run_pipeline():
    raw_dir = Path("data/raw")
    processed_dir = Path("data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)
    
    if not raw_dir.exists():
        logger.error("La cartella data/raw/ non esiste.")
        return

    csv_files = list(raw_dir.glob("*.csv"))
    if not csv_files:
        logger.warning("Nessun file CSV trovato in data/raw/.")
        print("\nNessun file CSV disponibile.")
        return

    print("\n--- FILE DISPONIBILI ---")
    for idx, file in enumerate(csv_files, 1):
        print(f"{idx}. {file.name}")
    print("------------------------")
    
    scelta_file = input("Seleziona il numero del file: ").strip()
    try:
        raw_file_path = csv_files[int(scelta_file) - 1]
    except (ValueError, IndexError):
        print("Scelta file non valida.")
        return

    print("\n--- SCEGLI L'ARCHITETTURA ---")
    print("1. ETL (Trasformazione specifica via Pandas)")
    print("2. ELT Dinamico (Caricamento raw in tabella dedicata basata sul nome file)")
    print("------------------------------")
    
    scelta_arch = input("Seleziona la modalità (1 o 2): ").strip()
    
    try:
        if scelta_arch == "1":
            logger.info(f"Avvio pipeline ETL per: {raw_file_path.name}")
            df_raw = extract_data(raw_file_path)
            df_trans = transform_data(df_raw)
            load_data(df_trans, table_name="canoni_locazione")
            logger.info("ETL completato con successo.")
            
        elif scelta_arch == "2":
            logger.info(f"Avvio pipeline ELT Dinamica per: {raw_file_path.name}")
            df_raw = extract_data(raw_file_path)
            # Carica il file in una tabella che prende il nome del file stesso
            load_dynamic_data(df_raw, raw_file_path.name)
            logger.info(f"Caricamento ELT dinamico completato per {raw_file_path.name}.")
            
        else:
            print("Modalità non valida.")
            return

        destination_path = processed_dir / raw_file_path.name
        shutil.move(str(raw_file_path), str(destination_path))
        print(f"\nOperazione completata! File spostato in: {destination_path}")

    except Exception as e:
        logger.error(f"Errore durante la pipeline: {e}")
        print(f"\nErrore: {e}")

if __name__ == "__main__":
    run_pipeline()