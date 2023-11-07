import random
import json
from openpyxl import Workbook

from gender_generator import generate_random_gender
from name_generator import generate_name_by_gender
from cpf_generator import generate_cpf
from cpf_generator import validate_cpf
from age_generator import generate_random_age
from cep_generator import generate_cep
from ethnicity_generator import generate_random_ethnicity
from educationLv_generator import generate_ramdom_educationLv
from employment_generator import generate_ramdom_ocupation

# Solicita ao usuário o número de perfis a serem gerados
num_perfil = int(input("Digite o número de perfis a serem gerados: "))

# Gera os perfis
perfis_data = []
for i in range(num_perfil):
    gender = generate_random_gender()
    full_name = generate_name_by_gender(gender)
    cpf = generate_cpf()
    is_valid = validate_cpf(cpf)
    idade = generate_random_age()
    etnia = generate_random_ethnicity(gender)
    educacao = generate_ramdom_educationLv(idade)
    ocupation = generate_ramdom_ocupation(idade)
    valid_cep = generate_cep()
    perfis_data.append(
        {"id": i + 1, "Nome": full_name, "Idade": idade, "Gênero": gender, 
         "Etnia": etnia, "Educação": educacao, "Ocupação": ocupation, "Cpf": cpf, "CEP": valid_cep, "valid": is_valid})

# Cria um arquivo JSON com os perfis gerados
json_filename = "perfis_generated.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(perfis_data, json_file, ensure_ascii=False, indent=2)

print(f"{num_perfil} Perfis gerados e salvos em {json_filename}")

# Crie um arquivo de planilha
wb = Workbook()
ws = wb.active

# Adicione cabeçalhos
ws.append(["ID", "Nome", "Idade", "Gênero", "Etnia", "Educação", "Ocupação", "CPF", "CEP"])

# Adicione os perfis aos dados
for perfil in perfis_data:
    ws.append([perfil["id"], perfil["Nome"], perfil["Idade"], perfil["Gênero"], 
               perfil["Etnia"], perfil["Educação"], perfil["Ocupação"], perfil["Cpf"], perfil["CEP"]])

# Especifique o caminho do arquivo .xls
xls_filename = "perfis_generated_openpyxl.xlsx"

# Salve a planilha no arquivo
wb.save(xls_filename)

print(f"{num_perfil} Perfis gerados e salvos em {xls_filename}")