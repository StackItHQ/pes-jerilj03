from google_sheets.sheet_sync import sync_google_sheet_to_db
from database.db_sync import sync_db_to_google_sheet
import time

def sync_loop():
    while True:
        sync_google_sheet_to_db()
        sync_db_to_google_sheet()
        time.sleep(1)  # Sync every 30 seconds

if __name__ == "__main__":
    sync_loop()