import random

# Taxas de ocupação/desocupação
percentages = {
    "Desocupada": 7.7,
    "Ocupada": 57.1,
    "Fora da força de trabalho": 35.2
}

# Funçaõ para gerar ocupação aleatória com base nas porcentagens

def generate_ramdom_ocupation(idade):
    if idade >= 14:
        ocupation = random.choices(["Sem ocupação", "Empregado: Setor privado (CLT)", "Empregado: Setor privado (sem CLT)", 
                                "Empregado: Trabalhador doméstico (CLT)", "Empregado: Trabalhador doméstico (sem CLT)", "Médio incompleto", 
                                "Empregado: Setor publico (CLT)", "Empregado: Setor publico (sem CLT)", 
                                "Empregado: Setor ublico (estatutário ou militar)", "Empregador: Com CNPJ",
                                "Empregador: Sem CNPJ", "Autonomo: Com CNPJ", "Autonomo: Sem CNPJ",
                                "Trabalhador familiar auxiliar"], weights=[6.0, 28.0, 7.8, 5.0, 29.9, 4.1, 19.2])[0]