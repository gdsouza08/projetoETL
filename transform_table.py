import pandas as pd
import pandera as pa

valores_ausentes = ['**', '###!', '####', '****', '*****', 'NULL']
df = pd.read_csv("ocorrencia.csv", sep=";", parse_dates = ['ocorrencia_dia'], dayfirst=True, na_values=valores_ausentes)
df.head(10)

schema = pa.DataFrameSchema(
    columns = {
        "codigo":pa.Column(pa.Int, required=False),
        "codigo_ocorrencia":pa.Column(pa.Int),
        "codigo_ocorrencia2":pa.Column(pa.Int),
        "ocorrencia_classificacao":pa.Column(pa.String),
        "ocorrencia_cidade":pa.Column(pa.String),
        "ocorrencia_uf":pa.Column(pa.String, pa.Check.str_length(2, 2), nullable=True),
        "ocorrencia_aerodromo":pa.Column(pa.String, nullable=True),
        "ocorrencia_dia":pa.Column(pa.DateTime),
        "ocorrencia_hora":pa.Column(pa.String, pa.Check.str_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'), nullable=True),
        "total_recomendacoes":pa.Column(pa.Int)
    }
)
schema.validate(df)

#pegando a ultima linha
df.iloc[-1]

df.iloc[10:15]

#busca de dados de uma coluna
df.loc[:, "ocorrencia_uf"]
df['ocorrencia_uf']

filtro = df.ocorrencia_uf.isnull()
df.loc[filtro]

#listar total dos valores sem contar os nulos
df.count()

#ocorrencias com mais de 10 recomendacoes

filtro = df.total_recomendacoes > 10
df.loc[filtro]

filtro = df.total_recomendacoes > 10
df.loc[filtro, ['ocorrencia_cidade']]

filtro = df.ocorrencia_classificacao == 'INCIDENTE GRAVE'	
df.loc[filtro, ['ocorrencia_classificacao', 'ocorrencia_cidade']]

filtro1 = df.ocorrencia_classificacao == 'INCIDENTE GRAVE'	
filtro2 = df.ocorrencia_uf == 'SP'
df.loc[filtro1 & filtro2, ['ocorrencia_classificacao', 'ocorrencia_cidade', 'ocorrencia_uf']]

filtro1 = df.ocorrencia_classificacao == 'INCIDENTE GRAVE'	
filtro2 = df.ocorrencia_uf == 'SP'
df.loc[filtro1 | filtro2, ['ocorrencia_classificacao', 'ocorrencia_cidade', 'ocorrencia_uf']]

filtro1 = (df.ocorrencia_classificacao == 'INCIDENTE GRAVE') | (df.ocorrencia_classificacao == 'INCIDENTE ')
filtro2 = df.ocorrencia_uf == 'SP'
df.loc[filtro1 & filtro2, ['ocorrencia_classificacao', 'ocorrencia_cidade', 'ocorrencia_uf']]

filtro1 = df.ocorrencia_classificacao.isin (['INCIDENTE GRAVE', 'INCIDENTE']) 
filtro2 = df.ocorrencia_uf == 'SP'
df.loc[filtro1 & filtro2, ['ocorrencia_classificacao', 'ocorrencia_cidade', 'ocorrencia_uf']]

filtro = df.ocorrencia_cidade.str[0] == 'C'
df.loc[filtro, [ 'ocorrencia_cidade','ocorrencia_uf']]

filtro = df.ocorrencia_cidade.str[-1] == 'A'
df.loc[filtro, [ 'ocorrencia_cidade','ocorrencia_uf']]

filtro = df.ocorrencia_cidade.str[-2:] == 'MA'
df.loc[filtro, [ 'ocorrencia_cidade','ocorrencia_uf']]

filtro = df.ocorrencia_cidade.str.contains('MA')
df.loc[filtro, [ 'ocorrencia_cidade','ocorrencia_uf']]

filtro = df.ocorrencia_dia.dt.year == 2018
df.loc[filtro]

#juntar duas colunas de tipos diferentes
df['ocorrencia_dia_hora'] = pd.to_datetime(df.ocorrencia_dia.astype(str) + ' ' + df.ocorrencia_hora)
