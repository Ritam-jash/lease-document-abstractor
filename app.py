import mysql.connector
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os
from werkzeug.utils import secure_filename
import PyPDF2

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Database configuration
db = mysql.connector.connect(
    host=os.environ.get('MYSQL_HOST'),
    user=os.environ.get('MYSQL_USER'),
    password=os.environ.get('MYSQL_PASSWORD'),
    database=os.environ.get('MYSQL_DATABASE')
)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'document' not in request.files:
        return redirect(request.url)
    file = request.files['document']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        file.save(file_path)
        abstract_data(file_path, filename)
        return redirect(url_for('upload_form'))
    return redirect(request.url)

def abstract_data(file_path, filename):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    clauses = extract_clauses(text)

    cursor = db.cursor()
    sql = "INSERT INTO leases (filename, clauses) VALUES (%s, %s)"
    val = (filename, clauses)
    cursor.execute(sql, val)
    db.commit()

def extract_clauses(text):
    return text[:500]  # Return the first 500 characters as a simple example

@app.route('/view')
def view_abstracts():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM leases")
    leases = cursor.fetchall()
    print("Leases fetched from database:", leases)  # Log the fetched data
    return render_template('view.html', leases=leases)

# Route to serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
