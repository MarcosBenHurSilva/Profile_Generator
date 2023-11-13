from pymongo import MongoClient
from profile_data_generator import generate_profiles
from json_generator import save_to_json
from xlx_generator import save_to_excel

def save_to_mongodb(profiles_data):
    # Substitua 'sua_uri' pelo URI do seu banco de dados MongoDB
    client = MongoClient('mongodb://localhost:27017')

    # Escolha ou crie um banco de dados e uma coleção
    db = client['Random_Profile']
    collection = db['Random_Profile']

    # Insira os perfis na coleção
    result = collection.insert_many(profiles_data)

    # Imprima os IDs dos documentos inseridos
    print(f"IDs dos documentos inseridos: {result.inserted_ids}")

    
    
if __name__ == "__main__":
    try:
        num_profiles = int(input("Digite o número de perfis a serem gerados: "))
        profiles_data = generate_profiles(num_profiles)

        json_filename = "perfis_generated.json"
        save_to_json(profiles_data, json_filename)
        print(f"{num_profiles} Perfis gerados e salvos em {json_filename}")

        xls_filename = "perfis_generated_openpyxl.xlsx"
        save_to_excel(profiles_data, xls_filename)
        print(f"{num_profiles} Perfis gerados e salvos em {xls_filename}")

        save_to_mongodb(profiles_data)

    except ValueError:
        print("Por favor, insira um número válido para o número de perfis.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
