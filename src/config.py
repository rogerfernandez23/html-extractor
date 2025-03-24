import gspread
import json
import os
from oauth2client.service_account import ServiceAccountCredentials

def get_google_sheets_client():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    # Configurações de Ambiente em Produção
    credentials = os.getenv('GOOGLE_SHEETS_CREDENTIALS')
    if not credentials:
        raise ValueError("❌ Variável de ambiente 'GOOGLE_SHEETS_CREDENTIALS' não encontrada!")
    
    print(credentials)

    creds_dict = json.loads(credentials)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    
    # Configurações de Ambiente Local
    # creds = ServiceAccountCredentials.from_json_keyfile_name('../credentials.json', scope)
    
    client = gspread.authorize(creds)

    return client

# Testando a conexão com o Google Sheets
try:
    client = get_google_sheets_client()
    spreadsheet = client.open("PAGAMENTOS")
    sheet = spreadsheet.sheet1
    print("✅ Acesso à planilha validado com sucesso!")
except gspread.exceptions.APIError as e:
    print(f"❌ Erro ao acessar a planilha: {e}")