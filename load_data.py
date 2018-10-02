# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import os
#print(os.getcwd())

# http://www.tse.jus.br/eleicoes/estatisticas/repositorio-de-dados-eleitorais-1/repositorio-de-dados-eleitorais
data = pd.read_csv("c:\dev\python\consulta_coligacao_2018_BRASIL.csv", sep=";", encoding='latin-1') 

# Preview the first 5 lines of the loaded data 
print(data.head(5))