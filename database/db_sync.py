
from .db_service import read_db_data,update_db_data
from google_sheets.sheet_service import update_sheet_data
from google_sheets.sheet_sync import read_sheet_data,sheet_service

def sync_google_sheet_to_db():
    # Get data from Google Sheets
    sheet_data = read_sheet_data(sheet_service)

    # Get data from MySQL
    db_data = read_db_data()

    # Compare data and update MySQL if necessary
    if sheet_data != db_data:
        print("Syncing Google Sheet -> Database")
        update_db_data(sheet_data)
    else:
        print("Google Sheet and Database are already in sync.")

def sync_db_to_google_sheet():
    # Get data from MySQL
    db_data = read_db_data()

    # Get data from Google Sheets
    sheet_data = read_sheet_data(sheet_service)

    # Compare data and update Google Sheets if necessary
    if sheet_data != db_data:
        print("Syncing Database -> Google Sheet")
        update_sheet_data(sheet_service, db_data)
    else:
        print("Database and Google Sheet are already in sync.")
