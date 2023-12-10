# app.py
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
API_KEY = 'abc123'  # กำหนดค่า API key ที่คุณต้องการใช้

def verify_api_key(api_key):
    return api_key == API_KEY

@app.route('/')
def index():
    return 'test api'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file_upload' not in request.files:
        return redirect(request.url)

    file = request.files['file_upload']
    api_key = request.headers.get('API-Key')  # รับค่า API key จาก header

    if not api_key or not verify_api_key(api_key):
        return 'Invalid API key', 401

    if file.filename == '':
        return redirect(request.url)

    if file:
        # ทำตามปกติ
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)
