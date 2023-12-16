from api import db


class Aluno(db.Model):
    __tablename__ = "aluno"
    id_aluno = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    profissao = db.Column(db.String(100), nullable=False)
    situacao = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=True)

