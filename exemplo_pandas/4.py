import pandas as pd

data_faltante = {
    'Nome': ['Bianca', 'Gabriel', None],
    'Idade': [None, 25, 30],
    'Cidade': ['São Paulo', 'Brasília', None]
}
df_faltante = pd.DataFrame(data_faltante)

#preenchendo os valores ausentes com um padrao
df_faltante['Cidade'].fillna('Desconhecida', inplace=True)
df_faltante['Idade'].fillna('Desconhecida', inplace=True)
df_faltante['Nome'].fillna('Desconhecido/a', inplace=True)

# removendo linhas com valores ausente
df_sem_nulos = df_faltante.dropna()

print("\nDataFrame com valores ausente (preenchido e sem nulos):")
print(df_faltante)
print("\nDataFrame sem valores ausente:")
print(df_sem_nulos)