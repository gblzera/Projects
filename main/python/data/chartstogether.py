import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/gabri/Downloads/archive/titanic-passengers.csv", sep=';')

print(df.info())
print(df.head())

survival_count = df['Survived'].value_counts()

fig, axes = plt.subplots(1,3, figsize=(14,7))

axes[0].bar(survival_count.index, survival_count.values, color=['red', 'green'])
axes[0].set_xlabel('Sobreviventes')
axes[0].set_ylabel('Quantidade de passageiros')
axes[0].set_title('Distribuição de sobreviventes do Titanic')
axes[0].set_xticks([0, 1])
axes[0].set_xticklabels(['Não Sobreviveu', 'Sobreviveu']) 

class_survival = df.groupby('Pclass')['Survived'].value_counts().unstack()
class_survival.plot(kind='bar', stacked=True, ax=axes[1], color=['red', 'green'])
axes[1].set_xlabel('Classe')
axes[1].set_ylabel('Quantidade de passageiros')
axes[1].set_title('Distribuição de sobreviventes por classe')
axes[1].set_xticks(range(len(class_survival.index)))
axes[1].set_xticklabels(['1ª Classe', '2ª Classe', '3ª Classe'])

sex_survival = df.groupby('Sex')['Survived'].value_counts().unstack()
sex_survival.plot(kind='bar', stacked=True, ax=axes[2], color=['red', 'green'])
axes[2].set_xlabel('Sexo')
axes[2].set_ylabel('Quantidade de passageiros')
axes[2].set_title('Distribuição de sobreviventes por sexo')
axes[2].set_xticks([0, 1])
axes[2].set_xticklabels(['Feminino', 'Masculino'])

plt.tight_layout()
plt.show()