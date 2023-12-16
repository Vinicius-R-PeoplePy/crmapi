from flask_restful import Resource
from flask import request, make_response, jsonify

from .. schemas import aluno_schema
from .. entidades import aluno
from .. services import aluno_service
from api import api


class Alunos(Resource):
    def get(self):
        return 'Teste de API 04'

    def post(self):
        cs = aluno_schema.AlunoSchema()
        validate = cs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        else:
            nome = request.json["nome"]
            profissao = request.json["profissao"]
            situacao = request.json["situacao"]
            email = request.json["email"]

            novo_aluno = aluno.Aluno(nome=nome, profissao=profissao, situacao=situacao, email=email)
            resultado = aluno_service.cadastrar_aluno(novo_aluno)

            return make_response(cs.jsonify(resultado), 201)


api.add_resource(Alunos, '/alunos')