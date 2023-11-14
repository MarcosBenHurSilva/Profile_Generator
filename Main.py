from profile_data_generator import generate_profiles
from json_generator import save_to_json
from xlx_generator import save_to_excel
from mongoDB import save_to_mongodb
    
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
