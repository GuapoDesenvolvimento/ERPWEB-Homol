from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return Usuario.query.filter_by(id=user_id).first()

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    __table_args__ = {"schema": "erpweb"}
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    dt_inclusao = db.Column(db.DateTime, nullable=False)

    def __init__(self, nome, email, cpf, password, dt_inclusao):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.password = generate_password_hash(password)
        self.dt_inclusao = dt_inclusao

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
