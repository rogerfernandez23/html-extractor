import gspread
from config import get_google_sheets_client

def insert_to_sheets(data_all, sheet_name='Dados'):
    client = get_google_sheets_client()

    spreadsheet = client.open("Teste")
    sheet = spreadsheet.worksheet(sheet_name)

    headers = list(data_all[0].keys())
    values = [list(item.values()) for item in data_all]

    exists_headers = sheet.row_values(1)

    if not exists_headers:
        sheet.append_row(headers)
    
    sheet.append_rows(values)

    print("✅ Dados inseridos na planilha com sucesso!")
