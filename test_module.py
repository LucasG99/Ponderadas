import unittest
from demographic_data_analyzer import calculate_demographic_data

class TestDemographicDataAnalyzer(unittest.TestCase):

    def setUp(self):
        # Executa a função uma vez e armazena os resultados para serem usados em todos os testes
        self.result = calculate_demographic_data(print_data=False)

    def test_race_count(self):
        # Testa o número de pessoas por raça
        expected_race_count = {
            'White': 27816,
            'Black': 3124,
            'Asian-Pac-Islander': 1039,
            'Amer-Indian-Eskimo': 311,
            'Other': 271
        }
        self.assertEqual(self.result['race_count'].to_dict(), expected_race_count)

    def test_average_age_men(self):
        # Testa a idade média dos homens
        expected_average_age_men = 39.43
        self.assertAlmostEqual(self.result['average_age_men'], expected_average_age_men, places=2)

    def test_percentage_bachelors(self):
        # Testa a porcentagem de pessoas com Bacharelado
        expected_percentage_bachelors = 16.4
        self.assertAlmostEqual(self.result['percentage_bachelors'], expected_percentage_bachelors, places=1)

if __name__ == "__main__":
    unittest.main()
