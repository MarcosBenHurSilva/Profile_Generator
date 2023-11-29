from openpyxl import Workbook

def save_to_excel(profiles, filename):
    wb = Workbook()
    ws = wb.active

    headers = ["ID", "Nome", "Idade", "Senha", "Data de Nascimento", "Gênero", "Etnia", # "Nome da Mãe",
               "Educação", "Ocupação", "Telefone", "Celular", "CPF", "CEP"]

    ws.append(headers)

    # Adicione os perfis aos dados
    for profile in profiles:
        ws.append([profile["id"], profile["Nome"], profile["Idade"], profile["Senha"], profile["Data de Nascimento"], profile["Gênero"], 
                profile["Etnia"],#profile["Nome da Mãe"]
                profile["Educação"], profile["Ocupação"],profile["Telefone"], 
                profile["Celular"], profile["Cpf"], profile["CEP"]])

    wb.save(filename)
    