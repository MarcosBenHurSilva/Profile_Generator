import random

# Função para gerar o nivel de educação aleatório com base nas porcentagens
def generate_ramdom_educationLv(idade):
    if idade >= 25:
        level = random.choices(["Sem instrução", "Fundamental incompleto", 
                                "Fundamental completo", "Médio incompleto", 
                                "Médio completo", "Superior incompleto", 
                                "Superior completo"], weights=[6.0, 28.0, 7.8, 5.0, 29.9, 4.1, 19.2])[0]
    else:
        level = "Em idade escolar."

    return level