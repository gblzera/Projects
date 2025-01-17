import pandas as pd

#Criando o DF a partir de um dicionario

data = {
    'Nome': ['Bianca','Gabriel', 'Marcos' ],
    'Idade': [27, 22, 37],
    'Cidade': ['São Paulo', 'Brasília', 'Brasília']
}
df = pd.DataFrame(data)

#exibindo o DF
print(df)

#selecionando uma coluna especific
#print(df['Nome'])

#selecionando uma linha pelo indice
#print(df.loc[1]) # linha com indice 1(Gabriel)

#adicionando uma nova coluna
#df['Profissão'] = ['Engeheira', 'Uber', 'Julius']
#print(df)
#fim
