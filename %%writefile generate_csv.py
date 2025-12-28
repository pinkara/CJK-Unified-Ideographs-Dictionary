import csv
import data_processor

# --- CONFIGURATION ---
OUTPUT_CSV_FILE = "cjk_characters.csv"

def generate_csv():
    print("1. Retrieving CJK data...")
    cjk_data = data_processor.get_cjk_data()

    if not cjk_data:
        print("   ERROR: Failed to retrieve CJK data. CSV generation aborted.")
        return

    print(f"   Successfully retrieved {len(cjk_data)} CJK characters.")
    print(f"2. Writing data to {OUTPUT_CSV_FILE}...")

    try:
        with open(OUTPUT_CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
            # Define the fieldnames based on the dictionary keys
            fieldnames = ['rad', 'str', 'cp', 'char']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader() # Write the header row
            for item in cjk_data:
                writer.writerow(item) # Write each character as a row

        print(f"   Successfully generated '{OUTPUT_CSV_FILE}' with {len(cjk_data)} entries.")
    except Exception as e:
        print(f"   CRITICAL ERROR: Failed to write CSV file. {e}")

if __name__ == "__main__":
    generate_csv()
