import random

# Lista de nomes femininos
mother_names = [
    "Maria", "Ana", "Luiza", "Isabela", "Larissa",
    "Camila", "Juliana", "Amanda", "Bianca", "Vanessa",
    "Renata", "Patrícia", "Aline", "Mônica", "Jessica",
    "Natália", "Leticia", "Thais", "Priscila", "Fernanda",
    "Andréa", "Cristina", "Cecília", "Helena", "Larissa",
    "Simone", "Mariana", "Cátia", "Tatiana", "Flávia",
    "Andressa", "Eduarda", "Rafaela", "Elaine", "Laura",
    "Vanessa", "Sandra", "Mônica", "Regina", "Larissa",
    "Isabela", "Márcia", "Tatiane", "Lorena", "Carla",
    "Patrícia", "Jéssica", "Ana", "Sueli", "Thais",
    "Priscila", "Fernanda", "Larissa", "Roberta", "Carolina",
    "Brenda", "Nathalia", "Amanda", "Karla", "Simone",
    "Valéria", "Eduarda", "Mariana", "Rosana", "Tânia"
]
unique_mother_names = list(set(mother_names))

# Lista de sobrenomes
mother_surnames = [
    "Silva", "Santos", "Oliveira", "Pereira", "Ribeiro", "Gomes", "Almeida", "Ferreira", "Carvalho",
    "Rodrigues", "Martins", "Fernandes", "Nunes", "Monteiro", "Cavalcanti", "Vieira", "Lima", "Sousa", "Barbosa",
    "Lopes", "Costa", "Correia", "Mendes", "Dias", "Castro", "Freitas", "Pinto", "Borges", "Moraes",
    "Sousa", "Pereira", "Nascimento", "Alves", "Rocha", "Ramos", "Pires", "Machado", "Nogueira", "Cardoso",
    "Andrade", "Ribeira", "Ferreira", "Mendes", "Correia", "Carvalho", "Lima", "Fernandes", "Barros", "Campos",
    "Moraes", "Nascimento", "Almeida", "Gonçalves", "Cavalcanti", "Vieira", "Dias", "Santana", "Pessoa", "Gomes",
    "Ramos", "Martins", "Rocha", "Nunes", "Lopes", "Dias", "Lima", "Carvalho", "Ribeira", "Andrade",
    "Ferreira", "Sousa", "Pereira", "Freitas", "Cardoso", "Pinto", "Santos", "Machado", "Nascimento", "Nogueira",
    "Borges", "Silveira", "Costa", "Alves", "Araújo", "Melo", "Gouveia", "Azevedo", "Campos", "Gonçalves"
]
unique_mother_surnames = list(set(mother_surnames))


def generate_mother_by_name(full_name):
    num_names = random.choices([1, 2], weights=[75, 25])[0]
    num_surnames = random.choices([1, 2, 3, 4], weights=[25, 60, 10, 5])[0]
    names = full_name.split(" ")
    
    if len(names) > 2:
        first_name = random.choice(unique_mother_names, num_names)
        last_name = random.choice(names[2:])
        unique_last_name = random.choice(unique_mother_surnames, num_surnames)
        return first_name + " " + last_name + " " + unique_last_name
    elif len(names) == 2:
        first_name = random.choice(unique_mother_names, num_names)
        last_name = random.choice(names[1:])
        unique_last_name = random.choice(unique_mother_surnames, num_surnames)
        return first_name + " " + last_name + " " + unique_last_name
    else:
        return random.choice(unique_mother_names, num_names) + " " + random.choice(unique_mother_surnames)
