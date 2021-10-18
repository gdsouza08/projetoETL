import pandas as pd

df = pd.read_csv("ocorrencia.csv", sep=";", parse_dates = ['ocorrencia_dia'], dayfirst=True)
df.head(5)

#pegando os dados de linha e coluna especificas
df.loc[1, 'ocorrencia_uf']

#pegando diversas linhas
df.loc[1:4]

#pegando toda a coluna
df.loc[:, 'ocorrencia_cidade']

df.set_index('codigo_ocorrencia', inplace=True)
df.head()

#vendo os dados de uma linha em especifico
df.loc[40324]

#voltando ao indece original
df.reset_index(drop=True, inplace=True)
df.head()

#alterando o valor de um dado
df.loc[0, 'ocorrencia_aerodromo'] = ''
df.head()

#alterando os dados de uma linha inteira
df.loc[1] = 38
df.head(2)

#alterando os dados de uma coluna inteira
df.loc[:, 'ocorrencia_classificacao'] = 'abcd'
df

#criando backup de coluna
df.loc['ocorrencia_uf_bkp'] = df.ocorrencia_uf
df

#filtrando dados e trocando valor de um campo
df.loc[df.ocorrencia_uf == 'SP', ['ocorrencia_classificacao']] ='GRAVE'
df

#filtrando linha por condicao
df.loc[df.ocorrencia_uf == 'SP']

#limpando e substituindo **** por <NA>
df.loc[df.ocorrencia_aerodromo == '****', ['ocorrencia_aerodromo']] = pd.NA
df.head()

#substituindo todos os nulos de uma vez
df.replace(['**', '###!', '####', '****', '*****', 'NULL'], pd.NA, inplace=True)
df

#somar por coluna quantos dados não informados por coluna tem
df.isna().sum()
df.isnull().sum()

df.fillna(4, inplace=True)
df.isna().sum()

#voltando valores para NA
df.replace([4], pd.NA, inplace=True)
df.isnull().sum()

#trocando valor NA de apenas uma coluna
df.fillna(value={'total_recomendacoes':4}, inplace=True)

df.drop(['Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'], axis=1, inplace=True)
df.drop(['ocorrencia_aerodromo == ****'], inplace=True)

#excluindo valores duplicados
df.drop_duplicates(inplace=True)