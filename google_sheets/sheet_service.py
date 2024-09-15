from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to the service account credentials JSON file
SERVICE_ACCOUNT_FILE = r'<enter path to service account key>.json'


# Scopes required to access Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Google Sheet ID
SPREADSHEET_ID = '12JOF2VyoMSAoVzIgNzXT2zzBoQpOyHR4bDKVGifSRZw'

# Example sheet range to sync
RANGE = 'Sheet1!A1:E'

def get_sheet_service():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    return sheet

def read_sheet_data(sheet_service):
    result = sheet_service.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE).execute()
    return result.get('values', [])

def update_sheet_data(sheet_service, data):
    sheet_service.values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE,
        valueInputOption="RAW",
        body={"values": data}
    ).execute()

sheet_service = get_sheet_service()


