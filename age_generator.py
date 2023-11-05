import random

# Porcentagens por faixa etária
percentages = {
    "0-14 anos": 28.2,
    "15-24 anos": 45.7,
    "25-54 anos": 50.6,
    "55-64 anos": 6.2,
    "65 anos ou mais": 9.5
}


# Função para gerar idade aleatória com base nas porcentagens
def generate_random_age():
    rand_num = random.uniform(0, 100)  # Gera um número aleatório entre 0 e 100

    if rand_num <= percentages["0-14 anos"]:
        return random.randint(0, 14)
    elif rand_num <= percentages["0-14 anos"] + percentages["15-24 anos"]:
        return random.randint(15, 24)
    elif rand_num <= percentages["0-14 anos"] + percentages["15-24 anos"] + percentages["25-54 anos"]:
        return random.randint(25, 54)
    elif rand_num <= percentages["0-14 anos"] + percentages["15-24 anos"] + percentages["25-54 anos"] + percentages[
        "55-64 anos"]:
        return random.randint(55, 64)
    else:
        return random.randint(65, 100)