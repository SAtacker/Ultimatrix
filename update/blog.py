import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
from flask.helpers import send_from_directory


UPLOAD_FOLDER = r"C:\Users\shrey_imghzs\Desktop\Ultimatrix\update\static\files"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__,template_folder="")

app.config['SECRET_KEY'] = 'cefvnnvjnncewbfewbvbew'

@app.route('/')
def index():
    return render_template('index.html')


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/blog.html', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file chosen')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if allowed_file(file.filename):
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                flash('Your file is uploaded successfully',category='message')
        else:
            flash('Selected file is not permitted')
    return render_template('blog.html')

from flask import send_from_directory


if __name__ == "__main__":
    app.run(debug=True)