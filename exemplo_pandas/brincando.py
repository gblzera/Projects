import pandas as pd
import matplotlib.pyplot as plt

# Criando os dados
data = {
    'Nome': ['Bianca', 'Gabriel', 'Marcos', 'Laura', 'Rafael', 'Mano Lima'],
    'Idade': [27, 22, 37, 22, 19, 66],
    'Cidade': ['São Paulo', 'Brasília', 'Brasília', 'Cachoeira', 'Rio de Janeiro', 'Porto Alegre']
}
df = pd.DataFrame(data)

# Gráfico 1: Histograma de Idade
plt.figure(figsize=(8,6))
plt.hist(df['Idade'], bins=5, color='skyblue', edgecolor='black')
plt.title('Distribuição das Idades')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.grid(True)

# Gráfico 2: Contagem de pessoas por cidade
plt.figure(figsize=(8,6))
cidade_contagem = df['Cidade'].value_counts()
cidade_contagem.plot(kind='bar', color='lightcoral', title='Número de Pessoas por Cidade')
plt.ylabel('Contagem')
plt.xlabel('Cidade')
plt.xticks(rotation=45)

# Gráfico 3: Gráfico de Dispersão (Idade x Nome)
plt.figure(figsize=(8,6))
plt.scatter(df['Nome'], df['Idade'], color='green')
plt.title('Idade por Nome')
plt.xlabel('Nome')
plt.ylabel('Idade')
plt.grid(True)

# Exibindo todos os gráficos de uma vez
plt.show()
