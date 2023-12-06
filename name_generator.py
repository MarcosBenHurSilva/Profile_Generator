import random

# Lista de nomes masculinos
male_names = [
    "João", "Pedro", "Carlos", "Miguel", "Rafael",
    "Antônio", "Lucas", "Fernando", "Gustavo", "Felipe",
    "José", "Daniel", "Bruno", "André", "Eduardo",
    "Marcelo", "Thiago", "Ricardo", "Guilherme", "Paulo",
    "Roberto", "Vinícius", "Fábio", "Sérgio", "Ronaldo",
    "Gilberto", "Samuel", "Leandro", "Márcio", "Carlos",
    "Vitor", "Diego", "Luciano", "Raul", "Wagner",
    "Felipe", "Alexandre", "Lucas", "César", "Ricardo",
    "Caio", "Leonardo", "Renato", "Giovanni", "Joaquim",
    "Luis", "Hugo", "Fernando", "Raul", "Antônio",
    "Alberto", "Isaac", "Elias", "Thiago", "Sebastião",
    "Geraldo", "Álvaro", "Armando", "Arnaldo", "Vicente",
    "Roberto", "Sergio", "Wagner", "Anderson"
]
unique_male_names = list(set(male_names))

# Lista de nomes femininos
female_names = [
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
unique_female_names = list(set(female_names))

# Lista de sobrenomes
surnames = [
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
unique_surnames = list(set(surnames))

def generate_name_by_gender(gender):
    num_names = random.choices([1, 2], weights=[75, 25])[0]
    num_surnames = random.choices([1, 2, 3, 4], weights=[25, 60, 10, 5])[0]

    if gender == "Masculino":
        first_name = random.sample(unique_male_names, num_names)
    elif gender == "Feminino":
        first_name = random.sample(unique_female_names, num_names)
    else:  # Gênero não-binário
        first_name = random.sample(random.choice([unique_male_names, unique_female_names]), num_names)
    
    last_names = random.sample(unique_surnames, num_surnames)
    full_name = ' '.join(first_name + last_names)

    return full_name
