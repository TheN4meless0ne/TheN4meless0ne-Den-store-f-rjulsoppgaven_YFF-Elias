from flask import Flask, render_template, send_from_directory, request
import os
import json
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    with open('../infomodule/data/info.json', encoding='utf-8') as f:
        info_data = json.load(f)
    with open('../infomodule/data/image.json', encoding='utf-8') as f:
        image_data = json.load(f)
    return render_template('page/portfolio.html', info=info_data['myInfo'], imageInfo=image_data['imageInfo'])

@app.route('/cv')
def cv():
    with open('../infomodule/data/pdf.json') as f:
        pdf_data = json.load(f)
    cv_pdf = next((pdf for pdf in pdf_data['pdfFiles'] if pdf['title'] == 'CV'), None)
    return render_template('page/cv.html', cv_pdf=cv_pdf)

@app.route('/files')
def downloads():
    with open('../infomodule/data/pdf.json') as f:
        pdf_data = json.load(f)
    return render_template('page/files.html', pdfs=pdf_data['pdfFiles'])

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('../infomodule/pdf_files', filename)

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('../infomodule/images', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0')