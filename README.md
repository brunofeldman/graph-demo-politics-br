
# Azure CosmosDB Graph Databases: Eleições 2018

* Script que gera um Graph Database no Azure CosmosDB a partir de uma relação de coligações de partidos políticos disponível em arquivo no site do TSE.
* Foram feitas em Python as manipulações no arquivo para obter somente os dados relevantes e também para gerar os scripts de inserção de vértices e edges.

# Como usar:

* Criar um recurso CosmosDB no Azure, selecionando a API Gremlin.
* Dentro do CosmosDB (via Portal: Data Explorer), criar um Database e um Graph.
* Alterar no script os parâmetros referente ao Database e Graph criados, junto com a Primary Key do recurso.
* Executar o script com o arquivo CSV no mesmo diretório.

# TODO list:

* Adicionar mais informações como estado, nome da coligação e cargo na EDGE.
* Adicionar exemplos de consultas no grafo.


