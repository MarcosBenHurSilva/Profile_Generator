import random

# Função para gerar número de telefone brasileiro
def generate_brazilian_phone_number():
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

    # Gerar número aleatório com 8 dígitos
    number = ''.join(random.choices("0123456789", k=8))

    # Formatar o número de telefone
    formatted_phone_number = f"({ddd}) 9{number[:3]}-{number[3:]}"

    return formatted_phone_number
