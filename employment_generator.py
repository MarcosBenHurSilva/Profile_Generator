import random

# Funçaõ para gerar ocupação aleatória com base nas porcentagens
def generate_ramdom_ocuppation(idade):
    if idade >= 14:
        status = random.choices(["Desocupado", "Ocupado"], weights=[7.73, 92.27])[0]
        if status == "Ocupado":
            ocupation = random.choices(["Empregado: Setor privado (CLT)", "Empregado: Setor privado (sem CLT)", 
                                    "Empregado: Trabalhador doméstico (CLT)", "Empregado: Trabalhador doméstico (sem CLT)", 
                                    "Empregado: Setor público (CLT)", "Empregado: Setor público (sem CLT)", 
                                    "Empregado: Setor público (estatutário ou militar)", "Empregador: Com CNPJ",
                                    "Empregador: Sem CNPJ", "Autônomo: Com CNPJ", "Autônomo: Sem CNPJ",
                                    "Trabalhador familiar auxiliar"], weights=[37.36, 13.26, 1.44, 4.38, 1.39, 7.72, 3.1, 3.42, 0.79, 6.37, 19.11, 1.5])[0]
        else: ocupation = "Desocupado"
    elif idade < 14:
        ocupation = "Fora da força de trabalho"
    elif idade > 80:
        ocupation = "Aposentado"
    
    return ocupation