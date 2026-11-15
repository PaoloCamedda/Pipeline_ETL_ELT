import os
import sqlite3
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def load_data(df: pd.DataFrame, table_name: str = "canoni_locazione") -> None:
    db_path = "data/warehouse.db"
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()

def load_dynamic_data(df: pd.DataFrame, file_name: str) -> None:
    table_name = os.path.splitext(file_name)[0].lower().replace('-', '_').replace(' ', '_')
    db_path = "data/warehouse.db"
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Tabella dinamica '{table_name}' creata/aggiornata con successo nel DB!")