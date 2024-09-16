# from googleapiclient.discovery import build
# from google.oauth2 import service_account

# # Google Sheets configuration
# SHEET_ID = '12JOF2VyoMSAoVzIgNzXT2zzBoQpOyHR4bDKVGifSRZw'
# RANGE_NAME = 'Sheet1!A:D'
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# SERVICE_ACCOUNT_FILE = r'C:\Users\jeril\Desktop\superjoin_assgn\google_sheets\mysqlsheets-435615-fa7d6f85d058.json'

# # Create Google Sheets service
# def get_sheets_service():
#     credentials = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES
#     )
#     return build('sheets', 'v4', credentials=credentials).spreadsheets()

# # Read data from Google Sheets
# def read_sheet_data():
#     sheet_service = get_sheets_service()
#     result = sheet_service.values().get(spreadsheetId=SHEET_ID, range=RANGE_NAME).execute()
#     values = result.get('values', [])
    
#     # Ensure each row has 4 columns
#     formatted_data = []
#     for row in values:
#         if len(row) < 4:
#             row.extend([''] * (4 - len(row)))
#         formatted_data.append(tuple(row))
    
#     return formatted_data

# Create or update rows in Google Sheets



from googleapiclient.discovery import build
from google.oauth2 import service_account

# Google Sheets configuration
SHEET_ID = '12JOF2VyoMSAoVzIgNzXT2zzBoQpOyHR4bDKVGifSRZw'
SERVICE_ACCOUNT_FILE = r'C:\Users\jeril\Desktop\superjoin_assgn\google_sheets\mysqlsheets-435615-fa7d6f85d058.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_sheets_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return build('sheets', 'v4', credentials=credentials).spreadsheets()
