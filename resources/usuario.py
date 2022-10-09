from blacklist import BLACKLIST
from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from flask_restful import Resource, reqparse
from models.usuario import UserModel
from utils import hash

#from werkzeug.security import safe_str_cmp

atributos = reqparse.RequestParser()
atributos.add_argument('nome')
atributos.add_argument('login', type=str, required=True, help="The 'login' field cannot be left blank.")
atributos.add_argument('senha', type=str, required=True, help="The 'senha' field cannot be left blank.")
atributos.add_argument('admin',type = bool, default = False)

class Users(Resource):
    #/usuarios
    def get(self):
        return {'Users': UserModel.find_all()}

class User(Resource):
    #/usuarios/<user_id>
    def get(self, username):
        user = UserModel.find_user(username)
        if user :
            return user.json()
        else:
            return {'message':'User not found.'},404

    def put(self, username):
        user = UserModel.find_user(username)
        if(user):
            #Pegando os dados novamente para que seja possivel enviar o payload sem o campo login
            atributos = reqparse.RequestParser()
            atributos.add_argument('nome')
            atributos.add_argument('senha', type=str, required=True, help="The 'senha' field cannot be left blank.")
            atributos.add_argument('admin',type = bool, default = False)
            dados = atributos.parse_args()
            #Setando o login como o username do próprio usuário , para que não seja possivel alterar o login
            # e nem permitir login duplicado, ou seja, mesmo que venha um login diferente no payload, não vai
            # ser alterado por que é primary key
            dados['login'] = username
            #Aplicando Hash na senha
            dados['senha'] = hash.generate_hash(dados['senha'])
            dados['senha'] =  dados['senha'].decode("utf-8", "ignore")
            user.update_user(**dados)
            user.save_user()
            return user.json(), 200
        else:
            return {'message':'User not found.'}

    @jwt_required()
    def delete(self, username):
        user = UserModel.find_user(username)
        if user:
            user.delete_user()
            return {'message':'User deleted.'}
        else:
            return {'message':'User not found.'},404



class UserRegister(Resource):
    #/cadastro
    def post(self):

        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {'message':f"The login {dados['login']} already exists."}
        else:
            dados['senha'] = hash.generate_hash(dados['senha'])
            dados['senha'] =  dados['senha'].decode("utf-8", "ignore")
            print("\n\n\n dados senha:"+dados['senha']+"\n\n\n")

            user = UserModel(**dados)
            user.save_user()
            return {'message':'User created successfully.'},201


class UserLogin(Resource):
    
    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_login(dados['login'])

        if user and hash.check_hash(dados['senha'], user.senha):
            token_de_acesso = create_access_token(identity = user.login)
            return {'access_token':token_de_acesso},200
        return {'message':'The username or password is incorrect.'},401

class UserLogout(Resource):
    
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {'message':'Successfully logged out.'}, 200
