from flask import Flask
from .extensions import api, db
from .resources import ns

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] ='mysql://gen_user:^wVTtDGXXsiF36@147.45.140.206:3306/TEST'

    api.init_app(app)
    db.init_app(app)

    api.add_namespace(ns)

    return app