from database.db_service import read_db_rows, create_db_rows, delete_db_rows
from google_sheets.sheet_service import read_sheet_data
import datetime
def sync_google_sheet_to_db():
    # Read data from Google Sheets
    sheet_data = read_sheet_data()
    
    # Read data from the database
    db_data = read_db_rows(datetime.datetime.min)  # Fetch all rows initially
    
    # Normalize data for comparison
    sheet_data_clean = set(sheet_data)
    db_data_clean = set(db_data)
    
    # Find rows to insert or update in the database
    rows_to_insert_or_update = sheet_data_clean - db_data_clean
    
    # Find rows to delete from the database
    rows_to_delete = db_data_clean - sheet_data_clean
    
    # Perform CRUD operations
    if rows_to_insert_or_update:
        create_db_rows(rows_to_insert_or_update)
    
    if rows_to_delete:
        delete_db_rows(rows_to_delete)

    print("Google Sheet and Database are now synced.")
