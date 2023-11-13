import random
import datetime

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

def generate_bithday(idade):
    # Obtém a data atual
    current_date = datetime.date.today()

    # Calcula o ano de nascimento com base na idade
    birth_year = current_date.year - idade

    # Gera um dia e mês de aniversário aleatórios
    birth_month = random.randint(1, 12)
    birth_month = random.randint(1, 12)
    max_day = 30 if birth_month in [4, 6, 9, 11] else 28 if birth_month == 2 else 31
    birth_day = random.randint(1, max_day)

    # Combina os componentes para formar a data de aniversário
    birthday = datetime.date(birth_year, birth_month, birth_day)

    # Formata a data como uma string 'dd/mm/aaaa'
    birthday_str = birthday.strftime('%d/%m/%Y')

    return birthday_str