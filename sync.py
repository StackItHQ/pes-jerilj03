# # import datetime
# # import time
# # from google_sheets.sheet_sync import read_sheet_data, update_sheet_data, get_last_sync_time_from_sheet, update_last_sync_time_in_sheet
# # from google_sheets.sheet_service import get_sheets_service
# # from database.db_service import get_db_connection
# # from database.db_sync import read_db_data, update_db_data
# # from logger import log_error, log_info

# # def sync_google_sheet_to_db(sheet_service):
# #     last_sync_time = get_last_sync_time_from_sheet(sheet_service)
# #     sheet_data = read_sheet_data(sheet_service)
# #     log_info("Data from Google Sheets: %s", sheet_data)
    
# #     for row in sheet_data:
# #         if len(row) != 4:
# #             log_error("Error: Data row %s does not match expected format (4 columns)", row)
# #             return
    
# #     db_data = read_db_data(last_sync_time)
# #     log_info("Data from Database: %s", db_data)

# #     if sheet_data != db_data:
# #         log_info("Syncing Google Sheet -> Database")
# #         update_db_data(sheet_data)
# #     else:
# #         log_info("Google Sheet and Database are already in sync.")

# # def sync_db_to_google_sheet(sheet_service):
# #     db_data = read_db_data(datetime.datetime.min)  # Read all data since beginning
# #     formatted_data = [list(row) for row in db_data]
    
# #     sheet_data = read_sheet_data(sheet_service)

# #     if formatted_data != sheet_data:
# #         log_info("Syncing Database -> Google Sheet")
# #         update_sheet_data(sheet_service, formatted_data)
# #     else:
# #         log_info("Database and Google Sheet are already in sync.")

# # def sync_loop():
# #     sheet_service = get_sheets_service()
# #     while True:
# #         try:
# #             sync_google_sheet_to_db(sheet_service)
# #             sync_db_to_google_sheet(sheet_service)
            
# #             update_last_sync_time_in_sheet(sheet_service, datetime.datetime.utcnow())
# #         except Exception as e:
# #             log_error("Error during synchronization: %s", e)
# #         time.sleep(15)  # Sleep for 15 seconds before the next sync

# # if __name__ == "__main__":
# #     sync_loop()



# import datetime
# import time
# from google_sheets.sheet_sync import read_sheet_data, update_sheet_data, get_last_sync_time_from_sheet, update_last_sync_time_in_sheet,SHEET_ID
# from google_sheets.sheet_service import get_sheets_service
# from database.db_service import get_db_connection
# from database.db_sync import read_db_data, update_db_data
# from logger import log_error, log_info

# def sync_google_sheet_to_db(sheet_service):
#     last_sync_time = get_last_sync_time_from_sheet(sheet_service)
#     sheet_data = read_sheet_data(sheet_service)
#     log_info("Data from Google Sheets: %s", sheet_data)

#     for row in sheet_data:
#         if len(row) != 4:
#             log_error("Error: Data row %s does not match expected format (4 columns)", row)
#             return
    
#     db_data = read_db_data(last_sync_time)
#     log_info("Data from Database: %s", db_data)

#     # Identify rows that need to be deleted from the sheet
#     db_data_set = set(tuple(row) for row in db_data)
#     sheet_data_set = set(tuple(row) for row in sheet_data)
    
#     # Rows to delete from Google Sheets
#     rows_to_delete = [row for row in sheet_data_set if row not in db_data_set]
    
#     if rows_to_delete:
#         log_info("Deleting rows from Google Sheet: %s", rows_to_delete)
#         delete_rows_from_sheet(sheet_service, rows_to_delete)
    
#     # Update the database with the latest data from the sheet
#     if sheet_data != db_data:
#         log_info("Syncing Google Sheet -> Database")
#         update_db_data(sheet_data)
#     else:
#         log_info("Google Sheet and Database are already in sync.")


# def sync_db_to_google_sheet(sheet_service):
#     db_data = read_db_data(datetime.datetime.min)  # Read all data since beginning
#     formatted_data = [list(row) for row in db_data]
    
