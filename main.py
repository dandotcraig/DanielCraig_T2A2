import os
from flask import Flask
from init import db, ma, bcrypt, jwt

def create_app():
    app = Flask(__name__)

    app.json.sort_keys = False

    #configs - passwords etc, hidden using .env
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URI")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

    #app factories - connecting our app via init
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    #adds the comand line controller
    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    from controllers.account_controller import account_bp
    app.register_blueprint(account_bp)

    from controllers.favourites_list_controller import favourites_list_bp
    app.register_blueprint(favourites_list_bp)

    from controllers.search_input_controller import search_input_bp
    app.register_blueprint(search_input_bp)

    return app

