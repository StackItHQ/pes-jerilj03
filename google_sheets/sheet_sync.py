from database.db_service import read_db_rows
from google_sheets.sheet_service import update_sheet_data, read_sheet_data, delete_sheet_rows
import datetime

def sync_db_to_google_sheet():
    # Fetch the latest data from both Google Sheets and the database
    db_data = read_db_rows(datetime.datetime.min)  # Fetch all rows from the database
    sheet_data = read_sheet_data()  # Fetch all rows from Google Sheets
    
    db_data_clean = {row[0]: row for row in db_data}  # Dictionary with col1 as the key
    sheet_data_clean = {row[0]: row for row in sheet_data}  # Same for Google Sheets
    
    rows_to_insert_or_update = []
    rows_to_delete = []
    
    # Compare the data to find rows to update or delete
    for db_key, db_row in db_data_clean.items():
        if db_key not in sheet_data_clean:
            # This row exists in the database but not in Google Sheets (INSERT)
            rows_to_insert_or_update.append(db_row)
        elif db_row != sheet_data_clean[db_key]:
            # This row exists in both, but values differ (UPDATE)
            rows_to_insert_or_update.append(db_row)
    
    for sheet_key in sheet_data_clean:
        if sheet_key not in db_data_clean:
            # This row exists in Google Sheets but not in the database (DELETE)
            rows_to_delete.append(sheet_data_clean[sheet_key])

    # Insert or update rows in Google Sheets
    if rows_to_insert_or_update:
        update_sheet_data(rows_to_insert_or_update)
        print(f"Inserted/Updated {len(rows_to_insert_or_update)} rows in Google Sheets.")
    
    # Delete rows from Google Sheets
    if rows_to_delete:
        delete_sheet_rows(rows_to_delete)
        print(f"Deleted {len(rows_to_delete)} rows from Google Sheets.")
    
    print("Database and Google Sheets are now synced.")