#     sheet_data = read_sheet_data(sheet_service)

#     if formatted_data != sheet_data:
#         log_info("Syncing Database -> Google Sheet")
#         update_sheet_data(sheet_service, formatted_data)
#     else:
#         log_info("Database and Google Sheet are already in sync.")

# def delete_rows_from_sheet(sheet_service, rows_to_delete):
#     # Get existing data to find row indexes to delete
#     existing_data = read_sheet_data(sheet_service)
#     existing_data_set = set(tuple(row) for row in existing_data)
    
#     # Identify indexes to delete
#     rows_to_delete_set = set(rows_to_delete)
#     rows_to_delete_indexes = [existing_data.index(row) for row in existing_data if row in rows_to_delete_set]

#     # Sort indexes in descending order to avoid index shifting issues
#     rows_to_delete_indexes.sort(reverse=True)
    
#     for index in rows_to_delete_indexes:
#         # Delete the row at the identified index
#         delete_row(sheet_service, index)

# def delete_row(sheet_service, row_index):
#     # Construct the range to delete a single row
#     range_to_delete = f'Sheet1!A{row_index+1}:D{row_index+1}'  # Adjusting for 1-based indexing
    
#     # Clear the row
#     sheet_service.values().clear(spreadsheetId=SHEET_ID, range=range_to_delete).execute()

# def sync_loop():
#     sheet_service = get_sheets_service()
#     while True:
#         try:
#             time.sleep(15)
#             sync_google_sheet_to_db(sheet_service)
            
#             sync_db_to_google_sheet(sheet_service)
            
#             update_last_sync_time_in_sheet(sheet_service, datetime.datetime.utcnow())
#         except Exception as e:
#             log_error("Error during synchronization: %s", e)
#         time.sleep(15)  # Sleep for 15 seconds before the next sync

# if __name__ == "__main__":
#     sync_loop()



# import datetime
# import time
# from google_sheets.sheet_sync import (
#     read_sheet_data, 
#     update_sheet_data, 
#     get_last_sync_time_from_sheet, 
#     update_last_sync_time_in_sheet, 
#     SHEET_ID
# )
# from google_sheets.sheet_service import get_sheets_service
# from database.db_service import get_db_connection
# from database.db_sync import read_db_data, update_db_data, get_last_db_update_time
# from logger import log_error, log_info

# def sync_google_sheet_to_db(sheet_service):
#     last_sync_time = get_last_sync_time_from_sheet(sheet_service)
#     sheet_data = read_sheet_data(sheet_service)
#     log_info("Data from Google Sheets: %s", sheet_data)

#     for row in sheet_data:
#         if len(row) != 4:
#             log_error("Error: Data row %s does not match expected format (4 columns)", row)
#             return
    
#     db_data = read_db_data(last_sync_time)
#     log_info("Data from Database: %s", db_data)

#     # Identify rows that need to be deleted from the sheet
#     db_data_set = set(tuple(row) for row in db_data)
#     sheet_data_set = set(tuple(row) for row in sheet_data)
    
#     # Rows to delete from Google Sheets
#     rows_to_delete = [row for row in sheet_data_set if row not in db_data_set]
    
#     if rows_to_delete:
#         log_info("Deleting rows from Google Sheet: %s", rows_to_delete)
#         delete_rows_from_sheet(sheet_service, rows_to_delete)
    
#     # Update the database with the latest data from the sheet
#     if sheet_data != db_data:
#         log_info("Syncing Google Sheet -> Database")
#         update_db_data(sheet_data)
#     else:
#         log_info("Google Sheet and Database are already in sync.")


# def sync_db_to_google_sheet(sheet_service):
#     db_data = read_db_data(datetime.datetime.min)  # Read all data since beginning
#     formatted_data = [list(row) for row in db_data]
    
#     sheet_data = read_sheet_data(sheet_service)

#     if formatted_data != sheet_data:
#         log_info("Syncing Database -> Google Sheet")
#         update_sheet_data(sheet_service, formatted_data)
#     else:
#         log_info("Database and Google Sheet are already in sync.")

