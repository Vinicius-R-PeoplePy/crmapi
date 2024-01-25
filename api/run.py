from api import app
from flask_restful import Api

api = Api(app)

import psycopg2

conexao = psycopg2.connect(database = "postgres",
                           host = "localhost",
                           user = "postgres",
                           password = "123456789",
                           port = "5432"
                           )
print("Conexão com Postgres:")
print(conexao.info)

if __name__ == '__main__':
    app.run()

