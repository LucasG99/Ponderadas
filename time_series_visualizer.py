import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importar e limpar os dados
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Filtrar os dados removendo os top 2.5% e bottom 2.5%
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Função para desenhar o gráfico de linha
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='r', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    fig.savefig('line_plot.png')
    return fig

# Função para desenhar o gráfico de barras
def draw_bar_plot():
    # Preparar os dados para o gráfico de barras
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Desenhar o gráfico de barras
    fig = df_bar.plot(kind='bar', figsize=(10, 6)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.tight_layout()
    fig.savefig('bar_plot.png')
    return fig

# Função para desenhar os box plots
def draw_box_plot():
    # Preparar os dados para os box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')

    # Desenhar os box plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()
    fig.savefig('box_plot.png')
    return fig

# Salvar os gráficos
if __name__ == "__main__":
    # Desenhar e salvar o gráfico de linha
    draw_line_plot()

    # Desenhar e salvar o gráfico de barras
    draw_bar_plot()

    # Desenhar e salvar os box plots
    draw_box_plot()

    print("Gráficos salvos com sucesso!")