# def delete_rows_from_sheet(sheet_service, rows_to_delete):
#     # Get existing data to find row indexes to delete
#     existing_data = read_sheet_data(sheet_service)
#     existing_data_set = set(tuple(row) for row in existing_data)
    
#     # Identify indexes to delete
#     rows_to_delete_set = set(rows_to_delete)
#     rows_to_delete_indexes = [existing_data.index(row) for row in existing_data if row in rows_to_delete_set]

#     # Sort indexes in descending order to avoid index shifting issues
#     rows_to_delete_indexes.sort(reverse=True)
    
#     for index in rows_to_delete_indexes:
#         # Delete the row at the identified index
#         delete_row(sheet_service, index)

# def delete_row(sheet_service, row_index):
#     # Construct the range to delete a single row
#     range_to_delete = f'Sheet1!A{row_index+1}:D{row_index+1}'  # Adjusting for 1-based indexing
    
#     # Clear the row
#     sheet_service.values().clear(spreadsheetId=SHEET_ID, range=range_to_delete).execute()

# import pytz

# def get_ist_time():
#     ist_timezone = pytz.timezone('Asia/Kolkata')
#     ist_time = datetime.now(ist_timezone)
#     return ist_time


# def sync_loop():
#     sheet_service = get_sheets_service()
#     while True:
#         try:
#             # Get the last sync times from Google Sheets and Database
#             last_sheet_sync_time = get_last_sync_time_from_sheet(sheet_service)
#             last_db_sync_time = get_last_db_update_time()

#             log_info(f"Last Google Sheet Sync: {last_sheet_sync_time}, Last DB Sync: {last_db_sync_time}")
            
#             # Compare the last sync times
#             if last_sheet_sync_time > last_db_sync_time:
#                 # Google Sheets was updated more recently, so sync Google Sheets to Database
#                 log_info("Google Sheets updated more recently. Syncing Sheets to Database.")
#                 sync_google_sheet_to_db(sheet_service)
#                 update_last_sync_time_in_sheet(sheet_service, get_ist_time())
#             else:
#                 # Database was updated more recently, so sync Database to Google Sheets
#                 log_info("Database updated more recently. Syncing Database to Sheets.")
#                 sync_db_to_google_sheet(sheet_service)
            
#             # Update the last sync time in Google Sheets after syncing
            
        
#         except Exception as e:
#             log_error("Error during synchronization: %s", e)
        
#         time.sleep(15)  # Sleep for 15 seconds before the next sync

# if __name__ == "__main__":
#     sync_loop()


import datetime
import time
import pytz
from google_sheets.sheet_sync import read_sheet_data, update_sheet_data, get_last_sync_time_from_sheet, update_last_sync_time_in_sheet, SHEET_ID
from google_sheets.sheet_service import get_sheets_service
from database.db_service import get_db_connection
from database.db_sync import read_db_data, update_db_data, get_last_db_update_time
from logger import log_error, log_info
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Google Drive API configuration for last modified time
SERVICE_ACCOUNT_FILE = r'C:\Users\jeril\Desktop\superjoin_assgn\google_sheets\mysqlsheets-435615-fa7d6f85d058.json'
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.metadata.readonly'
]

# Helper to get Google Drive API service
def get_drive_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return build('drive', 'v3', credentials=credentials)

# Function to get last modified time of Google Sheet and convert it to IST
def get_last_modified_time(sheet_id):
    drive_service = get_drive_service()
    file_metadata = drive_service.files().get(fileId=sheet_id, fields="modifiedTime").execute()
    
    # Parse the UTC timestamp returned by Google Drive API
    last_modified_time_utc = datetime.datetime.strptime(file_metadata['modifiedTime'], '%Y-%m-%dT%H:%M:%S.%fZ')
    
    # Convert to IST
    ist_timezone = pytz.timezone('Asia/Kolkata')
    last_modified_time_ist = last_modified_time_utc.replace(tzinfo=pytz.UTC).astimezone(ist_timezone)
    
    return last_modified_time_ist

