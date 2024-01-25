from ..models import aluno_model
from api import db

def cadastrar_aluno(aluno):
   aluno_db = aluno_model.Aluno(
        nome=aluno.nome,
        data_nascimento=aluno.data_nascimento,
        id_curso=aluno.id_curso
    )

   db.session.add(aluno_db)
   db.session.commit()
   return aluno_db

def listar_alunos():
    alunos = aluno_model.Aluno.query.all()
    return alunos

def listar_aluno_id(id_aluno):
    aluno = aluno_model.Aluno.query.filter_by(id_aluno=id_aluno).first()
    return aluno

def atualizar_aluno(aluno_anterior, aluno_novo):
    aluno_anterior.nome = aluno_novo.nome
    aluno_anterior.data_nascimento = aluno_novo.data_nascimento
    aluno_anterior.id_curso = aluno_novo.id_curso
    db.session.commit()

def remover_aluno(id_aluno):
    db.session.delete(id_aluno)
    db.session.commit()

