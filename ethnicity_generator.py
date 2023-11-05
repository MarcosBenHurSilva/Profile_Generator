import random

# Função para gerar etnia aleatória com base nas porcentagens
def generate_random_ethnicity(gender):
    if gender == "Masculino":
        ethnicity = random.choices(["Branco", "Preto", "Pardo", "Outro"], weights=[42.8, 10.6, 45.3, 1.3])[0]
    elif gender == "Feminino":
        ethnicity = random.choices(["Branca", "Preta", "Parda", "Outro"], weights=[42.8, 10.6, 45.3, 1.3])[0]
    else:
        ethnicity = random.choices(["Branco(a)", "Preto(a)", "Pardo(a)", "Outro"], weights=[42.8, 10.6, 45.3, 1.3])[0]
    
    return ethnicity
    
    