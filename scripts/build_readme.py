import pandas as pd
import json
import os
from datetime import datetime

# --- Configurazione Path ---
# Usiamo i percorsi relativi dalla radice del repository (dove viene eseguito)
DATA_FILE = 'data/source/races.json'
README_FILE = 'README.md'

# --- Configurazione Marcatori (Devono corrispondere a quelli nel tuo README.md) ---
START_MARKER = "Start Tables"
END_MARKER = "End Tables"

def load_data():
    """Carica i dati dal file JSON."""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return pd.DataFrame(data)
    except FileNotFoundError:
        print(f"❌ Errore: File dati non trovato in {DATA_FILE}. Assicurati di averlo creato.")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Errore di parsing JSON in {DATA_FILE}: {e}")
        return None

def generate_markdown_table(df):
    """Genera la tabella Markdown e le statistiche."""
    
    if df.empty:
        return "## Nessuna gara in programma trovata. Controlla il file 'data/gare.json'."

    # 1. Preparazione e Ordinamento dei Dati
    # Ordina per data, assicurando che la data sia trattata come stringa per Pandas
    df['date'] = df['date'].astype(str)
    df = df.sort_values(by='date', ascending=True)

    # Formatta le colonne per il README
    df['Data'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d').strftime('%d %b %Y'))
    df['Major'] = df['major'].apply(lambda x: '🏆 WMM' if x else '')
    df['Distanze'] = df['distances'].apply(lambda x: ', '.join(x))
    df['Status'] = df['status'].apply(lambda x: f'✅ {x}' if x == 'Open' else f'❌ {x}')
    df['Gara'] = df.apply(lambda row: f"**{row['name']}** {row['Major']}", axis=1)
    df['Link'] = df['url'].apply(lambda x: f"[🌐 Sito]({x})")

    # Seleziona e rinomina le colonne finali
    df_final = df[['Data', 'Gara', 'city', 'Distanze', 'Status', 'Link']].copy()
    df_final.columns = ['Data', 'Gara', 'Città', 'Distanze', 'Stato', 'Link']

    # 2. Generazione delle Statistiche
    total_races = len(df)
    open_races = len(df[df['status'] == 'Open'])
    majors = len(df[df['major'] == True])
    last_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')

    stats = f"""
| 📊 Statistiche | Valore |
| :--- | :--- |
| Gare Totali | **{total_races}** |
| Iscrizioni Aperte | **{open_races}** |
| World Majors | **{majors}** |

***
* Ultimo aggiornamento automatico dei dati: **{last_update}**
"""
    # Converte il DataFrame in tabella Markdown
    markdown_table = df_final.to_markdown(index=False)
    
    return f"{stats}\n\n{markdown_table}"


def update_readme(new_content):
    """Sostituisce il contenuto tra i marcatori nel README."""
    try:
        with open(README_FILE, 'r', encoding='utf-8') as f:
            readme_content = f.read()
    except FileNotFoundError:
        print(f"❌ Errore: File README.md non trovato.")
        return

    # Trova le posizioni dei marcatori
    start_index = readme_content.find(START_MARKER)
    end_index = readme_content.find(END_MARKER)

    if start_index == -1 or end_index == -1:
        print(f"❌ Errore: Marcatori {START_MARKER} o {END_MARKER} non trovati nel README.md")
        print("Assicurati che il tuo README abbia i due marcatori!")
        return

    # Costruisce il nuovo README
    before = readme_content[:start_index + len(START_MARKER)]
    after = readme_content[end_index:]
    
    new_readme_content = f"{before}\n{new_content}\n{after}"

    # Scrive il nuovo contenuto
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(new_readme_content)
    
    print("✅ README.md aggiornato con successo.")


if __name__ == "__main__":
    df_races = load_data()
    
    if df_races is not None:
        markdown = generate_markdown_table(df_races)
        update_readme(markdown)