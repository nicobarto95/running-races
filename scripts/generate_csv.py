import pandas as pd
import json
import os

DATA_FILE = 'data/gare.json'
CSV_FILE = 'data/gare.csv'

def generate_csv():
    """Reads JSON and saves it as CSV."""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        df = pd.DataFrame(data)
        
        # Flatten the 'distances' column for CSV (since CSVs are 2D)
        df['distances'] = df['distances'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
        
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
        
        df.to_csv(CSV_FILE, index=False)
        print(f"✅ Successfully generated CSV: {CSV_FILE}")

    except Exception as e:
        print(f"❌ Error generating CSV: {e}")
        
if __name__ == "__main__":
    generate_csv()