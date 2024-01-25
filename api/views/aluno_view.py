from flask_restful import Resource
from flask import request, make_response, jsonify

from .. schemas import aluno_schema
from .. entidades import aluno
from .. services import aluno_service
from api import api


class Alunos(Resource):
    def get(self):
        alunos = aluno_service.listar_alunos()
        service = aluno_schema.AlunoSchema(many=True)

        return make_response(service.jsonify(alunos), 200)

    def post(self):
        service = aluno_schema.AlunoSchema()
        validate = service.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        else:
            nome = request.json["nome"]
            data_nascimento = request.json["data_nascimento"]
            id_curso = request.json["id_curso"]

            novo_aluno = aluno.Aluno(nome=nome, data_nascimento=data_nascimento, id_curso=id_curso)
            resultado = aluno_service.cadastrar_aluno(novo_aluno)

            return make_response(service.jsonify(resultado), 201)

class AlunoDetail(Resource):
    def get(self, id_aluno):
        aluno = aluno_service.listar_aluno_id(id_aluno)
        if aluno is None:
            return make_response(jsonify("Aluno não encontrado."), 404)

        service = aluno_schema.AlunoSchema()
        return make_response(service.jsonify(aluno), 200)

    def put(self, id_aluno):
        aluno_db = aluno_service.listar_aluno_id(id_aluno)
        if aluno is None:
            return make_response(jsonify("Aluno não encontrado."), 400)

        service = aluno_schema.AlunoSchema()
        validate = service.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            data_nascimento = request.json["data_nascimento"]
            id_curso = request.json["id_curso"]
            novo_aluno = aluno.Aluno(nome=nome, data_nascimento=data_nascimento, id_curso=id_curso)
            aluno_service.atualizar_aluno(aluno_db, novo_aluno)
            aluno_atualizado = aluno_service.listar_aluno_id(id_aluno)

            return make_response(service.jsonify(aluno_atualizado), 200)

    def delete(self, id_aluno):
        aluno_db = aluno_service.listar_aluno_id(id_aluno)
        if aluno_db is None:
            return make_response(jsonify("Aluno não encontrado."), 404)
        aluno_service.remover_aluno(aluno_db)
        return make_response("Aluno removido com sucesso", 202)

api.add_resource(Alunos, '/alunos')
api.add_resource(AlunoDetail, '/alunos/<int:id_aluno>')