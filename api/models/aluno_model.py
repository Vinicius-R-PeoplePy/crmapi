from api import db


class Aluno(db.Model):
    __tablename__ = "aluno"
    id_aluno = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    id_curso = db.Column(db.Integer, autoincrement=True, nullable=False)

