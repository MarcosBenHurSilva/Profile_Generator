import random

# Lista de nomes femininos
mother_names = [
    "Maria",
    "Ana",
    "Luiza",
    "Isabela",
    "Larissa",
    "Camila",
    "Juliana",
    "Amanda",
    "Bianca",
    "Vanessa",
    "Renata",
    "Patrícia",
    "Aline",
    "Mônica",
    "Jessica",
    "Natália",
    "Leticia",
    "Thais",
    "Priscila",
    "Fernanda",
    "Andréa",
    "Cristina",
    "Cecília",
    "Helena",
    "Larissa",
    "Simone",
    "Mariana",
    "Cátia",
    "Tatiana",
    "Flávia",
    "Andressa",
    "Eduarda",
    "Rafaela",
    "Elaine",
    "Laura",
    "Vanessa",
    "Sandra",
    "Mônica",
    "Regina",
    "Larissa",
    "Isabela",
    "Márcia",
    "Tatiane",
    "Lorena",
    "Carla",
    "Patrícia",
    "Jéssica",
    "Ana",
    "Sueli",
    "Thais",
    "Priscila",
    "Fernanda",
    "Larissa",
    "Roberta",
    "Carolina",
    "Brenda",
    "Nathalia",
    "Amanda",
    "Karla",
    "Simone",
    "Valéria",
    "Eduarda",
    "Mariana",
    "Rosana",
    "Tânia",
]
unique_mother_names = list(set(mother_names))

# Lista de sobrenomes
mother_surnames = [
    "Silva",
    "Santos",
    "Oliveira",
    "Pereira",
    "Ribeiro",
    "Gomes",
    "Almeida",
    "Ferreira",
    "Carvalho",
    "Rodrigues",
    "Martins",
    "Fernandes",
    "Nunes",
    "Monteiro",
    "Cavalcanti",
    "Vieira",
    "Lima",
    "Sousa",
    "Barbosa",
    "Lopes",
    "Costa",
    "Correia",
    "Mendes",
    "Dias",
    "Castro",
    "Freitas",
    "Pinto",
    "Borges",
    "Moraes",
    "Sousa",
    "Pereira",
    "Nascimento",
    "Alves",
    "Rocha",
    "Ramos",
    "Pires",
    "Machado",
    "Nogueira",
    "Cardoso",
    "Andrade",
    "Ribeira",
    "Ferreira",
    "Mendes",
    "Correia",
    "Carvalho",
    "Lima",
    "Fernandes",
    "Barros",
    "Campos",
    "Moraes",
    "Nascimento",
    "Almeida",
    "Gonçalves",
    "Cavalcanti",
    "Vieira",
    "Dias",
    "Santana",
    "Pessoa",
    "Gomes",
    "Ramos",
    "Martins",
    "Rocha",
    "Nunes",
    "Lopes",
    "Dias",
    "Lima",
    "Carvalho",
    "Ribeira",
    "Andrade",
    "Ferreira",
    "Sousa",
    "Pereira",
    "Freitas",
    "Cardoso",
    "Pinto",
    "Santos",
    "Machado",
    "Nascimento",
    "Nogueira",
    "Borges",
    "Silveira",
    "Costa",
    "Alves",
    "Araújo",
    "Melo",
    "Gouveia",
    "Azevedo",
    "Campos",
    "Gonçalves",
]
unique_mother_surnames = list(set(mother_surnames))


def generate_mother_by_name(full_name):
    # num_mother_names = random.choices([1, 2], weights=[75, 25])[0]
    # num_mother_surnames = random.choices([1, 2], weights=[35, 65])[0]
    # shared_num_mother_surnames = random.choices([0, 1, 2], weights=[30, 65, 5])[0]
    # first_mother_name = random.sample(unique_mother_names, num_mother_names)
    # # Compartilhando pelo menos um sobrenome com o perfil principal
    # shared_surname = random.choice(full_name.split()[1:])
    # shared_last_names = random.sample(shared_surname, shared_num_mother_surnames)
    # mother_last_names = random.sample(unique_mother_surnames, num_mother_surnames)
    # full_mother_name = ' '.join(first_mother_name + mother_last_names + shared_last_names)

    num_mother_names = random.choices([1, 2], weights=[75, 25])[0]
    num_mother_surnames = random.choices([1, 2, 3, 4], weights=[25, 40, 25, 10])[0]
    shared_num_mother_surnames = min(num_mother_surnames, len(full_name.split()) - 1)
    
    # Primeiro nome da mãe
    first_mother_name = random.sample(unique_mother_names, num_mother_names)
    
    # Sobrenomes compartilhados
    # shared_last_names = random.sample(set(full_name.split()[1:]), shared_num_mother_surnames)
    shared_last_names = random.sample(list(set(full_name.split()[1:])), shared_num_mother_surnames)
    mother_last_names = random.sample(list(set(unique_mother_surnames) - set(shared_last_names)), num_mother_surnames - shared_num_mother_surnames)


    
    # Sobrenomes exclusivos da mãe
    # mother_last_names = random.sample(set(unique_mother_surnames) - set(shared_last_names), num_mother_surnames - shared_num_mother_surnames)
    
    # Combinando o nome completo da mãe
    full_mother_name = ' '.join(first_mother_name + mother_last_names + shared_last_names)
    
    return full_mother_name
