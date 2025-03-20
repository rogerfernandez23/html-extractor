import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_google_sheets_client():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('../credentials.json', scope)
    client = gspread.authorize(creds)

    return client

# Testando a conexão com o Google Sheets
try:
    client = get_google_sheets_client()
    spreadsheet = client.open("Teste")
    sheet = spreadsheet.sheet1
    print("✅ Acesso à planilha validado com sucesso!")
except gspread.exceptions.APIError as e:
    print(f"❌ Erro ao acessar a planilha: {e}")