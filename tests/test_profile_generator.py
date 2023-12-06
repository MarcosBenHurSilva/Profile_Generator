import unittest
from profile_data_generator import generate_profiles

class TestProfileGenerator(unittest.TestCase):
    def test_generate_profiles(self):
        # Testa se o gerador de perfis produz pelo menos um perfil
        num_profiles = 1
        profiles_data = generate_profiles(num_profiles)
        self.assertEqual(len(profiles_data), num_profiles)

        # Adicionar mais casos de teste

if __name__ == '__main__':
    unittest.main()
