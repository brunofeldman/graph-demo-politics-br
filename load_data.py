# Import libraries 
import pandas as pd 
from gremlin_python.driver import client, serializer
import sys, traceback

# CosmosDB parameters
ENDPOINT = 'SERVERNAME.gremlin.cosmosdb.azure.com'
DATABASE = 'DATABASENAME'
COLLECTION = 'GRAPHNAME'
PRIMARY_KEY = 'PRIMARY_KEY (get from Keys Menu on CosmosDB Azure Portal'

# File to load (Brazilian Elections 2018 Coalition)
# http://www.tse.jus.br/eleicoes/estatisticas/repositorio-de-dados-eleitorais-1/repositorio-de-dados-eleitorais
# Load CSV file into dataframe
data = pd.read_csv("consulta_coligacao_2018_BRASIL.csv", sep=";", encoding='latin-1') 

# Removing some unused columns, creating a new "data1" dataframe
colsToDrop = ['DT_GERACAO','HH_GERACAO','CD_ELEICAO','DT_ELEICAO', 'SQ_COLIGACAO', 'NR_PARTIDO' , 'DS_ELEICAO', 'SG_UE', 'CD_TIPO_ELEICAO', 'NM_TIPO_ELEICAO','NR_TURNO', 'NM_UE', 'CD_CARGO', 'NM_PARTIDO']
data1 = data.drop(colsToDrop, axis=1)

# Spliting "Coalition" column into 18 new columns
data2 = data1['DS_COMPOSICAO_COLIGACAO'].str.split(' / ',20,expand=True)
data1 = data1.join(data2)
data1 = data1.drop('DS_COMPOSICAO_COLIGACAO', axis=1)

# Now we need to create 2 lists, VERTICES and EDGES with this format:
# VERTICES: "g.addV('PARTIDO').property('id', '99').property('sigla', 'PPA').property('nome', 'PARTIDO EXEMPLO A')"
# EDGES: "g.V().has('sigla','PPA').addE('coligado').to(g.V().has('sigla','PPB'))"

# Init empty lists:
VERTICES = [] 
EDGES = [] 

# Building "VERTICES" list
# Creating "dataV" dataframe with columns that we need to vertices and excluding duplicate rows:
dataV = data[['SG_PARTIDO','NR_PARTIDO','NM_PARTIDO']].drop_duplicates()

# Iterating into "dataV" and append addV command into "VERTICE" list:
for row in dataV.itertuples(index=True, name='Pandas'):
    VERTICES.append('g.addV(\'PARTIDO\').property(\'id\',\''  + str(getattr(row, "NR_PARTIDO")) + '\').property(\'sigla\',\'' + getattr(row, "SG_PARTIDO") + '\').property(\'nome\',\'' + getattr(row, "NM_PARTIDO") + '\')')

# Building "EDGES" list
# Now we need to get all coalitions from 18 splitted columns into 18 new dataframes with same column names and concat in "dataE" dataframe (more beautiful code coming soon...)

dataE0 = data1[['SG_PARTIDO',0]].drop_duplicates() 
dataE1 = data1[['SG_PARTIDO',1]].drop_duplicates() 
dataE2 = data1[['SG_PARTIDO',2]].drop_duplicates() 
dataE3 = data1[['SG_PARTIDO',3]].drop_duplicates() 
dataE4 = data1[['SG_PARTIDO',4]].drop_duplicates() 
dataE5 = data1[['SG_PARTIDO',5]].drop_duplicates() 
dataE6 = data1[['SG_PARTIDO',6]].drop_duplicates() 
dataE7 = data1[['SG_PARTIDO',7]].drop_duplicates() 
dataE8 = data1[['SG_PARTIDO',8]].drop_duplicates() 
dataE9 = data1[['SG_PARTIDO',9]].drop_duplicates() 
dataE10 = data1[['SG_PARTIDO',10]].drop_duplicates() 
dataE11 = data1[['SG_PARTIDO',11]].drop_duplicates() 
dataE12 = data1[['SG_PARTIDO',12]].drop_duplicates() 
dataE13 = data1[['SG_PARTIDO',13]].drop_duplicates() 
dataE14 = data1[['SG_PARTIDO',14]].drop_duplicates() 
dataE15 = data1[['SG_PARTIDO',15]].drop_duplicates() 
dataE16 = data1[['SG_PARTIDO',16]].drop_duplicates() 
dataE17 = data1[['SG_PARTIDO',17]].drop_duplicates() 

dataE0.columns = ['partido','coligado']
dataE1.columns = ['partido','coligado']
dataE2.columns = ['partido','coligado']
dataE3.columns = ['partido','coligado']
dataE4.columns = ['partido','coligado']
dataE5.columns = ['partido','coligado']
dataE6.columns = ['partido','coligado']
dataE7.columns = ['partido','coligado']
dataE8.columns = ['partido','coligado']
dataE9.columns = ['partido','coligado']
dataE10.columns = ['partido','coligado']
dataE11.columns = ['partido','coligado']
dataE12.columns = ['partido','coligado']
dataE13.columns = ['partido','coligado']
dataE14.columns = ['partido','coligado']
dataE15.columns = ['partido','coligado']
dataE16.columns = ['partido','coligado']
dataE17.columns = ['partido','coligado']

dataE = pd.concat([dataE0, dataE1, dataE2, dataE3, dataE4, dataE5, dataE6, dataE7, dataE8, dataE9, dataE10, dataE11, dataE12, dataE13, dataE14, dataE15, dataE16, dataE17])

# Removing null values (expected in cases with less than 18 coalitions) and dropping duplicates
dataE = dataE[dataE['coligado'].notnull()]
dataE = dataE.drop_duplicates()

# Iterating into "dataE" and append addE command into "EDGES" list:
for row in dataE.itertuples(index=True, name='Pandas'):
    EDGES.append('g.V().has(\'sigla\',\'' + getattr(row, "partido") +   '\').addE(\'coligado\').to(g.V().has(\'sigla\',\'' + getattr(row, "coligado") + '\'))')

# Initializing CosmosDB connection, cleaning graph and inserting vertices and edges:

def cleanup_graph(gremlin_client):
    callback = gremlin_client.submitAsync("g.V().drop()")
    if callback.result() is not None:
        print("Cleaned up the graph!")

def insert_vertices(gremlin_client):
    for vertex in VERTICES:
        callback = gremlin_client.submitAsync(vertex)
        if callback.result() is not None:
            print("Inserted this vertex:\n{0}".format(callback.result().one()))
        else:
            print("Something went wrong with this query: {0}".format(vertex))

def insert_edges(gremlin_client):
    for edge in EDGES:
        callback = gremlin_client.submitAsync(edge)
        if callback.result() is not None:
            print("Inserted this edge:\n{0}".format(callback.result().one()))
        else:
            print("Something went wrong with this query:\n{0}".format(edge))

def handler():
    # Initialise client
    print('Initialising client...')
    gremlin_client = client.Client(
        'wss://' + ENDPOINT + ':443/', 'g',
        username="/dbs/"+ DATABASE + "/colls/" + COLLECTION,
        password=PRIMARY_KEY
        
    )
    print('Client initialised!')

    # Purge graph
    cleanup_graph(gremlin_client)

    # Insert vertices (i.e. nodes)
    insert_vertices(gremlin_client)

    # Insert edges (i.e. nodes)
    insert_edges(gremlin_client)

    print('Finished!')

if __name__ == '__main__':
    handler()
