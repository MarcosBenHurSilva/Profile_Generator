import random
import json
from openpyxl import Workbook

from gender_generator import generate_random_gender
from name_generator import generate_name_by_gender
from cpf_generator import generate_cpf
from cpf_generator import validate_cpf
from age_generator import generate_random_age
from age_generator import generate_bithday
from cep_generator import generate_cep
from ethnicity_generator import generate_random_ethnicity
from educationLv_generator import generate_ramdom_educationLv
from employment_generator import generate_ramdom_ocupation
from mother_generator import generate_mother_by_name
from telephone_number_generator import generate_brazilian_phone_number
from telephone_generator import generate_brazilian_telephone_number

# Solicita ao usuário o número de perfis a serem gerados
num_perfil = int(input("Digite o número de perfis a serem gerados: "))

# Gera os perfis
perfis_data = []
for i in range(num_perfil):
    # Códigos de DDD do Brasil
    ddd_list = [
        "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "21", "22", "24", "27", "28", "31", "32", "33", "34", "35",
        "37", "38", "41", "42", "43", "44", "45", "46", "47", "48",
        "49", "51", "53", "54", "55", "61", "62", "63", "64", "65",
        "66", "67", "68", "69", "71", "73", "74", "75", "77", "79",
        "81", "82", "83", "84", "85", "86", "87", "88", "89", "91",
        "92", "93", "94", "95", "96", "97", "98", "99"
    ]

    # Gerar DDD aleatório
    ddd = random.choice(ddd_list)
    gender = generate_random_gender()
    full_name = generate_name_by_gender(gender)
    cpf = generate_cpf()
    is_valid = validate_cpf(cpf)
    idade = generate_random_age()
    aniversario = generate_bithday(idade)
    etnia = generate_random_ethnicity(gender)
    mae = generate_mother_by_name(full_name)
    educacao = generate_ramdom_educationLv(idade)
    ocupation = generate_ramdom_ocupation(idade)
    telefone = generate_brazilian_telephone_number()
    celular = generate_brazilian_phone_number()
    valid_cep = generate_cep()
    perfis_data.append(
        {"id": i + 1, "Nome": full_name, "Idade": idade, "Data de Nascimento": aniversario, "Gênero": gender, 
         "Etnia": etnia, "Nome da Mãe": mae, "Educação": educacao, "Ocupação": ocupation, "Telefone": ddd + telefone, "Celular": ddd + celular, "Cpf": cpf, "CEP": valid_cep, "valid": is_valid})

# Cria um arquivo JSON com os perfis gerados
json_filename = "perfis_generated.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(perfis_data, json_file, ensure_ascii=False, indent=2)

print(f"{num_perfil} Perfis gerados e salvos em {json_filename}")

# Crie um arquivo de planilha
wb = Workbook()
ws = wb.active

# Adicione cabeçalhos
ws.append(["ID", "Nome", "Idade", "Data de Nascimento", "Gênero", "Etnia","Nome da Mãe", "Educação", "Ocupação","Telefone","Celular", "CPF", "CEP"])

# Adicione os perfis aos dados
for perfil in perfis_data:
    ws.append([perfil["id"], perfil["Nome"], perfil["Idade"], perfil["Data de Nascimento"], perfil["Gênero"], 
               perfil["Etnia"],perfil["Nome da Mãe"] , perfil["Educação"], perfil["Ocupação"],perfil["Telefone"], perfil["Celular"], perfil["Cpf"], perfil["CEP"]])

# Especifique o caminho do arquivo .xls
xls_filename = "perfis_generated_openpyxl.xlsx"

# Salve a planilha no arquivo
wb.save(xls_filename)

print(f"{num_perfil} Perfis gerados e salvos em {xls_filename}")