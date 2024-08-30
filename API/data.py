import mysql.connector
import json
import os

class Banco:
    @staticmethod
    def iniciar_conexao_banco():
        try:
            # Supondo que os dados do banco estejam em um arquivo JSON ou sejam carregados de outro lugar
            with open('config.json', 'r') as f:
                dados_banco = json.load(f)
                
            conexao = mysql.connector.connect(
                host=dados_banco['host'],
                user=dados_banco['user'],
                password=dados_banco['password'],
                database=dados_banco['database']
            )
            return conexao
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            return None

    @staticmethod
    def listar_estados():
        conexao = Banco.iniciar_conexao_banco()
        if conexao is None:
            return None
        
        try:
            with conexao.cursor() as cursor:
                query = "SELECT id, sigla, nome, capital FROM estados ORDER BY nome ASC;"
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows:
                    keys = [column[0] for column in cursor.description]
                    result = [dict(zip(keys, row)) for row in rows]
                return result
        except mysql.connector.Error as err:
            print(f"Erro ao executar a query: {err}")
            return None
        finally:
            conexao.close()

