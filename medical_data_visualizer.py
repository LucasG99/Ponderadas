import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o dataset
df = pd.read_csv('medical_examination.csv')

# Criar a coluna 'overweight'
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)) > 25
df['overweight'] = df['overweight'].astype(int)

# Normalizando as colunas 'cholesterol' e 'gluc'
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Salvar o DataFrame atualizado em um arquivo CSV
df.to_csv('medical_examination.csv', index=False)

# Função para desenhar o gráfico categórico
def draw_cat_plot():
    # Criar o DataFrame usando pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Agrupar os dados e renomear a coluna de contagem
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size().rename(columns={'size': 'total'})

    # Criar o gráfico categórico
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', kind='bar', col='cardio').fig

    return fig

# Função para desenhar o Heat Map
def draw_heat_map():
    # Filtrar dados incorretos
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calcular a matriz de correlação
    corr = df_heat.corr()

    # Gerar uma máscara para o triângulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Configurar a figura do matplotlib
    fig, ax = plt.subplots(figsize=(10, 10))

    # Criar o heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", ax=ax, cmap='coolwarm', cbar_kws={'shrink': 0.5})

    return fig

# Salvar os gráficos
if __name__ == "__main__":
    # Desenhar e salvar o gráfico categórico
    fig_cat = draw_cat_plot()
    fig_cat.savefig('catplot.png')

    # Desenhar e salvar o Heat Map
    fig_heat = draw_heat_map()
    fig_heat.savefig('heatmap.png')

    print("Gráficos salvos com sucesso!")