import random

# Função para gerar gênero aleatório com base nas porcentagens
def generate_random_gender():
    gender = random.choices(["Masculino", "Feminino", "Não-Binário"], weights=[48, 50, 2])[0]
    return gender
