from pymongo import MongoClient
from bson.objectid import ObjectId  # Importe ObjectId para lidar com IDs do MongoDB

def save_to_mongodb(profiles_data):
    # Substitua 'sua_uri' pelo URI do seu banco de dados MongoDB
    client = MongoClient('mongodb://localhost:27017')

    # Escolha ou crie um banco de dados e uma coleção
    db = client[input('Digite o cliente: ')] # client = tudo_junto
    collection = db[input('Digite a collection: ')] # collection = tudo_junto

    # Insira os perfis na coleção
    result = collection.insert_many(profiles_data)

    # Imprima os IDs dos documentos inseridos
    #print(f"IDs dos documentos inseridos: {result.inserted_ids}")

def read_from_mongodb():
    client = MongoClient('mongodb://localhost:27017')
    db = client[input('Digite o cliente: ')]
    collection = db[input('Digite a collection: ')]

    # Consulta todos os documentos na coleção
    documents = collection.find()

    # Imprime os documentos
    for doc in documents:
        print(doc)

def update_mongodb_document(document_id, updated_data):
    client = MongoClient('mongodb://localhost:27017')
    db = client[input('Digite o cliente: ')]
    collection = db[input('Digite a collection: ')]

    # Certifique-se de que o document_id seja um ObjectId válido
    document_id = ObjectId(document_id)

    # Atualiza o documento com o ID fornecido
    collection.update_one({"_id": document_id}, {"$set": updated_data})

def delete_mongodb_document(document_id):
    client = MongoClient('mongodb://localhost:27017')
    db = client[input('Digite o cliente: ')]
    collection = db[input('Digite a collection: ')]

    # Certifique-se de que o document_id seja um ObjectId válido
    document_id = ObjectId(document_id)

    # Exclui o documento com o ID fornecido
    collection.delete_one({"_id": document_id})
