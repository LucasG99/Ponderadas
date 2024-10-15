import pandas as pd

def calculate_demographic_data(print_data=True):
    # Defina os nomes das colunas manualmente
    column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
                    'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
                    'hours-per-week', 'native-country', 'salary']

    # Carregar o dataset e remover espaços extras
    df = pd.read_csv('adult.data.csv', names=column_names)

    # Remover espaços em branco das colunas 'race', 'sex' e 'education'
    df['race'] = df['race'].str.strip()
    df['sex'] = df['sex'].str.strip()
    df['education'] = df['education'].str.strip()

    # 1. Quantas pessoas de cada raça estão representadas neste conjunto de dados?
    race_count = df['race'].value_counts()

    # 2. Qual é a idade média dos homens?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. Qual a porcentagem de pessoas com diploma de Bacharelado?
    percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100

    # Imprimir alguns resultados
    if print_data:
        print("Número de pessoas por raça:\n", race_count)
        print("Idade média dos homens:", average_age_men)
        print(f"Porcentagem de pessoas com Bachelors: {percentage_bachelors:.1f}%")

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
    }

# Adicione esse bloco para rodar o código
if __name__ == "__main__":
    calculate_demographic_data(print_data=True)
