# **HTML Extractor - Extração de Dados de Frequência para Planilhas**

Este projeto em **Python** permite extrair dados de arquivos **HTML** contendo informações de frequência de colaboradores e inseri-los automaticamente em uma **planilha do Google Sheets**.

## 🚀 **Funcionalidades**

- 📂 Faz upload de um arquivo HTML contendo dados de frequência.
- 🔍 Extrai automaticamente as informações relevantes do arquivo.
- 📊 Processa e organiza os dados para facilitar a análise.
- ☁️ Insere os dados diretamente em uma planilha do Google Sheets.
- 🖥 Interface web simples utilizando **Flask** para interação.

## 🛠 **Tecnologias Utilizadas**

- **Python** 🐍
- **Flask** (Interface Web)
- **Google Sheets API** (Para inserir os dados na planilha)
- **BeautifulSoup** (Para parsing do HTML)
- **Google Apps Script** (Para automação de planilhas)

## ⚙️ **Como Usar**

1. Clone este repositório:

   ```bash
   git clone https://github.com/rogerfernandez23/html_extractor.git
   cd html_extractor
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure suas credenciais do Google Sheets (arquivo `credentials.json`).

4. Inicie a aplicação Flask:

   ```bash
   python app.py
   ```

5. Acesse no navegador:

   ```
   http://127.0.0.1:5000
   ```

6. Faça upload do arquivo HTML e visualize os dados extraídos na planilha do Google Sheets.

\*. Necessário configurar as Credenciais de sua planlha no Google Cloud. Mais sobre: https://medium.com/@matheussouza004/acessando-uma-planilha-do-google-sheets-usando-python-dc243d9803c3
