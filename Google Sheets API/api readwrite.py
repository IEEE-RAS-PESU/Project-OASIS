from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from pprint import pprint
SERVICE_ACCOUNT_FILE = 'key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = '1o0UYj_TXa4exRgDMlBVCkIpvupXKKGW2ddcs7-wg-zw'
service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="sheet1!A1:C4").execute()
values = result.get('values', [])
x = [[2,5],[56,77]]
response = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Sheet1!B5:C6",valueInputOption="USER_ENTERED",
            body={"values":x}).execute()
#pprint(values)