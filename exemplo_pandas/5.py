import pandas as pd

data_estatistica = {
    'Categoria': ['A', 'B', 'A', 'B', 'A'],
    'Valor': [10, 20, 30, 40, 50]
}
df_estatistica = pd.DataFrame(data_estatistica)

#calculando a soma por categoria
agrupado = df_estatistica.groupby('Categoria').sum()
print("\nSoma por categoria")
print(agrupado)

#estatisticas basicas
print("\nEstatisticas basicas")
print(f"Média: {df_estatistica['Valor'].mean()}")
print(f"Desvio padrão: {df_estatistica['Valor'].std()}")
print(f"Máximo: {df_estatistica['Valor'].max()}")
#fim