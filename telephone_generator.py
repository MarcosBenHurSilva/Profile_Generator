import random

# Função para gerar número de telefone brasileiro
def generate_brazilian_telephone_number():
    
    # Gerar número aleatório com 8 dígitos
    number = ''.join(random.choices("0123456789", k=8))

    # Formatar o número de telefone
    formatted_phone_number = f" {number[:4]}-{number[4:]}"

    return formatted_phone_number
