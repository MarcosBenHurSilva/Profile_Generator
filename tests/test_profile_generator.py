import unittest
import sys
from pathlib import Path

# Obtém o diretório atual do script
script_dir = Path(__file__).resolve().parent

# Adiciona o diretório do script ao sys.path
sys.path.append(str(script_dir.parent))

from profile_data_generator import generate_profiles

class TestProfileGenerator(unittest.TestCase):
    def test_generate_profiles(self):
        # Testa se o gerador de perfis produz pelo menos um perfil
        num_profiles = 1
        profiles_data = generate_profiles(num_profiles)
        self.assertEqual(len(profiles_data), num_profiles)
        # Testa se o nome completo tem entre dois e seis palavras
        for profile in profiles_data:
            full_name = profile.get("Nome", "")
            num_words = len(full_name.split())
            self.assertGreaterEqual(num_words, 2, f"O nome '{full_name}' tem menos de duas palavras.")
            self.assertLessEqual(num_words, 6, f"O nome '{full_name}' tem mais de seis palavras.")
        # Testa se a idade é um número inteiro positivo menor que 101
        for profile in profiles_data:
            age = profile.get("Idade", None)
            self.assertIsNotNone(age, "A idade não está presente no perfil.")
            self.assertIsInstance(age, int, "A idade não é um número inteiro.")
            self.assertGreaterEqual(age, 0, "A idade não é um número inteiro positivo.")
            self.assertLess(age, 101, "A idade é maior ou igual a 101.")

if __name__ == '__main__':
    unittest.main()