# Get IST time for sync time update
def get_ist_time():
    ist_timezone = pytz.timezone('Asia/Kolkata')
    return datetime.datetime.now(ist_timezone)

def sync_google_sheet_to_db(sheet_service):
    last_sync_time = get_last_sync_time_from_sheet(sheet_service)
    sheet_data = read_sheet_data(sheet_service)
    log_info("Data from Google Sheets: %s", sheet_data)

    for row in sheet_data:
        if len(row) != 4:
            log_error("Error: Data row %s does not match expected format (4 columns)", row)
            return
    
    db_data = read_db_data(last_sync_time)
    log_info("Data from Database: %s", db_data)

    # Identify rows that need to be deleted from the sheet
    db_data_set = set(tuple(row) for row in db_data)
    sheet_data_set = set(tuple(row) for row in sheet_data)
    
    # Rows to delete from Google Sheets
    rows_to_delete = [row for row in sheet_data_set if row not in db_data_set]
    
    if rows_to_delete:
        log_info("Deleting rows from Google Sheet: %s", rows_to_delete)
        delete_rows_from_sheet(sheet_service, rows_to_delete)
    
    # Update the database with the latest data from the sheet
    if sheet_data != db_data:
        log_info("Syncing Google Sheet -> Database")
        update_db_data(sheet_data)
    else:
        log_info("Google Sheet and Database are already in sync.")

def sync_db_to_google_sheet(sheet_service):
    db_data = read_db_data(datetime.datetime.min)  # Read all data since beginning
    formatted_data = [list(row) for row in db_data]
    
    sheet_data = read_sheet_data(sheet_service)

    if formatted_data != sheet_data:
        log_info("Syncing Database -> Google Sheet")
        update_sheet_data(sheet_service, formatted_data)
    else:
        log_info("Database and Google Sheet are already in sync.")

def delete_rows_from_sheet(sheet_service, rows_to_delete):
    existing_data = read_sheet_data(sheet_service)
    existing_data_set = set(tuple(row) for row in existing_data)
    
    # Identify indexes to delete
    rows_to_delete_set = set(rows_to_delete)
    rows_to_delete_indexes = [existing_data.index(row) for row in existing_data if row in rows_to_delete_set]

    # Sort indexes in descending order to avoid index shifting issues
    rows_to_delete_indexes.sort(reverse=True)
    
    for index in rows_to_delete_indexes:
        delete_row(sheet_service, index)

def delete_row(sheet_service, row_index):
    range_to_delete = f'Sheet1!A{row_index+1}:D{row_index+1}'  # Adjusting for 1-based indexing
    sheet_service.values().clear(spreadsheetId=SHEET_ID, range=range_to_delete).execute()

# Main sync loop with Google Sheet last modified check
def sync_loop():
    sheet_service = get_sheets_service()
    
    while True:
        try:
            # Get last modified times for both Google Sheets and the database
            last_google_sheet_update = get_last_modified_time(SHEET_ID)
            last_db_update = get_last_db_update_time()
            
            # Ensure last_db_update is timezone-aware (convert to IST timezone)
            ist_timezone = pytz.timezone('Asia/Kolkata')
            if last_db_update.tzinfo is None:  # if naive, make it timezone-aware
                last_db_update = ist_timezone.localize(last_db_update)
            
            log_info(f"Last Google Sheet Sync (IST): {last_google_sheet_update}, Last DB Sync: {last_db_update}")
            
            # Compare times to determine which sync function to call
            if last_google_sheet_update > last_db_update:
                log_info("Google Sheet was updated last, syncing Google Sheet to DB")
                sync_google_sheet_to_db(sheet_service)
            else:
                log_info("Database was updated last, syncing DB to Google Sheet")
                sync_db_to_google_sheet(sheet_service)

            # Update last sync time in Google Sheets
            update_last_sync_time_in_sheet(sheet_service, get_ist_time())

        except Exception as e:
            log_error("Error during synchronization: %s", e)

        time.sleep(15)  # Sleep for 15 seconds before the next sync

if __name__ == "__main__":
    sync_loop()
