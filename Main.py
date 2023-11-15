from xml.dom.expatbuilder import DOCUMENT_NODE
from profile_data_generator import generate_profiles
from json_generator import save_to_json
from xlx_generator import save_to_excel
from mongoDB import *
from bson.objectid import ObjectId  # Importe ObjectId para lidar com IDs do MongoDB
    
if __name__ == "__main__":
    try:
        option = input("Selecione a operação a ser feita: Create(C), Read(R), Update(U) or Delete(D): ").upper()
        
        match option:
            case "C":
                num_profiles = int(input("Digite o número de perfis a serem gerados: "))
                profiles_data = generate_profiles(num_profiles)

                json_filename = "perfis_generated.json"
                save_to_json(profiles_data, json_filename)
                print(f"{num_profiles} Perfis gerados e salvos em {json_filename}")

                xls_filename = "perfis_generated_openpyxl.xlsx"
                save_to_excel(profiles_data, xls_filename)
                print(f"{num_profiles} Perfis gerados e salvos em {xls_filename}")

                # Certifique-se de que o document_id seja um ObjectId válido
                document_id = input("Digite o ID do documento que deseja atualizar (ou deixe em branco para criar um novo): ")
                updated_data = profiles_data
                save_to_mongodb(profiles_data)
            case "R":
                read_from_mongodb()
            case "U":
                if num_profiles == 1:
                    update_mongodb_document(document_id, updated_data, id_key='id')
                else:
                    print("Somente atualize apenas um perfil por vez.")
            case "D":
                delete_mongodb_document(document_id, id_key='id')

    except ValueError:
        print("Por favor, insira um número válido para o número de perfis.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
