from xml.dom.expatbuilder import DOCUMENT_NODE
from profile_data_generator import generate_profiles
from json_generator import save_to_json
from xlx_generator import save_to_excel
from mongoDB import *
from bson.objectid import ObjectId  # Importe ObjectId para lidar com IDs do MongoDB
    
if __name__ == "__main__":
    try:
        option = input("Selecione a operação a ser feita: Create(C) ou Read(R): ").upper()
        
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
                updated_data = profiles_data
                save_to_mongodb(profiles_data)

            case "R":
                read_from_mongodb()

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
