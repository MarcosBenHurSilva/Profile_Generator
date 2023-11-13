class ProfileDTO:
    def __init__(self, profile_id, full_name, age, birthday, gender, ethnicity, education, occupation, phone_number, cell_number, cpf, cep, is_valid):
        self.profile_id = profile_id
        self.full_name = full_name
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.ethnicity = ethnicity
        # self.mother_name = mother_name
        self.education = education
        self.occupation = occupation
        self.phone_number = phone_number
        self.cell_number = cell_number
        self.cpf = cpf
        self.cep = cep
        self.is_valid = is_valid

    def to_dict(self):
        return {
            "id": self.profile_id,
            "Nome": self.full_name,
            "Idade": self.age,
            "Data de Nascimento": self.birthday,
            "Gênero": self.gender,
            "Etnia": self.ethnicity,
            # "Nome da Mãe": self.mother_name,
            "Educação": self.education,
            "Ocupação": self.occupation,
            "Telefone": self.phone_number,
            "Celular": self.cell_number,
            "Cpf": self.cpf,
            "CEP": self.cep,
            "valid": self.is_valid
        }
