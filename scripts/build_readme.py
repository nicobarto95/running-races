import pandas as pd
import json
import os
from datetime import datetime

# --- Configurazione Path ---
DATA_FILE = 'data/source/races.json'
README_FILE = 'README.md'

# --- Configuration Markers (included into the README.md) ---
START_MARKER = "Start Tables"
END_MARKER = "End Tables"

def format_date(date_str):
    if not date_str:
        return ""
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%d %b %Y')
    except ValueError:
        return date_str
    
def load_data():
    """Loads data from the JSON file."""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return pd.DataFrame(data)
    except FileNotFoundError:
        print(f"❌ Error: Data file not found at {DATA_FILE}. Please ensure it exists.")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error in {DATA_FILE}: {e}")
        return None

def generate_markdown_table(df):
    """Generates the Markdown table and statistics."""
    
    if df.empty:
        return "## No races scheduled found. Check the 'data/source/races.json' file."

    # 1. DATA PREPARATION AND SORTING
    
    # Sort by date, ensuring date is treated as string for Pandas
    df['date'] = df['date'].astype(str)
    
    # Sort races by date
    df['SortDate'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.sort_values(by='SortDate', ascending=True).drop(columns=['SortDate'])
    
    # Formatta le colonne per il README
    df['Date'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d').strftime('%d %b %Y'))
    df['Major'] = df['major'].apply(lambda x: '🏆 WMM' if x else '')
    df['Distances'] = df['distances'].apply(lambda x: ', '.join(x))
    df['Status'] = df['status'].apply(lambda x: f'✅ {x}' if x == 'Open' else f'❌ {x}')
    df['Race'] = df.apply(lambda row: f"**{row['name']}** {row['Major']}", axis=1)
    df['Link'] = df['url'].apply(lambda x: f"[🌐 Sito]({x})")

    # Seleziona e rinomina le colonne finali
    df_final = df[['Date', 'Race', 'City', 'country', 'Distances', 'price', 'Status', 'Link']].copy()
    df_final.rename(columns={
        'country': 'Country',
        'price': 'Price'
    }, inplace=True)

    # 2. GENERATE STATISTICS
    total_races = len(df)
    open_races = len(df[df['status'] == 'Open'])
    majors = len(df[df['major'] == True])
    last_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')

    stats = f"""
| 📊 Statistics | Value |
| :--- | :--- |
| Total Races | **{total_races}** |
| Open Registrations | **{open_races}** |
| World Majors | **{majors}** |

***
* Last automatic update: **{last_update}**
"""
    # Convert DataFrame to Markdown table
    markdown_table = df_final.to_markdown(index=False)
    
    return f"{stats}\n\n{markdown_table}"


def update_readme(new_content):
    """Replaces content between markers in the README."""    
    try:
        with open(README_FILE, 'r', encoding='utf-8') as f:
            readme_content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: README.md file not found.")
        return

    # Trova le posizioni dei marcatori
    start_index = readme_content.find(START_MARKER)
    end_index = readme_content.find(END_MARKER)

    if start_index == -1 or end_index == -1:
        print(f"❌ Error: Markers '{START_MARKER}' or '{END_MARKER}' not found in README.md")
        print("Ensure your README has both markers!")
        return

    # Costruisce il nuovo README
    before = readme_content[:start_index + len(START_MARKER)]
    after = readme_content[end_index:]
    
    new_readme_content = f"{before}\n{new_content}\n{after}"

    # Scrive il nuovo contenuto
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(new_readme_content)
    
    print("✅ README.md successfully updated.")


if __name__ == "__main__":
    df_races = load_data()
    
    if df_races is not None:
        markdown = generate_markdown_table(df_races)
        update_readme(markdown)