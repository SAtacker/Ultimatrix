from flask import render_template, request, Blueprint,flash,redirect, url_for,render_template
from flaskblog.models import Post
from werkzeug.utils import secure_filename
from flask.helpers import send_from_directory
import os
path = os.path.abspath(os.getcwd())

UPLOAD_FOLDER = r"flaskblog\static\files"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','zip'}

path = os.path.join(path,UPLOAD_FOLDER)
print(path)
main = Blueprint('main', __name__)


@main.route("/")
@main.route("/index")
def index():
    return render_template('edited.html', title='Index')


@main.route("/blog/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route('/files', methods=['GET', 'POST'])
def upload_file():
    f=None
    filename = ''
    filenames = [fname for fname in os.listdir(path) if os.path.isfile(os.path.join(path,fname))]
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
                # fname=Add_Filename(text=filename)
                # db.session.add(fname)
                # db.session.commit()
                file_path = os.path.join(path, filename)
                file.save(file_path)
                
                flash('Your file is uploaded successfully',category='message')
        else:
            flash('Selected file is not permitted')
    return render_template('files.html',name=filenames)


@main.route('/<filename>',methods = ['GET','POST'])
def download(filename):
    return send_from_directory(path,filename=filename,as_attachment=True)