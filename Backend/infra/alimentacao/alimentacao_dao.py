# Imports
import sqlite3
import pyodbc
from contextlib import closing

# String de conexão com Banco
server = "coel.database.windows.net"
database = "Aplicativo"
username = "Adriano"
password = "Coelmatic01"
driver = '{SQL Server}'

str_conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                          ';DATABASE='+database+';UID='+username+';PWD=' + password)


# Tabela
model_name = "alimentacao"


# Query que lista tudo da tabela
def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id_alimentacao, alimentacao) in rows:
                registros.append(
                    {"id_alimentacao": id_alimentacao, "alimentacao": alimentacao})
            return registros


# Query que consulta por ID a tabela
def consultar(id):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM {model_name} WHERE id_alimentacao = ?", (id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return ({"id_alimentacao": row[0], "alimentacao": row[1]})
