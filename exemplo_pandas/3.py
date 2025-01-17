import pandas as pd

data = {
    'Nome': ['Bianca', 'Gabriel', 'Marcos'],
    'Idade': [27, 22, 37],
    'Cidade': ['São Paulo', 'Brasília', 'Brasília']
}
df = pd.DataFrame(data)

#Filtrando linhas onde a idade é amior que 30
filtro = df[df['Idade'] > 30]
print("Dados filtrados (Idade > 30): ")
print(filtro)

# Ordenando os dados pela idade
df_ordenado = df.sort_values(by='Idade', ascending=True)
print("\nDados ordenados pela idade:")
print(df_ordenado)

# salvando o dataFrame em CSV
df.to_csv('dados2.csv', index=False)

# lendo um arquivo CSV
df_read = pd.read_csv('dados2.csv')

#exibindo as priemiras linhas do dataFrame
print("\nLeitura do arquivo CSV:")
print(df_read.head())

# salvando um dataFrame em Excel
df_read.to_excel('dados2.xlsx', index=False)

print("\nArquivos CSV e Excel criados com sucesso!")
#fim