from flask import Flask,render_template,url_for
app = Flask(__name__,template_folder="")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

if __name__ == "__main__":
    app.run(debug=True)