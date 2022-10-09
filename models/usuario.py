from sql_alchemy import banco


class UserModel(banco.Model):
    table_name = 'usuarios'

    login = banco.Column(banco.String(40), primary_key = True)
    senha = banco.Column(banco.String(40))
    nome = banco.Column(banco.String(40))
    admin = banco.Column(banco.Boolean,default=False)

    def __init__(self, login, senha, nome, admin):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.admin = admin

    def json(self):
        return {
        'nome':self.nome,
        'login': self.login,
        'admin':self.admin
        }

    @classmethod
    def find_all(cls):
        return [user.json() for user in cls.query.all()]


    @classmethod
    def find_user(cls, username):
        user = cls.query.filter_by(login=username).first()
        print(user)
        if user:
            return user
        else:
            return None
            

    @classmethod
    def find_by_login(cls, login):
        print(cls.senha)
        user = cls.query.filter_by(login=login).first()
        print(user)
        if user:
            return user
        else:
            return None
            
    def save_user(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()

    def update_user(self, login, senha, nome, admin):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.admin = admin
