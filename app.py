from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload_test_filename')
def upload_test_filename():
    return render_template("upload.html")

@app.route('/upload_filename', methods=['POST'])
def upload_save_filename():
    file = request.files['file']    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path_to_save = "static/files"
        file.save(os.path.join(path_to_save, filename))
        filepath = "files/" + filename
        print(file.content_type)
        if 'image' in file.content_type:
            return render_template("uploaded_image.html", filepath=filepath)
        else:
            return f"Fichier Uplodé avec Succès{filename}", 200
    else:
        return "Fichier non autorisé.", 400


if __name__ == '__main__':
    app.run()
