import pandas as pd
from pathlib import Path

def extract_data(file_path: str) -> pd.DataFrame:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File non trovato nel percorso: {file_path}")
    
    df = pd.read_csv(path, sep=';', encoding='utf-8')
    return df

if __name__ == "__main__":
    raw_file = "data/raw/ds558_canoni-di-locazione-versati-e-percepiti-da-regione_rpk5-kd8d.csv"
    df_raw = extract_data(raw_file)
    print(f"Dati estratti con successo! Righe lette: {df_raw.shape[0]}, Colonne: {df_raw.shape[1]}")