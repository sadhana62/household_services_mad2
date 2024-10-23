from flask import Flask
from flask_login import login_required
from Backend.config import LocalDevelopmentConfig
from Backend.models import db, User, Role
from flask_security import Security, SQLAlchemyUserDatastore, auth_required
# from Backend.resources import api


def createApp():
    app = Flask(__name__,  template_folder='frontend/urban-services-app/dist/', 
    static_folder='frontend/urban-services-app/dist/', 
    static_url_path='/')

    app.config.from_object(LocalDevelopmentConfig)


    # model init
    db.init_app(app)
    
    # flask-restful init
    # api.init_app(app)

    #flask security
    datastore = SQLAlchemyUserDatastore(db, User, Role)

    app.security = Security(app, datastore=datastore, register_blueprint=False)
    app.app_context().push()

    return app

app = createApp()

import Backend.initial_data

import Backend.routes


if (__name__ == '__main__'):
    app.run()