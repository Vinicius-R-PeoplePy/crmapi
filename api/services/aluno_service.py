from ..models import aluno_model
from api import db

def cadastrar_aluno(aluno):
   aluno_db = aluno_model.Aluno(
        nome=aluno.nome,
        profissao=aluno.profissao,
        situacao=aluno.situacao,
        email = aluno.email
    )

   db.session.add(aluno_db)
   db.session.commit()
   return aluno_db

