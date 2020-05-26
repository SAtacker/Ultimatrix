import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
from flask.helpers import send_from_directory
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = r"C:\Users\shrey_imghzs\Desktop\Ultimatrix\update\static\files"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','zip'}




app = Flask(__name__,template_folder="")
db = SQLAlchemy(app) 
app.config['SECRET_KEY'] = 'cefvnnvjnncewbfewbvbew'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///files.db' 

class Add_Filename(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    text = db.Column(db.String(200)) 
  
    def __repr__(self): 
        return self.text 

@app.route('/')
def index():
    return render_template('index.html')


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/blog.html', methods=['GET', 'POST'])
def upload_file():
    f=None
    filename = ''
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
                fname=Add_Filename(text=filename)
                db.session.add(fname)
                db.session.commit()
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                flash('Your file is uploaded successfully',category='message')
        else:
            flash('Selected file is not permitted')
    return render_template('blog.html',filename=filename)

from flask import send_from_directory
@app.route('/<filename>',methods = ['GET','POST'])
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename=filename,as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)