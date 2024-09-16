import datetime
import time
from google_sheets.sheet_sync import read_sheet_data, update_sheet_data, get_last_sync_time_from_sheet, update_last_sync_time_in_sheet
from google_sheets.sheet_service import get_sheets_service
from database.db_service import get_db_connection
from database.db_sync import read_db_data, update_db_data
from logger import log_error, log_info

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




# def sync_loop():
#     sheet_service = get_sheets_service()
#     while True:
#         try:
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
# from google_sheets.sheet_service import get_sheets_service
# from google_sheets.sheet_sync import read_sheet_data, update_sheet_data, get_last_sync_time_from_sheet, update_last_sync_time_in_sheet
# from database.db_sync import read_db_data, update_db_data
# from logger import log_info, log_error

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

# def sync_loop():
#     sheet_service = get_sheets_service()
#     while True:
#         try:
#             sync_google_sheet_to_db(sheet_service)
#             sync_db_to_google_sheet(sheet_service)
#             update_last_sync_time_in_sheet(sheet_service, datetime.datetime.utcnow())
#         except Exception as e:
#             log_error("Error during synchronization: %s", e)
#         time.sleep(15)  # Sleep for 15 seconds before the next sync

# if __name__ == "__main__":
#     sync_loop()


import datetime
import time
from google_sheets.sheet_service import get_sheets_service
from google_sheets.sheet_sync import read_sheet_data, update_sheet_data, get_last_sync_time_from_sheet, update_last_sync_time_in_sheet
from database.db_sync import read_db_data, update_db_data
from logger import log_info, log_error

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

def sync_loop():
    sheet_service = get_sheets_service()
    while True:
        try:
            sync_db_to_google_sheet(sheet_service)
            sync_google_sheet_to_db(sheet_service)
            update_last_sync_time_in_sheet(sheet_service, datetime.datetime.utcnow())
        except Exception as e:
            log_error("Error during synchronization: %s", e)
        time.sleep(65)  # Sleep for 15 seconds before the next sync

if __name__ == "__main__":
    sync_loop()
