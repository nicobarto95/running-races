import pandas as pd
from datetime import datetime
import os

# --- Configurazione ---
# Sostituisci questo con l'URL effettivo o il percorso del tuo file HTML
SOURCE_PATH = './data/source/gare-podistiche-mondo.html' # Se il tuo HTML è un file locale
# SOURCE_PATH = 'https://www.esempio.com/pagina-gare.html' # Se è un URL
OUTPUT_DIR = 'data'

def scrape_and_process_data(source_path):
    """
    Estrae i dati delle tabelle da una sorgente HTML (file o URL) e li pulisce.
    """
    try:
        print(f"Tentativo di leggere la sorgente da: {source_path}")

        # Pandas cerca automaticamente le tabelle <table> nel codice HTML
        # e le restituisce come una lista di DataFrame.
        tables = pd.read_html(source_path)

        if not tables:
            print("Nessuna tabella trovata nella sorgente HTML.")
            return None

        # Assumiamo che la prima tabella (indice 0) contenga i dati delle gare
        df = tables[0]

        print(f"Trovata la tabella con {len(df)} righe.")

        # --- Pulizia e standardizzazione (adatta al tuo HTML specifico) ---

        # 1. Rinomina le colonne per chiarezza (adatta i nomi esatti del tuo HTML)
        # Esempio: se le colonne sono 'Data', 'Nome Corsa', 'Distanza (km)'
        # df.columns = ['Data', 'Nome', 'Distanza', 'Localita', 'Note']

        # 2. Rimuovi righe totalmente vuote
        df.dropna(how='all', inplace=True)

        # 3. Conversione e pulizia dei dati (esempio: data)
        # Se la colonna data si chiama 'Data', potresti volerla convertire in un formato ISO
        # df['Data'] = pd.to_datetime(df['Data'], errors='coerce', dayfirst=True)
        # df.dropna(subset=['Data'], inplace=True) # Rimuove le righe con data non valida

        # 4. Ordina per data (se hai la colonna Data)
        # df.sort_values(by='Data', inplace=True)

        return df

    except Exception as e:
        print(f"Errore durante lo scraping: {e}")
        # In un ambiente di produzione (GitHub Actions) si potrebbe voler fallire qui
        # raise
        return None

def save_data(df: pd.DataFrame):
    """
    Salva il DataFrame pulito nei formati JSON e CSV.
    """
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 1. Salva in JSON (ideale per l'uso in web app o API)
    json_path = os.path.join(OUTPUT_DIR, 'gare.json')
    # orient='records' crea una lista di oggetti (facile da consumare)
    df.to_json(json_path, orient='records', indent=4, date_format='iso')
    print(f"Dati salvati in: {json_path}")

    # 2. Salva in CSV (ideale per l'analisi manuale o Google Sheets)
    csv_path = os.path.join(OUTPUT_DIR, 'gare.csv')
    df.to_csv(csv_path, index=False)
    print(f"Dati salvati in: {csv_path}")

    # 3. Aggiorna il timestamp (per tracciamento)
    timestamp_path = os.path.join(OUTPUT_DIR, 'last_update.txt')
    with open(timestamp_path, 'w') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":

    # Esegui lo scraping
    races_df = scrape_and_process_data(SOURCE_PATH)

    if races_df is not None and not races_df.empty:
        # Se i dati sono stati estratti con successo, salvali
        save_data(races_df)
    else:
        print("Scraping non riuscito o nessun dato valido trovato. Nessun file salvato.")