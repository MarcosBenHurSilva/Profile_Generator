import random

def generate_cep():
    # Gera os oito primeiros dígitos do CEP de forma aleatória
    cep = [random.randint(0, 9) for _ in range(8)]

    # Calcula o nono dígito verificador
    total = 0
    for i in range(8):
        total += cep[i] * (10 - i)
    remainder = total % 11
    if remainder < 2:
        cep.append(0)
    else:
        cep.append(11 - remainder)

    # Formata o CEP no padrão brasileiro (XXXXXXXX)
    cep_str = ''.join(map(str, cep))

    return cep_str
