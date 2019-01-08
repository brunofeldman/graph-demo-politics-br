# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
#import os
#print(os.getcwd())

# http://www.tse.jus.br/eleicoes/estatisticas/repositorio-de-dados-eleitorais-1/repositorio-de-dados-eleitorais
data = pd.read_csv("consulta_coligacao_2018_BRASIL.csv", sep=";", encoding='latin-1') 


colsToDrop = ['DT_GERACAO','HH_GERACAO','CD_ELEICAO','DT_ELEICAO', 'SQ_COLIGACAO', 'NR_PARTIDO' , 'DS_ELEICAO', 'SG_UE', 'CD_TIPO_ELEICAO', 'NM_TIPO_ELEICAO']

data1 = data.drop(colsToDrop, axis=1)

# Preview the first 5 lines of the loaded data 
print(data1.head(15))

print(data1.columns.tolist())

#print(data.loc[:,'SG_PARTIDO'])