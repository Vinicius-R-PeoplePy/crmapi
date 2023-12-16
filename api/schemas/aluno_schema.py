from api import ma
from ..models import aluno_model
from marshmallow import fields


class AlunoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = aluno_model.Aluno
        load_instance = True
        fields = ("nome", "profissao", "situacao", "email")

    nome = fields.String(required=True)
    profissao = fields.String(required=True)
    situacao = fields.String(required=True)
    email = fields.String(required=False)