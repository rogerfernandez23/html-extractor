from src.html_parser import extract_from_html
from src.google_sheets import insert_to_sheets

def main():
    file_path = '../files/test.html'

    # Executa extração de dados do HTML
    data_all = extract_from_html(file_path)

    # Insere os Dados na Planilha
    insert_to_sheets(data_all)

if __name__ == '__main__':
    main()