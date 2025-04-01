from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from html_parser import extract_from_html
import os
from google_sheets import insert_to_sheets

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'html'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():    
    if 'file' not in request.files:
        flash("Nenhum arquivo enviado", "error")
        return redirect(request.url)
        
    file = request.files['file']

    if file.filename == '':
        flash("Nenhum arquivo selecionado", "error")
        return redirect(request.url)
        

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        data_all = extract_from_html(file_path)
        if data_all:
            insert_to_sheets(data_all)
            flash("✅ Dados inseridos na planilha com sucesso!", "success")
        else:
            flash("⚠️ Nenhum dado encontrado no arquivo.", "warning")
        
        return redirect(url_for('index'))
    
    flash("⚠️ Arquivo inválido. Envie um arquivo HTML.", "error")
    return redirect(request.url)
    
if  __name__ == '__main__':
    app.run(debug=True)