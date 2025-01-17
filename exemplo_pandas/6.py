import pandas as pd
import matplotlib.pyplot as plt

#criando um grafico de barras
df_grafico = pd.DataFrame({
    'Nome': ['Bianca', 'Gabriel', 'Marcos'],
    'Pontuação': [92, 69, 100]
})
df_grafico.plot(kind='bar', x='Nome', y='Pontuação', title='Pontuação por pessoa')
plt.ylabel('Pontuação')
plt.show()
