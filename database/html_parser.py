import os
from bs4 import BeautifulSoup

def extract_from_html(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding="utf-8") as file:
            soup = BeautifulSoup(file, 'html.parser')
    else:
        print(f'Erro: O arquivo {file_path} não existe.')
        return None

    data = {}

    titles = soup.find_all('td', class_='tot_titulo_width')
    values = soup.find_all('td', class_='tot_valor_width')

    if not titles or not values:
        print('⚠️ Nenhuma informação encontrada.')
        return {}
    
    for title, value in zip(titles, values):
        title_text = title.get_text(strip=True)
        value_text = value.get_text(strip=True)
        data[title_text] = value_text

    print('✅ Informações extraídas com sucesso.', data)
    return data