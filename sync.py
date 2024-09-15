from google_sheets.sheet_sync import sync_db_to_google_sheet
from database.db_sync import sync_google_sheet_to_db
import time

def sync_loop():
    while True:
        try:
            print("Syncing Google Sheet -> Database")
            sync_google_sheet_to_db()
            
            print("Syncing Database -> Google Sheet")
            sync_db_to_google_sheet()
            
        except Exception as e:
            print(f"Error during synchronization: {e}")
        
        time.sleep(15)  # Sleep for 15 seconds before the next sync

if __name__ == "__main__":
    sync_loop()
