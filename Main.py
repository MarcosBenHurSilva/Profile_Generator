from profile_data_generator import generate_profiles
from json_generator import save_to_json
from xlx_generator import save_to_excel
from mongoDB import *
    
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

        document_id = id
        updated_data = profiles_data

        option = chr(input("Selecione a operação a ser feita: Create(C), Read(R), Update(U) or Delete(D)").upper)
        
        match option:
            case "C":
                save_to_mongodb(profiles_data)
            case "R":
                read_from_mongodb()
            case "U":
                if num_profiles == 1:
                    update_mongodb_document(document_id, updated_data)
                else:
                    print("Somente atualize apenas um perfil por vez.")
            case "D":
                delete_mongodb_document(document_id)

    except ValueError:
        print("Por favor, insira um número válido para o número de perfis.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
