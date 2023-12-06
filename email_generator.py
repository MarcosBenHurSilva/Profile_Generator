import random
import string

email_domains = [
    "gmail.com", "outlook.com", "yahoo.com", "terra.com.br", "hotmail.com", "icloud.com",
    "aol.com", "protonmail.com", "yandex.com", "zoho.com", "mail.com",
    "gmx.com", "outlook.co.uk", "live.com", "me.com","bol.com.br", "ig.com.br", 
    "uol.com.br", "terra.com.br", "globomail.com",
    "r7.com", "oi.com.br", "brturbo.com.br", "superig.com.br", "ig.com",
    "pop.com.br", "zipmail.com.br", "oi.com", "yahoo.com.br", "sercomtel.com.br",
    "live.com.pt",
]

def generate_complement(length, include_numbers, include_symbols):
    number_chars = string.digits
    symbol_chars = "!#$%&"
    allowed_chars = ""
    complement = ""
    allowed_chars += number_chars if include_numbers else ""
    allowed_chars += symbol_chars if include_symbols else ""

    for _ in range(length):
        random_index = random.randint(0, len(allowed_chars) - 1)
        complement += allowed_chars[random_index]

    return complement

def generate_email_by_name(full_name, complement_length, include_numbers, include_symbols):
    num_nickname = random.choices([1, 2], weights=[75, 25])[0]
    weights = [20, 10, 5, 5, 10] + [1] * (len(email_domains) - 5)
    random_domain = random.choices(email_domains, weights=weights)[0]

    names = full_name.split(" ")

    if len(names) > 1:
        nickname = names[0] + "_" + names[-1]
    else:
        nickname = "_".join(names)

    complement = generate_complement(
        complement_length,
        include_numbers,
        include_symbols
    )

    return (nickname + complement + "@" + random_domain).replace(" ", "_")
