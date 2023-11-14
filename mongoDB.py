from pymongo import MongoClient

def save_to_mongodb(profiles_data):
    # Substitua 'sua_uri' pelo URI do seu banco de dados MongoDB
    client = MongoClient('mongodb://localhost:27017')

    # Escolha ou crie um banco de dados e uma coleção
    db = client[input('Digite o cliente: ')]
    collection = db[input('Digite a collection: ')]

    # Insira os perfis na coleção
    result = collection.insert_many(profiles_data)

    # Imprima os IDs dos documentos inseridos
    print(f"IDs dos documentos inseridos: {result.inserted_ids}")