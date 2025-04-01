import os
from bs4 import BeautifulSoup

def extract_from_html(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding="utf-8") as file:
            soup = BeautifulSoup(file, 'html.parser')
    else:
        print(f'Erro: O arquivo {file_path} não existe.')
        return None

    data = []

    user_info = soup.find_all('tr')

    for user in user_info:
        nome = None
        cpf = None
        cols = user.find_all('td')

        cols = user.find_all('td')

        for col in cols:
            if "Funcionário" in col.get_text():
                nome = col.find_next('td').get_text(strip=True)
            elif "Matrícula" in col.get_text():
                cpf = col.find_next('td').get_text(strip=True)
        
        if nome and cpf:
            titles = user.find_all_next('td', class_='tot_titulo_width', limit=50) 
            values = user.find_all_next('td', class_='tot_valor_width', limit=50)

            data_row = {
                'Funcionário': nome,
                'Matrícula': cpf
            }

            for title, value in zip(titles, values):
                title_text = title.get_text(strip=True)
                value_text = value.get_text(strip=True)
            
                if title_text not in data_row:  
                    data_row[title_text] = value_text
            data.append(data_row) 

    if not data:
        print('⚠️ Nenhuma informação encontrada.')
    else:
        print('✅ Informações extraídas com sucesso.')

    return data
