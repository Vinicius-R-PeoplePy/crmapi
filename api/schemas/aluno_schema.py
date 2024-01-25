from api import ma
from ..models import aluno_model
from marshmallow import fields


class AlunoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = aluno_model.Aluno
        load_instance = True
        fields = ("id_aluno", "nome", "data_nascimento", "id_curso")

    nome = fields.String(required=True)
    data_nascimento = fields.Date(required=True)
    id_curso = fields.Integer(required=True)