from flask import Flask
from config import db, migrate
from routes.usuario import user_bp
from flask_cors import CORS
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import os

load_dotenv()
app=Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY']='wyhgewty3g278te62fec32uhes'
jwt=JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.register_blueprint(user_bp, url_prefix='/users')

if __name__=='__main__':
    app.run(debug=True)