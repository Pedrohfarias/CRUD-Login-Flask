import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from blacklist import BLACKLIST
from resources.usuario import User, UserLogin, UserLogout, UserRegister, Users

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
DEBUG = os.getenv("DEBUG")

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)

jwt = JWTManager(app)

api.add_resource(Users,'/usuarios')
api.add_resource(User,'/usuarios/<string:username>')
api.add_resource(UserRegister,'/cadastro')
api.add_resource(UserLogin,'/login')
api.add_resource(UserLogout,'/logout')

@app.before_first_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blocklist_loader
def verifica_blacklist(self,token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jat_payload):
    return jsonify({'message':'The user is logged out.'}),401

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug = (DEBUG == "True"))
