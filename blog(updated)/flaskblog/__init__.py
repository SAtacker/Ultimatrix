from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
# from webpush_handler import trigger_push_notification   #
# from webpush_handler import

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)  #
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # app.config['SECRET_KEY'] = 'cefvnnvjnncewbfewbvbew'
    # app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///files.db'
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

# To-do : inside static put registerserviceworker.js and serviceworker.js