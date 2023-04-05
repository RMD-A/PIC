import os
from flask import Flask, flash, request, redirect, render_template, Response
from werkzeug.utils import secure_filename
import subprocess

UPLOAD_FOLDER = '../Core/uploads'
BASH_FILE = '../Core/run'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = '!zI2IM&NMJjbF8rX^+x7MC$(&ubW'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No file part", category="warning")
            return redirect(request.url)

        file = request.files['file']

        if file and allowed_file(file.filename):
            os.chdir('../Core')
            name = os.listdir('./uploads')
            if name != []:
                os.remove('./uploads/' + name[0])
            else:
                pass
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            boi = subprocess.run(["python", "check_images.py"], capture_output=True)
            out = boi.stdout.decode()
            flash(out, category='info')
            return redirect(request.url)

if __name__ == '__main__':
    app.run(debug = False)
