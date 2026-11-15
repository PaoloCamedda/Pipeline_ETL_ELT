import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.copy()
    
    df_clean.columns = (
        df_clean.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('/', '_')
    )
    
    df_clean = df_clean.rename(columns={
        'ultimo_canone_percepito_al_netto_delle_spese': 'canone_percepito_netto',
        'spese_accessorie_percepite': 'spese_accessorie_percepite'
    })
    
    df_clean['spese_accessorie_percepite'] = df_clean['spese_accessorie_percepite'].fillna(0.0)
    df_clean['canone_percepito_lordo'] = df_clean['canone_percepito_netto'] + df_clean['spese_accessorie_percepite']
    
    df_clean['civico'] = df_clean['civico'].fillna('').astype(str).str.replace(r'\.0$', '', regex=True)
    df_clean.loc[df_clean['civico'] == '', 'civico'] = None
    
    columns_to_keep = [
        'tipologia_locazione', 'locatore', 'locatario', 'provincia',
        'comune_citta', 'indirizzo', 'civico', 'destinazione',
        'data_decorrenza_contratto', 'data_scadenza_contratto',
        'canone_percepito_netto', 'spese_accessorie_percepite',
        'canone_percepito_lordo', 'note'
    ]
    
    df_clean = df_clean[columns_to_keep]
    return df_clean

if __name__ == "__main__":
    from extract import extract_data
    raw_file = "data/raw/ds558_canoni-di-locazione-versati-e-percepiti-da-regione_rpk5-kd8d.csv"
    df_raw = extract_data(raw_file)
    df_trans = transform_data(df_raw)
    print(f"Trasformazione completata! Righe elaborate: {df_trans.shape[0]}, Colonne: {df_trans.shape[1]}")