import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Carregar o dataset
    data = pd.read_csv('epa-sea-level.csv')

    # Criar o gráfico de dispersão
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Regressão linear para todos os dados
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    
    # Previsão até 2050
    years_extended = pd.Series(range(1880, 2051))
    sea_levels_extended = intercept + slope * years_extended
    
    # Plotar a linha de melhor ajuste (1880-2050)
    plt.plot(years_extended, sea_levels_extended, color='r', label='Best fit line (1880-2050)')

    # Regressão linear desde 2000
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    
    # Previsão até 2050 com os dados recentes (2000-2050)
    sea_levels_recent = intercept_recent + slope_recent * years_extended
    plt.plot(years_extended, sea_levels_recent, color='green', label='Best fit line (2000-2050)')

    # Ajustes de eixo e título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Adicionar legenda
    plt.legend()

    # Salvar a imagem como 'sea_level_plot.png'
    plt.savefig('sea_level_plot.png')

    # Mostrar o gráfico (opcional, útil para depuração)
    plt.show()

    # Retornar o eixo atual (para os testes)
    return plt.gca()

if __name__ == "__main__":
    draw_plot()