import pandas as pd

# Criando o DataFrame a partir de um dicionário
data = {
    'Nome': ['Bianca', 'Gabriel', 'Marcos'],
    'Idade': [27, 22, 37],
    'Cidade': ['São Paulo', 'Brasília', 'Brasília']
}
df = pd.DataFrame(data)

# Salvando o DataFrame em um arquivo CSV
df.to_csv('dados.csv', index=False)

# Lendo o arquivo CSV
df_read = pd.read_csv('dados.csv')

# Exibindo as primeiras linhas do DataFrame
print(df_read.head())

# Salvando o DataFrame em um arquivo Excel (certifique-se de ter o openpyxl instalado)
df_read.to_excel('dados.xlsx', index=False)

print("Arquivos CSV e Excel criados com sucesso!")
#fim