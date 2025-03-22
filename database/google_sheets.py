import gspread
from config import get_google_sheets_client
from datetime import datetime

def insert_to_sheets(data_all, spreadsheet_name='Teste'):
    client = get_google_sheets_client()
    spreadsheet = client.open(spreadsheet_name)

    sheet_name = datetime.now().strftime('Relatório_%Y%m%d')
    
    sheet = spreadsheet.add_worksheet(title=sheet_name, rows="100", cols="50")

    headers = list(data_all[0].keys())
    values = [list(item.values()) for item in data_all]

    sheet.append_row(headers)
    sheet.append_rows(values)

    print("✅ Dados inseridos na planilha com sucesso!")
    return sheet_name
