from gender_generator import generate_random_gender
from name_generator import generate_name_by_gender
from cpf_generator import generate_cpf
from password_generator import generate_password
from cpf_generator import validate_cpf
from age_generator import generate_random_age
from age_generator import generate_birthday
from cep_generator import generate_cep
from ethnicity_generator import generate_random_ethnicity
from educationLv_generator import generate_ramdom_educationLv
from employment_generator import generate_ramdom_ocuppation
# from mother_generator import generate_mother_by_name
from telephone_number_generator import generate_brazilian_phone_number
from telephone_generator import generate_brazilian_telephone_number
from ddd_generator import generate_ddd
# from Data_Transfer_Object import ProfileDTO

def generate_profiles(num_profiles):
    profiles = []
    for i in range(num_profiles):
        gender = generate_random_gender()
        full_name = generate_name_by_gender(gender)
        cpf = generate_cpf()
        password = generate_password(12, any, any, any, any)
        is_valid = validate_cpf(cpf)
        age = generate_random_age()
        birthday = generate_birthday(age)
        ethnicity = generate_random_ethnicity(gender)
        # mother_name = generate_mother_by_name(full_name)
        education = generate_ramdom_educationLv(age)
        occupation = generate_ramdom_ocuppation(age)
        ddd = generate_ddd()
        phone_number = generate_brazilian_telephone_number()
        cell_number = generate_brazilian_phone_number()
        valid_cep = generate_cep()

        profiles.append({
            "id": i + 1, "Nome": full_name, "Idade": age, "Senha": password, "Data de Nascimento": birthday,
            "Gênero": gender, "Etnia": ethnicity, #"Nome da Mãe": mother_name,
            "Educação": education, "Ocupação": occupation, "Telefone": ddd + phone_number,
            "Celular": ddd + cell_number, "Cpf": cpf, "CEP": valid_cep, "valid": is_valid
        })

        # # Crie uma instância do ProfileDTO
        # profile_dto = ProfileDTO(
        #     i + 1, full_name, age, birthday, gender, ethnicity,
        #     education, occupation, ddd + phone_number, ddd + cell_number, cpf, valid_cep, is_valid
        # )

        # # Adicione o dicionário do DTO à lista de perfis
        # profiles.append(profile_dto.to_dict())

    return profiles