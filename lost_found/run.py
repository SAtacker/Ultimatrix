from flaskblog import create_app


app = create_app()

app.config['SECRET_KEY'] = 'cefvnnvjnncewbfewbvbew'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///files.db'
if __name__ == '__main__':
    app.run(debug=True)