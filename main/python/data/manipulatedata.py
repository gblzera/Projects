import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset Titanic com o separador correto
df = pd.read_csv("C:/Users/gabri/Downloads/archive/titanic-passengers.csv", sep=';')

# Verificar as informações gerais do dataset
print(df.info())  # visualizar as informações gerais do dataset
print(df.columns)  # visualizar todas as colunas
print(df.head())  # exibir as primeiras 5 linhas

estatisticas = df.describe()
print(estatisticas)

# Contar a quantidade de sobreviventes e não sobreviventes
survival_count = df['Survived'].value_counts()

# Criar o gráfico de barras para a distribuição de sobreviventes
plt.figure(figsize=(10,6))
plt.bar(survival_count.index, survival_count.values, color=['red', 'green'])
plt.xlabel('Sobreviventes')
plt.ylabel('Quantidade de passageiros')
plt.title('Distribuição de sobreviventes do Titanic')
plt.xticks([0, 1], ['Não Sobreviveu', 'Sobreviveu'])
plt.tight_layout()  # ajusta o layout automaticamente
plt.show()

class_survival = df.groupby('Pclass')['Survived'].value_counts().unstack()# Contagem de sobreviventes por classe

class_survival.plot(kind='bar', stacked=True, figsize=(10,6), color=['red', 'green'])# Criar gráfico de barras para a contagem de sobreviventes por classe
plt.xlabel('Classe')
plt.ylabel('Quantidade de passageiros')
plt.title('Distribuição de sobreviventes por classe')
plt.xticks(range(len(class_survival.index)), ['1ª Classe', '2ª Classe', '3ª Classe'], rotation=0)
plt.tight_layout()
plt.show()

sex_survival = df.groupby('Sex')['Survived'].value_counts().unstack()# Contagem de sobreviventes por sexo

sex_survival.plot(kind='bar', stacked=True, figsize=(10,6), color=['red', 'green'])# Criar gráfico de barras para a contagem de sobreviventes por sexo
plt.xlabel('Sexo')
plt.ylabel('Quantidade de passageiros')
plt.title('Distribuição de sobreviventes por sexo')
plt.xticks([0, 1], ['Feminino', 'Masculino'], rotation=0)
plt.tight_layout()
plt.show()

media_idade = df['Age'].mean()
print(f'Média de Idade: {media_idade}')

contagem_classes = df['Pclass'].value_counts()
print(f'Contagem de Classes: \n{contagem_classes}')