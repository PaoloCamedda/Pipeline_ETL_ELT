DROP TABLE IF EXISTS canoni_locazione;

CREATE TABLE canoni_locazione (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipologia_locazione TEXT NOT NULL,
    locatore TEXT NOT NULL,
    locatario TEXT NOT NULL,
    provincia TEXT,
    comune_citta TEXT,
    indirizzo TEXT,
    civico TEXT,
    destinazione TEXT,
    data_decorrenza_contratto TEXT,
    data_scadenza_contratto TEXT,
    canone_percepito_netto REAL DEFAULT 0.0,
    spese_accessorie_percepite REAL DEFAULT 0.0,
    canone_percepito_lordo REAL DEFAULT 0.0,
    note TEXT,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);