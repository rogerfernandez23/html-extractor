import gspread
from config import get_google_sheets_client
from datetime import datetime

def insert_to_sheets(data_all, spreadsheet_name='PAGAMENTOS'):
    if not data_all:
        print("❌ Nenhum dado para inserir na planilha.")
        return None
    
    client = get_google_sheets_client()
    spreadsheet = client.open(spreadsheet_name)
    

    sheet_name = datetime.now().strftime('Relatório_%Y%m%d_%H%M%S')
    
    sheet = spreadsheet.add_worksheet(title=sheet_name, rows="100", cols="50")

    all_headers = set()  
    for item in data_all:
        all_headers.update(item.keys()) 

    fixed_headers = ['Funcionário', 'Matrícula']
    
    headers = sorted(list(all_headers - set(fixed_headers)))
    headers = fixed_headers + headers

    values = []
    for item in data_all:
        row = []
        for header in headers:
            if header in item:
                row.append(item[header])
            else:
                row.append(None) 
        values.append(row)

    sheet.batch_update([{"range": "A1", "values": [headers]}, {"range": "A2", "values": values}])

    print("✅ Dados inseridos na planilha com sucesso!")
    return sheet_name