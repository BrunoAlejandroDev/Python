'''
ETAPA 2: ANALISE EXPLORATORIA GUIADA
'''

#* Importar o dataset
import pandas as pd
dataframe = pd.read_csv(r'C:\Users\Usuário\Downloads\satisfaction_learnsmart_150.csv')
# print(dataframe)

#* Inspecao Inicial 
# print(dataframe.head()) # formato
# print(dataframe.info()) # tipos de dados
# print(dataframe.describe())
# print(dataframe.isnull().sum()) # contagem de elementos nulos
# print(dataframe['feedback_text'].value_counts())

#* Pergunta 1: existe relacao enter horas gastas e nao conclusao do curso?
pergunta1 = dataframe.groupby('completion_status')['time_spent_hours'].describe()
print(f'Pergunta 1:\n{pergunta1}')

#* Pergunta 2: Alunos brasileiros concluem mais cursos? Sim
pergunta2 = pd.crosstab(dataframe['country'], dataframe['completion_status'], normalize='index') * 100
print(f'Pergunta 2:\n{pergunta2}')

#* Pergunta 3: alunos estrageiros tem notas mais baixas? Sim
pergunta3 = dataframe.groupby('country')['satisfaction_rating'].mean().sort_values()
print(f'Pergunta 3:\n{pergunta3}')

#* Pergunta 4: estrangeiros concluem menos cursos de programacao
taxa_programacao_df = dataframe[dataframe['category'] == 'Programação']
pergunta4 = pd.crosstab(taxa_programacao_df['country'], taxa_programacao_df['completion_status'], normalize='index') * 100
print(f'Pergunta 4:\n{pergunta4}')