# import psycopg2
# from psycopg2 import sql
# # from Data_Transfer_Object import ProfileDTO

# # Defina suas credenciais de banco de dados
# db_config = {
#     'dbname': 'Ramdom_Profiles',
#     'user': 'postgres',
#     'password': 'xxxx',
#     'host': 'localhost',
#     'port': '5432'
#      }

# def save_to_database(profiles):
#     # Conecte-se ao banco de dados
#     connection = psycopg2.connect(**db_config)
#     cursor = connection.cursor()

#     try:
#         # Crie a tabela se ainda não existir
#         create_table_query = """
#         CREATE TABLE IF NOT EXISTS profiles (
#             id SERIAL PRIMARY KEY,
#             nome VARCHAR,
#             idade INTEGER,
#             data_nascimento DATE,
#             genero VARCHAR,
#             etnia VARCHAR,
#             educacao VARCHAR,
#             ocupacao VARCHAR,
#             telefone VARCHAR,
#             celular VARCHAR,
#             cpf VARCHAR,
#             cep VARCHAR,
#             is_valid BOOLEAN
#         );
#         """
#         cursor.execute(create_table_query)
#         connection.commit()

#         # Insira os perfis na tabela
#         insert_query = sql.SQL("""
#         INSERT INTO profiles (
#             id, nome, idade, data_nascimento, genero, etnia,
#             educacao, ocupacao, telefone, celular, cpf, cep, is_valid
#         ) VALUES (
#             %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
#         );
#         """)

#         for profile in profiles:
#             cursor.execute(insert_query, (
#                 profile['id'], profile['Nome'], profile['Idade'],
#                 profile['Data de Nascimento'], profile['Gênero'],
#                 profile['Etnia'], profile['Educação'], profile['Ocupação'],
#                 profile['Telefone'], profile['Celular'], profile['Cpf'],
#                 profile['CEP'], profile['valid']
#             ))

#         connection.commit()
#         print("Dados inseridos no banco de dados com sucesso!")

#     except Exception as e:
#         print(f"Erro ao inserir dados no banco de dados: {str(e)}")

#     finally:
#         # Feche a conexão
#         cursor.close()
#         connection.close()


