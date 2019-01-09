* Creating...




```python
# Import libraries 
import pandas as pd
```


```python
# File to load (Brazilian Elections 2018 Coalition)
# http://www.tse.jus.br/eleicoes/estatisticas/repositorio-de-dados-eleitorais-1/repositorio-de-dados-eleitorais
# Load CSV file into dataframe
data = pd.read_csv("consulta_coligacao_2018_BRASIL.csv", sep=";", encoding='latin-1') 
```


```python
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DT_GERACAO</th>
      <th>HH_GERACAO</th>
      <th>ANO_ELEICAO</th>
      <th>CD_TIPO_ELEICAO</th>
      <th>NM_TIPO_ELEICAO</th>
      <th>NR_TURNO</th>
      <th>CD_ELEICAO</th>
      <th>DS_ELEICAO</th>
      <th>DT_ELEICAO</th>
      <th>SG_UF</th>
      <th>...</th>
      <th>NM_UE</th>
      <th>CD_CARGO</th>
      <th>DS_CARGO</th>
      <th>TP_AGREMIACAO</th>
      <th>NR_PARTIDO</th>
      <th>SG_PARTIDO</th>
      <th>NM_PARTIDO</th>
      <th>SQ_COLIGACAO</th>
      <th>NM_COLIGACAO</th>
      <th>DS_COMPOSICAO_COLIGACAO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>BA</td>
      <td>...</td>
      <td>BAHIA</td>
      <td>10</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>90</td>
      <td>PROS</td>
      <td>PARTIDO REPUBLICANO DA ORDEM SOCIAL</td>
      <td>50000050202</td>
      <td>MAIS TRABALHO POR TODA A BAHIA</td>
      <td>PT / PP / PDT / PSD / PSB / PC do B / PR / PMB...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RR</td>
      <td>...</td>
      <td>RORAIMA</td>
      <td>9</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>55</td>
      <td>PSD</td>
      <td>PARTIDO SOCIAL DEMOCRÁTICO</td>
      <td>230000050050</td>
      <td>TODOS POR RORAIMA</td>
      <td>PSDB / DEM / MDB / PSD / PPS / SOLIDARIEDADE / DC</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RS</td>
      <td>...</td>
      <td>RIO GRANDE DO SUL</td>
      <td>10</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>20</td>
      <td>PSC</td>
      <td>PARTIDO SOCIAL CRISTÃO</td>
      <td>210000050185</td>
      <td>RIO GRANDE NO RUMO CERTO</td>
      <td>MDB / PSD / PSB / PR / PSC / PATRI / PRP / PMN...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>MA</td>
      <td>...</td>
      <td>MARANHÃO</td>
      <td>9</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>23</td>
      <td>PPS</td>
      <td>PARTIDO POPULAR SOCIALISTA</td>
      <td>100000050110</td>
      <td>TODOS PELO MARANHÃO</td>
      <td>PC do B / PRB / PDT / PPS / DEM / PSB / PR / P...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>TO</td>
      <td>...</td>
      <td>TOCANTINS</td>
      <td>3</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>43</td>
      <td>PV</td>
      <td>PARTIDO VERDE</td>
      <td>270000050710</td>
      <td>Coligação Frente Alternativa</td>
      <td>REDE / PRTB / PTB / PC do B / PT / PV / PDT / PSD</td>
    </tr>
    <tr>
      <th>5</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>PI</td>
      <td>...</td>
      <td>PIAUÍ</td>
      <td>9</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>10</td>
      <td>PRB</td>
      <td>PARTIDO REPUBLICANO BRASILEIRO</td>
      <td>180000050225</td>
      <td>MUDAR PARA CUIDAR DA NOSSA GENTE</td>
      <td>PMN / PRB / SOLIDARIEDADE / PPL / PTC</td>
    </tr>
    <tr>
      <th>6</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>ES</td>
      <td>...</td>
      <td>ESPÍRITO SANTO</td>
      <td>4</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>10</td>
      <td>PRB</td>
      <td>PARTIDO REPUBLICANO BRASILEIRO</td>
      <td>80000050196</td>
      <td>COLIGAÇÃO EM DEFESA DA VIDA E DA FAMILIA</td>
      <td>PR / PRB / PSL</td>
    </tr>
    <tr>
      <th>7</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RJ</td>
      <td>...</td>
      <td>RIO DE JANEIRO</td>
      <td>9</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>21</td>
      <td>PCB</td>
      <td>PARTIDO COMUNISTA BRASILEIRO</td>
      <td>190000050058</td>
      <td>MUDAR É POSSÍVEL</td>
      <td>PSOL / PCB</td>
    </tr>
    <tr>
      <th>8</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>AL</td>
      <td>...</td>
      <td>ALAGOAS</td>
      <td>9</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>22</td>
      <td>PR</td>
      <td>PARTIDO DA REPÚBLICA</td>
      <td>20000050568</td>
      <td>Avança Mais Alagoas</td>
      <td>MDB / PODE / PPS / PDT / PR / PTB / PHS / PV /...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>PA</td>
      <td>...</td>
      <td>PARÁ</td>
      <td>10</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>65</td>
      <td>PC do B</td>
      <td>PARTIDO COMUNISTA DO BRASIL</td>
      <td>140000050740</td>
      <td>PRA VIVER EM PAZ</td>
      <td>PT / PC do B</td>
    </tr>
    <tr>
      <th>10</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>PE</td>
      <td>...</td>
      <td>PERNAMBUCO</td>
      <td>7</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>15</td>
      <td>MDB</td>
      <td>MOVIMENTO DEMOCRÁTICO BRASILEIRO</td>
      <td>170000050274</td>
      <td>FRENTE POPULAR DE PERNAMBUCO PARA DEPUTADO EST...</td>
      <td>PSB / MDB / PSD</td>
    </tr>
    <tr>
      <th>11</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>AP</td>
      <td>...</td>
      <td>AMAPÁ</td>
      <td>10</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>45</td>
      <td>PSDB</td>
      <td>PARTIDO DA SOCIAL DEMOCRACIA BRASILEIRA</td>
      <td>30000050520</td>
      <td>TRABALHO E UNIÃO PELO AMAPÁ</td>
      <td>DEM / REDE / PSDB / PPL / PP / PSC / AVANTE / ...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>MA</td>
      <td>...</td>
      <td>MARANHÃO</td>
      <td>3</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>22</td>
      <td>PR</td>
      <td>PARTIDO DA REPÚBLICA</td>
      <td>100000050110</td>
      <td>TODOS PELO MARANHÃO</td>
      <td>PC do B / PRB / PDT / PPS / DEM / PSB / PR / P...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>BA</td>
      <td>...</td>
      <td>BAHIA</td>
      <td>10</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>33</td>
      <td>PMN</td>
      <td>PARTIDO DA MOBILIZAÇÃO NACIONAL</td>
      <td>50000050202</td>
      <td>MAIS TRABALHO POR TODA A BAHIA</td>
      <td>PT / PP / PDT / PSD / PSB / PC do B / PR / PMB...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RO</td>
      <td>...</td>
      <td>RONDÔNIA</td>
      <td>5</td>
      <td>SENADOR</td>
      <td>PARTIDO ISOLADO</td>
      <td>35</td>
      <td>PMB</td>
      <td>PARTIDO DA MULHER BRASILEIRA</td>
      <td>220000050546</td>
      <td>#NULO#</td>
      <td>PMB</td>
    </tr>
    <tr>
      <th>15</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>MA</td>
      <td>...</td>
      <td>MARANHÃO</td>
      <td>9</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>11</td>
      <td>PP</td>
      <td>PARTIDO PROGRESSISTA</td>
      <td>100000050110</td>
      <td>TODOS PELO MARANHÃO</td>
      <td>PC do B / PRB / PDT / PPS / DEM / PSB / PR / P...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RR</td>
      <td>...</td>
      <td>RORAIMA</td>
      <td>4</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>14</td>
      <td>PTB</td>
      <td>PARTIDO TRABALHISTA BRASILEIRO</td>
      <td>230000050426</td>
      <td>DÊ UMA CHANCE PARA RORAIMA</td>
      <td>PTB / PV / REDE / PT</td>
    </tr>
    <tr>
      <th>17</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>TO</td>
      <td>...</td>
      <td>TOCANTINS</td>
      <td>5</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>11</td>
      <td>PP</td>
      <td>PARTIDO PROGRESSISTA</td>
      <td>270000050486</td>
      <td>GOVERNO DE ATITUDE</td>
      <td>PHS / SOLIDARIEDADE / PP / DEM / PTC / PRB / A...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>MA</td>
      <td>...</td>
      <td>MARANHÃO</td>
      <td>7</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>31</td>
      <td>PHS</td>
      <td>PARTIDO HUMANISTA DA SOLIDARIEDADE</td>
      <td>100000050339</td>
      <td>CORAGEM E UNIÃO PARA FAZER O MARANHÃO MELHOR</td>
      <td>PODE / REDE / DC / PHS / PMN / PSDB</td>
    </tr>
    <tr>
      <th>19</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RJ</td>
      <td>...</td>
      <td>RIO DE JANEIRO</td>
      <td>10</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>18</td>
      <td>REDE</td>
      <td>REDE SUSTENTABILIDADE</td>
      <td>190000050290</td>
      <td>A FORÇA QUE VEM DO POVO</td>
      <td>PODE / PR / REDE / PPL</td>
    </tr>
    <tr>
      <th>20</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>SE</td>
      <td>...</td>
      <td>SERGIPE</td>
      <td>6</td>
      <td>DEPUTADO FEDERAL</td>
      <td>COLIGACAO</td>
      <td>33</td>
      <td>PMN</td>
      <td>PARTIDO DA MOBILIZAÇÃO NACIONAL</td>
      <td>260000050432</td>
      <td>PARA RENOVAR SERGIPE</td>
      <td>PODE / AVANTE / PMN / PATRI</td>
    </tr>
    <tr>
      <th>21</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RS</td>
      <td>...</td>
      <td>RIO GRANDE DO SUL</td>
      <td>4</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>13</td>
      <td>PT</td>
      <td>PARTIDO DOS TRABALHADORES</td>
      <td>210000050179</td>
      <td>POR UM RIO GRANDE JUSTO</td>
      <td>PT / PC do B</td>
    </tr>
    <tr>
      <th>22</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RJ</td>
      <td>...</td>
      <td>RIO DE JANEIRO</td>
      <td>4</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>36</td>
      <td>PTC</td>
      <td>PARTIDO TRABALHISTA CRISTÃO</td>
      <td>190000050571</td>
      <td>Para o Povo Voltar a Ser Feliz</td>
      <td>PRP / PRB / PTC / PATRI</td>
    </tr>
    <tr>
      <th>23</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RO</td>
      <td>...</td>
      <td>RONDÔNIA</td>
      <td>7</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>43</td>
      <td>PV</td>
      <td>PARTIDO VERDE</td>
      <td>220000050483</td>
      <td>RONDONIA, UNIDOS SOMOS FORTES 2</td>
      <td>MDB / PV</td>
    </tr>
    <tr>
      <th>24</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>CE</td>
      <td>...</td>
      <td>CEARÁ</td>
      <td>7</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>PARTIDO ISOLADO</td>
      <td>16</td>
      <td>PSTU</td>
      <td>PARTIDO SOCIALISTA DOS TRABALHADORES UNIFICADO</td>
      <td>60000050561</td>
      <td>#NULO#</td>
      <td>PSTU</td>
    </tr>
    <tr>
      <th>25</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>DF</td>
      <td>...</td>
      <td>DISTRITO FEDERAL</td>
      <td>4</td>
      <td>VICE-GOVERNADOR</td>
      <td>PARTIDO ISOLADO</td>
      <td>30</td>
      <td>NOVO</td>
      <td>PARTIDO NOVO</td>
      <td>70000050065</td>
      <td>#NULO#</td>
      <td>NOVO</td>
    </tr>
    <tr>
      <th>26</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>DF</td>
      <td>...</td>
      <td>DISTRITO FEDERAL</td>
      <td>6</td>
      <td>DEPUTADO FEDERAL</td>
      <td>PARTIDO ISOLADO</td>
      <td>22</td>
      <td>PR</td>
      <td>PARTIDO DA REPÚBLICA</td>
      <td>70000050315</td>
      <td>#NULO#</td>
      <td>PR</td>
    </tr>
    <tr>
      <th>27</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>MG</td>
      <td>...</td>
      <td>MINAS GERAIS</td>
      <td>7</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>35</td>
      <td>PMB</td>
      <td>PARTIDO DA MULHER BRASILEIRA</td>
      <td>130000050269</td>
      <td>RENOVAÇÃO</td>
      <td>PATRI / PTC / PMB</td>
    </tr>
    <tr>
      <th>28</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RS</td>
      <td>...</td>
      <td>RIO GRANDE DO SUL</td>
      <td>5</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>36</td>
      <td>PTC</td>
      <td>PARTIDO TRABALHISTA CRISTÃO</td>
      <td>210000050185</td>
      <td>RIO GRANDE NO RUMO CERTO</td>
      <td>MDB / PSD / PSB / PR / PSC / PATRI / PRP / PMN...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RS</td>
      <td>...</td>
      <td>RIO GRANDE DO SUL</td>
      <td>9</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>22</td>
      <td>PR</td>
      <td>PARTIDO DA REPÚBLICA</td>
      <td>210000050185</td>
      <td>RIO GRANDE NO RUMO CERTO</td>
      <td>MDB / PSD / PSB / PR / PSC / PATRI / PRP / PMN...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6179</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>PR</td>
      <td>...</td>
      <td>PARANÁ</td>
      <td>5</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>45</td>
      <td>PSDB</td>
      <td>PARTIDO DA SOCIAL DEMOCRACIA BRASILEIRA</td>
      <td>160000050609</td>
      <td>PARANA DECIDE</td>
      <td>PP / PTB / DEM / PMN / PMB / PSB / PSDB / PROS</td>
    </tr>
    <tr>
      <th>6180</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RN</td>
      <td>...</td>
      <td>RIO GRANDE DO NORTE</td>
      <td>5</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>23</td>
      <td>PPS</td>
      <td>PARTIDO POPULAR SOCIALISTA</td>
      <td>200000050306</td>
      <td>TRABALHO E SUPERAÇÃO</td>
      <td>PRB / PTB / PR / PPS / PMB / PTC / PSB / PRP /...</td>
    </tr>
    <tr>
      <th>6181</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>AM</td>
      <td>...</td>
      <td>AMAZONAS</td>
      <td>4</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>77</td>
      <td>SOLIDARIEDADE</td>
      <td>SOLIDARIEDADE</td>
      <td>40000050267</td>
      <td>EU VOTO NO AMAZONAS</td>
      <td>PDT / PRP / AVANTE / PP / PV / PR / SOLIDARIED...</td>
    </tr>
    <tr>
      <th>6182</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>CE</td>
      <td>...</td>
      <td>CEARÁ</td>
      <td>5</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>50</td>
      <td>PSOL</td>
      <td>PARTIDO SOCIALISMO E LIBERDADE</td>
      <td>60000050534</td>
      <td>FRENTE DE ESQUERDA SOCIALISTA</td>
      <td>PSOL</td>
    </tr>
    <tr>
      <th>6183</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>AC</td>
      <td>...</td>
      <td>ACRE</td>
      <td>9</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>20</td>
      <td>PSC</td>
      <td>PARTIDO SOCIAL CRISTÃO</td>
      <td>10000050011</td>
      <td>Muda Acre de Verdade</td>
      <td>PSL / PATRI / PSC</td>
    </tr>
    <tr>
      <th>6184</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>AL</td>
      <td>...</td>
      <td>ALAGOAS</td>
      <td>4</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>14</td>
      <td>PTB</td>
      <td>PARTIDO TRABALHISTA BRASILEIRO</td>
      <td>20000050568</td>
      <td>Avança Mais Alagoas</td>
      <td>MDB / PODE / PPS / PDT / PR / PTB / PHS / PV /...</td>
    </tr>
    <tr>
      <th>6185</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>SP</td>
      <td>...</td>
      <td>SÃO PAULO</td>
      <td>9</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>14</td>
      <td>PTB</td>
      <td>PARTIDO TRABALHISTA BRASILEIRO</td>
      <td>250000050400</td>
      <td>São Paulo Confia e Avança</td>
      <td>PSB / PSC / PPS / PTB / PV / PR / PODE / PMB /...</td>
    </tr>
    <tr>
      <th>6186</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>SP</td>
      <td>...</td>
      <td>SÃO PAULO</td>
      <td>4</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>65</td>
      <td>PC do B</td>
      <td>PARTIDO COMUNISTA DO BRASIL</td>
      <td>250000050635</td>
      <td>SÃO PAULO DO TRABALHO  E DE OPORTUNIDADES</td>
      <td>PT / PC do B</td>
    </tr>
    <tr>
      <th>6187</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>SC</td>
      <td>...</td>
      <td>SANTA CATARINA</td>
      <td>9</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>65</td>
      <td>PC do B</td>
      <td>PARTIDO COMUNISTA DO BRASIL</td>
      <td>240000050553</td>
      <td>AQUI É TRABALHO</td>
      <td>PSD / PRB / PDT / PSB / PODE / SOLIDARIEDADE /...</td>
    </tr>
    <tr>
      <th>6188</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>MG</td>
      <td>...</td>
      <td>MINAS GERAIS</td>
      <td>9</td>
      <td>1º SUPLENTE</td>
      <td>PARTIDO ISOLADO</td>
      <td>30</td>
      <td>NOVO</td>
      <td>PARTIDO NOVO</td>
      <td>130000050025</td>
      <td>#NULO#</td>
      <td>NOVO</td>
    </tr>
    <tr>
      <th>6189</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>MG</td>
      <td>...</td>
      <td>MINAS GERAIS</td>
      <td>4</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>19</td>
      <td>PODE</td>
      <td>PODEMOS</td>
      <td>130000050682</td>
      <td>#MinasTemJeito</td>
      <td>PDT / PODE / MDB / PROS / PRB / PV</td>
    </tr>
    <tr>
      <th>6190</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>PI</td>
      <td>...</td>
      <td>PIAUÍ</td>
      <td>3</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>19</td>
      <td>PODE</td>
      <td>PODEMOS</td>
      <td>180000050413</td>
      <td>RESISTÊNCIA PELO PIAUÍ</td>
      <td>PODE / AVANTE / PATRI / REDE / PPS / PV / PRP ...</td>
    </tr>
    <tr>
      <th>6191</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>AP</td>
      <td>...</td>
      <td>AMAPÁ</td>
      <td>3</td>
      <td>GOVERNADOR</td>
      <td>PARTIDO ISOLADO</td>
      <td>16</td>
      <td>PSTU</td>
      <td>PARTIDO SOCIALISTA DOS TRABALHADORES UNIFICADO</td>
      <td>30000050277</td>
      <td>#NULO#</td>
      <td>PSTU</td>
    </tr>
    <tr>
      <th>6192</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>AP</td>
      <td>...</td>
      <td>AMAPÁ</td>
      <td>9</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>40</td>
      <td>PSB</td>
      <td>PARTIDO SOCIALISTA BRASILEIRO</td>
      <td>30000050517</td>
      <td>COM O POVO PRA AVANÇAR</td>
      <td>PT / PSB</td>
    </tr>
    <tr>
      <th>6193</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>DF</td>
      <td>...</td>
      <td>DISTRITO FEDERAL</td>
      <td>3</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>40</td>
      <td>PSB</td>
      <td>PARTIDO SOCIALISTA BRASILEIRO</td>
      <td>70000050382</td>
      <td>Brasília de Mãos Limpas</td>
      <td>PSB / PV / PC do B / PDT / REDE</td>
    </tr>
    <tr>
      <th>6194</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>PR</td>
      <td>...</td>
      <td>PARANÁ</td>
      <td>7</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>33</td>
      <td>PMN</td>
      <td>PARTIDO DA MOBILIZAÇÃO NACIONAL</td>
      <td>160000050593</td>
      <td>FIRME E FORTE, UNIDOS PELO PARANA</td>
      <td>PROS / PMB / PMN</td>
    </tr>
    <tr>
      <th>6195</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>SC</td>
      <td>...</td>
      <td>SANTA CATARINA</td>
      <td>10</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>70</td>
      <td>AVANTE</td>
      <td>AVANTE</td>
      <td>240000050249</td>
      <td>SANTA CATARINA QUER MAIS</td>
      <td>MDB / AVANTE / PSDB / PTB / PTC / PRTB / DC / ...</td>
    </tr>
    <tr>
      <th>6196</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>MA</td>
      <td>...</td>
      <td>MARANHÃO</td>
      <td>3</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>25</td>
      <td>DEM</td>
      <td>DEMOCRATAS</td>
      <td>100000050110</td>
      <td>TODOS PELO MARANHÃO</td>
      <td>PC do B / PRB / PDT / PPS / DEM / PSB / PR / P...</td>
    </tr>
    <tr>
      <th>6197</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>SC</td>
      <td>...</td>
      <td>SANTA CATARINA</td>
      <td>7</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>25</td>
      <td>DEM</td>
      <td>DEMOCRATAS</td>
      <td>240000050745</td>
      <td>AQUI TEM TRABALHO</td>
      <td>DEM / PROS / PPL / PRP / PV</td>
    </tr>
    <tr>
      <th>6198</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>PB</td>
      <td>...</td>
      <td>PARAÍBA</td>
      <td>6</td>
      <td>DEPUTADO FEDERAL</td>
      <td>COLIGACAO</td>
      <td>43</td>
      <td>PV</td>
      <td>PARTIDO VERDE</td>
      <td>150000050332</td>
      <td>FORÇA DA ESPERANÇA I</td>
      <td>PV / PSDB / PSD / PSC / SOLIDARIEDADE</td>
    </tr>
    <tr>
      <th>6199</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>ES</td>
      <td>...</td>
      <td>ESPÍRITO SANTO</td>
      <td>10</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>43</td>
      <td>PV</td>
      <td>PARTIDO VERDE</td>
      <td>80000050688</td>
      <td>ESPIRITO SANTO MAIS IGUAL</td>
      <td>PSB / PHS / PROS / PV / PSC / AVANTE / PTC / P...</td>
    </tr>
    <tr>
      <th>6200</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>TO</td>
      <td>...</td>
      <td>TOCANTINS</td>
      <td>7</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>70</td>
      <td>AVANTE</td>
      <td>AVANTE</td>
      <td>270000050488</td>
      <td>TOCANTINS DE OPORTUNIDADES 1</td>
      <td>PHS / PROS / PP / DEM / AVANTE / PATRI / SOLID...</td>
    </tr>
    <tr>
      <th>6201</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RO</td>
      <td>...</td>
      <td>RONDÔNIA</td>
      <td>7</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>50</td>
      <td>PSOL</td>
      <td>PARTIDO SOCIALISMO E LIBERDADE</td>
      <td>220000050591</td>
      <td>SEM MEDO DE SER FELIZ</td>
      <td>PT / PSOL</td>
    </tr>
    <tr>
      <th>6202</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>SC</td>
      <td>...</td>
      <td>SANTA CATARINA</td>
      <td>3</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>44</td>
      <td>PRP</td>
      <td>PARTIDO REPUBLICANO PROGRESSISTA</td>
      <td>240000050553</td>
      <td>AQUI É TRABALHO</td>
      <td>PSD / PRB / PDT / PSB / PODE / SOLIDARIEDADE /...</td>
    </tr>
    <tr>
      <th>6203</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>MT</td>
      <td>...</td>
      <td>MATO GROSSO</td>
      <td>7</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>40</td>
      <td>PSB</td>
      <td>PARTIDO SOCIALISTA BRASILEIRO</td>
      <td>110000050341</td>
      <td>Segue em frente Mato Grosso III</td>
      <td>PSB / PPS</td>
    </tr>
    <tr>
      <th>6204</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>MG</td>
      <td>...</td>
      <td>MINAS GERAIS</td>
      <td>9</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>14</td>
      <td>PTB</td>
      <td>PARTIDO TRABALHISTA BRASILEIRO</td>
      <td>130000050129</td>
      <td>RECONSTRUIR MINAS</td>
      <td>PSDB / PSD / SOLIDARIEDADE / PTB / PPS / PMN /...</td>
    </tr>
    <tr>
      <th>6205</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RR</td>
      <td>...</td>
      <td>RORAIMA</td>
      <td>7</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>14</td>
      <td>PTB</td>
      <td>PARTIDO TRABALHISTA BRASILEIRO</td>
      <td>230000050429</td>
      <td>SOMOS TODOS RORAIMA</td>
      <td>PTB / REDE / PT</td>
    </tr>
    <tr>
      <th>6206</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>RJ</td>
      <td>...</td>
      <td>RIO DE JANEIRO</td>
      <td>4</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>19</td>
      <td>PODE</td>
      <td>PODEMOS</td>
      <td>190000050290</td>
      <td>A FORÇA QUE VEM DO POVO</td>
      <td>PODE / PR / REDE / PPL</td>
    </tr>
    <tr>
      <th>6207</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>GO</td>
      <td>...</td>
      <td>GOIÁS</td>
      <td>3</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>10</td>
      <td>PRB</td>
      <td>PARTIDO REPUBLICANO BRASILEIRO</td>
      <td>90000050238</td>
      <td>NOVAS IDEIAS NOVO GOIÁS</td>
      <td>MDB / PRB / PHS / PP</td>
    </tr>
    <tr>
      <th>6208</th>
      <td>30/09/2018</td>
      <td>08:04:54</td>
      <td>2018</td>
      <td>2</td>
      <td>ELEIÇÃO ORDINÁRIA</td>
      <td>1</td>
      <td>297</td>
      <td>Eleições Gerais Estaduais 2018</td>
      <td>07/10/2018</td>
      <td>PR</td>
      <td>...</td>
      <td>PARANÁ</td>
      <td>5</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>28</td>
      <td>PRTB</td>
      <td>PARTIDO RENOVADOR TRABALHISTA BRASILEIRO</td>
      <td>160000050563</td>
      <td>UNIDOS PELO PARANÁ</td>
      <td>PRTB / PRP</td>
    </tr>
  </tbody>
</table>
<p>6209 rows × 21 columns</p>
</div>




```python
# Removing some unused columns, creating a new "data1" dataframe
colsToDrop = ['DT_GERACAO','HH_GERACAO','CD_ELEICAO','DT_ELEICAO', 'SQ_COLIGACAO', 'NR_PARTIDO' , 'DS_ELEICAO', 'SG_UE', 'CD_TIPO_ELEICAO', 'NM_TIPO_ELEICAO','NR_TURNO', 'NM_UE', 'CD_CARGO', 'NM_PARTIDO']
data1 = data.drop(colsToDrop, axis=1)
data1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ANO_ELEICAO</th>
      <th>SG_UF</th>
      <th>DS_CARGO</th>
      <th>TP_AGREMIACAO</th>
      <th>SG_PARTIDO</th>
      <th>NM_COLIGACAO</th>
      <th>DS_COMPOSICAO_COLIGACAO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018</td>
      <td>BA</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PROS</td>
      <td>MAIS TRABALHO POR TODA A BAHIA</td>
      <td>PT / PP / PDT / PSD / PSB / PC do B / PR / PMB...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018</td>
      <td>RR</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PSD</td>
      <td>TODOS POR RORAIMA</td>
      <td>PSDB / DEM / MDB / PSD / PPS / SOLIDARIEDADE / DC</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018</td>
      <td>RS</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PSC</td>
      <td>RIO GRANDE NO RUMO CERTO</td>
      <td>MDB / PSD / PSB / PR / PSC / PATRI / PRP / PMN...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2018</td>
      <td>MA</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PPS</td>
      <td>TODOS PELO MARANHÃO</td>
      <td>PC do B / PRB / PDT / PPS / DEM / PSB / PR / P...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2018</td>
      <td>TO</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PV</td>
      <td>Coligação Frente Alternativa</td>
      <td>REDE / PRTB / PTB / PC do B / PT / PV / PDT / PSD</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2018</td>
      <td>PI</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PRB</td>
      <td>MUDAR PARA CUIDAR DA NOSSA GENTE</td>
      <td>PMN / PRB / SOLIDARIEDADE / PPL / PTC</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2018</td>
      <td>ES</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PRB</td>
      <td>COLIGAÇÃO EM DEFESA DA VIDA E DA FAMILIA</td>
      <td>PR / PRB / PSL</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2018</td>
      <td>RJ</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PCB</td>
      <td>MUDAR É POSSÍVEL</td>
      <td>PSOL / PCB</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2018</td>
      <td>AL</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PR</td>
      <td>Avança Mais Alagoas</td>
      <td>MDB / PODE / PPS / PDT / PR / PTB / PHS / PV /...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2018</td>
      <td>PA</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PC do B</td>
      <td>PRA VIVER EM PAZ</td>
      <td>PT / PC do B</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2018</td>
      <td>PE</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>MDB</td>
      <td>FRENTE POPULAR DE PERNAMBUCO PARA DEPUTADO EST...</td>
      <td>PSB / MDB / PSD</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2018</td>
      <td>AP</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PSDB</td>
      <td>TRABALHO E UNIÃO PELO AMAPÁ</td>
      <td>DEM / REDE / PSDB / PPL / PP / PSC / AVANTE / ...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2018</td>
      <td>MA</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PR</td>
      <td>TODOS PELO MARANHÃO</td>
      <td>PC do B / PRB / PDT / PPS / DEM / PSB / PR / P...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2018</td>
      <td>BA</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PMN</td>
      <td>MAIS TRABALHO POR TODA A BAHIA</td>
      <td>PT / PP / PDT / PSD / PSB / PC do B / PR / PMB...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2018</td>
      <td>RO</td>
      <td>SENADOR</td>
      <td>PARTIDO ISOLADO</td>
      <td>PMB</td>
      <td>#NULO#</td>
      <td>PMB</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2018</td>
      <td>MA</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PP</td>
      <td>TODOS PELO MARANHÃO</td>
      <td>PC do B / PRB / PDT / PPS / DEM / PSB / PR / P...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2018</td>
      <td>RR</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PTB</td>
      <td>DÊ UMA CHANCE PARA RORAIMA</td>
      <td>PTB / PV / REDE / PT</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2018</td>
      <td>TO</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>PP</td>
      <td>GOVERNO DE ATITUDE</td>
      <td>PHS / SOLIDARIEDADE / PP / DEM / PTC / PRB / A...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2018</td>
      <td>MA</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>PHS</td>
      <td>CORAGEM E UNIÃO PARA FAZER O MARANHÃO MELHOR</td>
      <td>PODE / REDE / DC / PHS / PMN / PSDB</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2018</td>
      <td>RJ</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>REDE</td>
      <td>A FORÇA QUE VEM DO POVO</td>
      <td>PODE / PR / REDE / PPL</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2018</td>
      <td>SE</td>
      <td>DEPUTADO FEDERAL</td>
      <td>COLIGACAO</td>
      <td>PMN</td>
      <td>PARA RENOVAR SERGIPE</td>
      <td>PODE / AVANTE / PMN / PATRI</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2018</td>
      <td>RS</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PT</td>
      <td>POR UM RIO GRANDE JUSTO</td>
      <td>PT / PC do B</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2018</td>
      <td>RJ</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PTC</td>
      <td>Para o Povo Voltar a Ser Feliz</td>
      <td>PRP / PRB / PTC / PATRI</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2018</td>
      <td>RO</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>PV</td>
      <td>RONDONIA, UNIDOS SOMOS FORTES 2</td>
      <td>MDB / PV</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2018</td>
      <td>CE</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>PARTIDO ISOLADO</td>
      <td>PSTU</td>
      <td>#NULO#</td>
      <td>PSTU</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2018</td>
      <td>DF</td>
      <td>VICE-GOVERNADOR</td>
      <td>PARTIDO ISOLADO</td>
      <td>NOVO</td>
      <td>#NULO#</td>
      <td>NOVO</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2018</td>
      <td>DF</td>
      <td>DEPUTADO FEDERAL</td>
      <td>PARTIDO ISOLADO</td>
      <td>PR</td>
      <td>#NULO#</td>
      <td>PR</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2018</td>
      <td>MG</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>PMB</td>
      <td>RENOVAÇÃO</td>
      <td>PATRI / PTC / PMB</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2018</td>
      <td>RS</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>PTC</td>
      <td>RIO GRANDE NO RUMO CERTO</td>
      <td>MDB / PSD / PSB / PR / PSC / PATRI / PRP / PMN...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2018</td>
      <td>RS</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PR</td>
      <td>RIO GRANDE NO RUMO CERTO</td>
      <td>MDB / PSD / PSB / PR / PSC / PATRI / PRP / PMN...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6179</th>
      <td>2018</td>
      <td>PR</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>PSDB</td>
      <td>PARANA DECIDE</td>
      <td>PP / PTB / DEM / PMN / PMB / PSB / PSDB / PROS</td>
    </tr>
    <tr>
      <th>6180</th>
      <td>2018</td>
      <td>RN</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>PPS</td>
      <td>TRABALHO E SUPERAÇÃO</td>
      <td>PRB / PTB / PR / PPS / PMB / PTC / PSB / PRP /...</td>
    </tr>
    <tr>
      <th>6181</th>
      <td>2018</td>
      <td>AM</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>SOLIDARIEDADE</td>
      <td>EU VOTO NO AMAZONAS</td>
      <td>PDT / PRP / AVANTE / PP / PV / PR / SOLIDARIED...</td>
    </tr>
    <tr>
      <th>6182</th>
      <td>2018</td>
      <td>CE</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>PSOL</td>
      <td>FRENTE DE ESQUERDA SOCIALISTA</td>
      <td>PSOL</td>
    </tr>
    <tr>
      <th>6183</th>
      <td>2018</td>
      <td>AC</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PSC</td>
      <td>Muda Acre de Verdade</td>
      <td>PSL / PATRI / PSC</td>
    </tr>
    <tr>
      <th>6184</th>
      <td>2018</td>
      <td>AL</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PTB</td>
      <td>Avança Mais Alagoas</td>
      <td>MDB / PODE / PPS / PDT / PR / PTB / PHS / PV /...</td>
    </tr>
    <tr>
      <th>6185</th>
      <td>2018</td>
      <td>SP</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PTB</td>
      <td>São Paulo Confia e Avança</td>
      <td>PSB / PSC / PPS / PTB / PV / PR / PODE / PMB /...</td>
    </tr>
    <tr>
      <th>6186</th>
      <td>2018</td>
      <td>SP</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PC do B</td>
      <td>SÃO PAULO DO TRABALHO  E DE OPORTUNIDADES</td>
      <td>PT / PC do B</td>
    </tr>
    <tr>
      <th>6187</th>
      <td>2018</td>
      <td>SC</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PC do B</td>
      <td>AQUI É TRABALHO</td>
      <td>PSD / PRB / PDT / PSB / PODE / SOLIDARIEDADE /...</td>
    </tr>
    <tr>
      <th>6188</th>
      <td>2018</td>
      <td>MG</td>
      <td>1º SUPLENTE</td>
      <td>PARTIDO ISOLADO</td>
      <td>NOVO</td>
      <td>#NULO#</td>
      <td>NOVO</td>
    </tr>
    <tr>
      <th>6189</th>
      <td>2018</td>
      <td>MG</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PODE</td>
      <td>#MinasTemJeito</td>
      <td>PDT / PODE / MDB / PROS / PRB / PV</td>
    </tr>
    <tr>
      <th>6190</th>
      <td>2018</td>
      <td>PI</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PODE</td>
      <td>RESISTÊNCIA PELO PIAUÍ</td>
      <td>PODE / AVANTE / PATRI / REDE / PPS / PV / PRP ...</td>
    </tr>
    <tr>
      <th>6191</th>
      <td>2018</td>
      <td>AP</td>
      <td>GOVERNADOR</td>
      <td>PARTIDO ISOLADO</td>
      <td>PSTU</td>
      <td>#NULO#</td>
      <td>PSTU</td>
    </tr>
    <tr>
      <th>6192</th>
      <td>2018</td>
      <td>AP</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PSB</td>
      <td>COM O POVO PRA AVANÇAR</td>
      <td>PT / PSB</td>
    </tr>
    <tr>
      <th>6193</th>
      <td>2018</td>
      <td>DF</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PSB</td>
      <td>Brasília de Mãos Limpas</td>
      <td>PSB / PV / PC do B / PDT / REDE</td>
    </tr>
    <tr>
      <th>6194</th>
      <td>2018</td>
      <td>PR</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>PMN</td>
      <td>FIRME E FORTE, UNIDOS PELO PARANA</td>
      <td>PROS / PMB / PMN</td>
    </tr>
    <tr>
      <th>6195</th>
      <td>2018</td>
      <td>SC</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>AVANTE</td>
      <td>SANTA CATARINA QUER MAIS</td>
      <td>MDB / AVANTE / PSDB / PTB / PTC / PRTB / DC / ...</td>
    </tr>
    <tr>
      <th>6196</th>
      <td>2018</td>
      <td>MA</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>DEM</td>
      <td>TODOS PELO MARANHÃO</td>
      <td>PC do B / PRB / PDT / PPS / DEM / PSB / PR / P...</td>
    </tr>
    <tr>
      <th>6197</th>
      <td>2018</td>
      <td>SC</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>DEM</td>
      <td>AQUI TEM TRABALHO</td>
      <td>DEM / PROS / PPL / PRP / PV</td>
    </tr>
    <tr>
      <th>6198</th>
      <td>2018</td>
      <td>PB</td>
      <td>DEPUTADO FEDERAL</td>
      <td>COLIGACAO</td>
      <td>PV</td>
      <td>FORÇA DA ESPERANÇA I</td>
      <td>PV / PSDB / PSD / PSC / SOLIDARIEDADE</td>
    </tr>
    <tr>
      <th>6199</th>
      <td>2018</td>
      <td>ES</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PV</td>
      <td>ESPIRITO SANTO MAIS IGUAL</td>
      <td>PSB / PHS / PROS / PV / PSC / AVANTE / PTC / P...</td>
    </tr>
    <tr>
      <th>6200</th>
      <td>2018</td>
      <td>TO</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>AVANTE</td>
      <td>TOCANTINS DE OPORTUNIDADES 1</td>
      <td>PHS / PROS / PP / DEM / AVANTE / PATRI / SOLID...</td>
    </tr>
    <tr>
      <th>6201</th>
      <td>2018</td>
      <td>RO</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>PSOL</td>
      <td>SEM MEDO DE SER FELIZ</td>
      <td>PT / PSOL</td>
    </tr>
    <tr>
      <th>6202</th>
      <td>2018</td>
      <td>SC</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PRP</td>
      <td>AQUI É TRABALHO</td>
      <td>PSD / PRB / PDT / PSB / PODE / SOLIDARIEDADE /...</td>
    </tr>
    <tr>
      <th>6203</th>
      <td>2018</td>
      <td>MT</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>PSB</td>
      <td>Segue em frente Mato Grosso III</td>
      <td>PSB / PPS</td>
    </tr>
    <tr>
      <th>6204</th>
      <td>2018</td>
      <td>MG</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PTB</td>
      <td>RECONSTRUIR MINAS</td>
      <td>PSDB / PSD / SOLIDARIEDADE / PTB / PPS / PMN /...</td>
    </tr>
    <tr>
      <th>6205</th>
      <td>2018</td>
      <td>RR</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>PTB</td>
      <td>SOMOS TODOS RORAIMA</td>
      <td>PTB / REDE / PT</td>
    </tr>
    <tr>
      <th>6206</th>
      <td>2018</td>
      <td>RJ</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PODE</td>
      <td>A FORÇA QUE VEM DO POVO</td>
      <td>PODE / PR / REDE / PPL</td>
    </tr>
    <tr>
      <th>6207</th>
      <td>2018</td>
      <td>GO</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PRB</td>
      <td>NOVAS IDEIAS NOVO GOIÁS</td>
      <td>MDB / PRB / PHS / PP</td>
    </tr>
    <tr>
      <th>6208</th>
      <td>2018</td>
      <td>PR</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>PRTB</td>
      <td>UNIDOS PELO PARANÁ</td>
      <td>PRTB / PRP</td>
    </tr>
  </tbody>
</table>
<p>6209 rows × 7 columns</p>
</div>




```python
# Spliting "Coalition" column into 18 new columns
data2 = data1['DS_COMPOSICAO_COLIGACAO'].str.split(' / ',20,expand=True)
data1 = data1.join(data2)
data1 = data1.drop('DS_COMPOSICAO_COLIGACAO', axis=1)
data1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ANO_ELEICAO</th>
      <th>SG_UF</th>
      <th>DS_CARGO</th>
      <th>TP_AGREMIACAO</th>
      <th>SG_PARTIDO</th>
      <th>NM_COLIGACAO</th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>...</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
      <th>16</th>
      <th>17</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018</td>
      <td>BA</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PROS</td>
      <td>MAIS TRABALHO POR TODA A BAHIA</td>
      <td>PT</td>
      <td>PP</td>
      <td>PDT</td>
      <td>PSD</td>
      <td>...</td>
      <td>PRP</td>
      <td>PODE</td>
      <td>AVANTE</td>
      <td>PMN</td>
      <td>PROS</td>
      <td>PTC</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018</td>
      <td>RR</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PSD</td>
      <td>TODOS POR RORAIMA</td>
      <td>PSDB</td>
      <td>DEM</td>
      <td>MDB</td>
      <td>PSD</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018</td>
      <td>RS</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PSC</td>
      <td>RIO GRANDE NO RUMO CERTO</td>
      <td>MDB</td>
      <td>PSD</td>
      <td>PSB</td>
      <td>PR</td>
      <td>...</td>
      <td>PTC</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2018</td>
      <td>MA</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PPS</td>
      <td>TODOS PELO MARANHÃO</td>
      <td>PC do B</td>
      <td>PRB</td>
      <td>PDT</td>
      <td>PPS</td>
      <td>...</td>
      <td>PROS</td>
      <td>PT</td>
      <td>PTB</td>
      <td>PATRI</td>
      <td>PTC</td>
      <td>SOLIDARIEDADE</td>
      <td>PPL</td>
      <td>AVANTE</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2018</td>
      <td>TO</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PV</td>
      <td>Coligação Frente Alternativa</td>
      <td>REDE</td>
      <td>PRTB</td>
      <td>PTB</td>
      <td>PC do B</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2018</td>
      <td>PI</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PRB</td>
      <td>MUDAR PARA CUIDAR DA NOSSA GENTE</td>
      <td>PMN</td>
      <td>PRB</td>
      <td>SOLIDARIEDADE</td>
      <td>PPL</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2018</td>
      <td>ES</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PRB</td>
      <td>COLIGAÇÃO EM DEFESA DA VIDA E DA FAMILIA</td>
      <td>PR</td>
      <td>PRB</td>
      <td>PSL</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2018</td>
      <td>RJ</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PCB</td>
      <td>MUDAR É POSSÍVEL</td>
      <td>PSOL</td>
      <td>PCB</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2018</td>
      <td>AL</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PR</td>
      <td>Avança Mais Alagoas</td>
      <td>MDB</td>
      <td>PODE</td>
      <td>PPS</td>
      <td>PDT</td>
      <td>...</td>
      <td>PT</td>
      <td>PRP</td>
      <td>PRTB</td>
      <td>PSD</td>
      <td>PC do B</td>
      <td>DC</td>
      <td>AVANTE</td>
      <td>SOLIDARIEDADE</td>
      <td>PMN</td>
      <td>None</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2018</td>
      <td>PA</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PC do B</td>
      <td>PRA VIVER EM PAZ</td>
      <td>PT</td>
      <td>PC do B</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2018</td>
      <td>PE</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>MDB</td>
      <td>FRENTE POPULAR DE PERNAMBUCO PARA DEPUTADO EST...</td>
      <td>PSB</td>
      <td>MDB</td>
      <td>PSD</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2018</td>
      <td>AP</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PSDB</td>
      <td>TRABALHO E UNIÃO PELO AMAPÁ</td>
      <td>DEM</td>
      <td>REDE</td>
      <td>PSDB</td>
      <td>PPL</td>
      <td>...</td>
      <td>PODE</td>
      <td>SOLIDARIEDADE</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2018</td>
      <td>MA</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PR</td>
      <td>TODOS PELO MARANHÃO</td>
      <td>PC do B</td>
      <td>PRB</td>
      <td>PDT</td>
      <td>PPS</td>
      <td>...</td>
      <td>PROS</td>
      <td>PT</td>
      <td>PTB</td>
      <td>PATRI</td>
      <td>PTC</td>
      <td>SOLIDARIEDADE</td>
      <td>PPL</td>
      <td>AVANTE</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2018</td>
      <td>BA</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PMN</td>
      <td>MAIS TRABALHO POR TODA A BAHIA</td>
      <td>PT</td>
      <td>PP</td>
      <td>PDT</td>
      <td>PSD</td>
      <td>...</td>
      <td>PRP</td>
      <td>PODE</td>
      <td>AVANTE</td>
      <td>PMN</td>
      <td>PROS</td>
      <td>PTC</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2018</td>
      <td>RO</td>
      <td>SENADOR</td>
      <td>PARTIDO ISOLADO</td>
      <td>PMB</td>
      <td>#NULO#</td>
      <td>PMB</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2018</td>
      <td>MA</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PP</td>
      <td>TODOS PELO MARANHÃO</td>
      <td>PC do B</td>
      <td>PRB</td>
      <td>PDT</td>
      <td>PPS</td>
      <td>...</td>
      <td>PROS</td>
      <td>PT</td>
      <td>PTB</td>
      <td>PATRI</td>
      <td>PTC</td>
      <td>SOLIDARIEDADE</td>
      <td>PPL</td>
      <td>AVANTE</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2018</td>
      <td>RR</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PTB</td>
      <td>DÊ UMA CHANCE PARA RORAIMA</td>
      <td>PTB</td>
      <td>PV</td>
      <td>REDE</td>
      <td>PT</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2018</td>
      <td>TO</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>PP</td>
      <td>GOVERNO DE ATITUDE</td>
      <td>PHS</td>
      <td>SOLIDARIEDADE</td>
      <td>PP</td>
      <td>DEM</td>
      <td>...</td>
      <td>PROS</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2018</td>
      <td>MA</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>PHS</td>
      <td>CORAGEM E UNIÃO PARA FAZER O MARANHÃO MELHOR</td>
      <td>PODE</td>
      <td>REDE</td>
      <td>DC</td>
      <td>PHS</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2018</td>
      <td>RJ</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>REDE</td>
      <td>A FORÇA QUE VEM DO POVO</td>
      <td>PODE</td>
      <td>PR</td>
      <td>REDE</td>
      <td>PPL</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2018</td>
      <td>SE</td>
      <td>DEPUTADO FEDERAL</td>
      <td>COLIGACAO</td>
      <td>PMN</td>
      <td>PARA RENOVAR SERGIPE</td>
      <td>PODE</td>
      <td>AVANTE</td>
      <td>PMN</td>
      <td>PATRI</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2018</td>
      <td>RS</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PT</td>
      <td>POR UM RIO GRANDE JUSTO</td>
      <td>PT</td>
      <td>PC do B</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2018</td>
      <td>RJ</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PTC</td>
      <td>Para o Povo Voltar a Ser Feliz</td>
      <td>PRP</td>
      <td>PRB</td>
      <td>PTC</td>
      <td>PATRI</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2018</td>
      <td>RO</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>PV</td>
      <td>RONDONIA, UNIDOS SOMOS FORTES 2</td>
      <td>MDB</td>
      <td>PV</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2018</td>
      <td>CE</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>PARTIDO ISOLADO</td>
      <td>PSTU</td>
      <td>#NULO#</td>
      <td>PSTU</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2018</td>
      <td>DF</td>
      <td>VICE-GOVERNADOR</td>
      <td>PARTIDO ISOLADO</td>
      <td>NOVO</td>
      <td>#NULO#</td>
      <td>NOVO</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2018</td>
      <td>DF</td>
      <td>DEPUTADO FEDERAL</td>
      <td>PARTIDO ISOLADO</td>
      <td>PR</td>
      <td>#NULO#</td>
      <td>PR</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2018</td>
      <td>MG</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>PMB</td>
      <td>RENOVAÇÃO</td>
      <td>PATRI</td>
      <td>PTC</td>
      <td>PMB</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2018</td>
      <td>RS</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>PTC</td>
      <td>RIO GRANDE NO RUMO CERTO</td>
      <td>MDB</td>
      <td>PSD</td>
      <td>PSB</td>
      <td>PR</td>
      <td>...</td>
      <td>PTC</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2018</td>
      <td>RS</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PR</td>
      <td>RIO GRANDE NO RUMO CERTO</td>
      <td>MDB</td>
      <td>PSD</td>
      <td>PSB</td>
      <td>PR</td>
      <td>...</td>
      <td>PTC</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6179</th>
      <td>2018</td>
      <td>PR</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>PSDB</td>
      <td>PARANA DECIDE</td>
      <td>PP</td>
      <td>PTB</td>
      <td>DEM</td>
      <td>PMN</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6180</th>
      <td>2018</td>
      <td>RN</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>PPS</td>
      <td>TRABALHO E SUPERAÇÃO</td>
      <td>PRB</td>
      <td>PTB</td>
      <td>PR</td>
      <td>PPS</td>
      <td>...</td>
      <td>PSDB</td>
      <td>PSD</td>
      <td>AVANTE</td>
      <td>PROS</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6181</th>
      <td>2018</td>
      <td>AM</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>SOLIDARIEDADE</td>
      <td>EU VOTO NO AMAZONAS</td>
      <td>PDT</td>
      <td>PRP</td>
      <td>AVANTE</td>
      <td>PP</td>
      <td>...</td>
      <td>PTB</td>
      <td>PHS</td>
      <td>PSL</td>
      <td>PPL</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6182</th>
      <td>2018</td>
      <td>CE</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>PSOL</td>
      <td>FRENTE DE ESQUERDA SOCIALISTA</td>
      <td>PSOL</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6183</th>
      <td>2018</td>
      <td>AC</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PSC</td>
      <td>Muda Acre de Verdade</td>
      <td>PSL</td>
      <td>PATRI</td>
      <td>PSC</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6184</th>
      <td>2018</td>
      <td>AL</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PTB</td>
      <td>Avança Mais Alagoas</td>
      <td>MDB</td>
      <td>PODE</td>
      <td>PPS</td>
      <td>PDT</td>
      <td>...</td>
      <td>PT</td>
      <td>PRP</td>
      <td>PRTB</td>
      <td>PSD</td>
      <td>PC do B</td>
      <td>DC</td>
      <td>AVANTE</td>
      <td>SOLIDARIEDADE</td>
      <td>PMN</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6185</th>
      <td>2018</td>
      <td>SP</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PTB</td>
      <td>São Paulo Confia e Avança</td>
      <td>PSB</td>
      <td>PSC</td>
      <td>PPS</td>
      <td>PTB</td>
      <td>...</td>
      <td>PHS</td>
      <td>PPL</td>
      <td>PRP</td>
      <td>PATRI</td>
      <td>PROS</td>
      <td>SOLIDARIEDADE</td>
      <td>AVANTE</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6186</th>
      <td>2018</td>
      <td>SP</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PC do B</td>
      <td>SÃO PAULO DO TRABALHO  E DE OPORTUNIDADES</td>
      <td>PT</td>
      <td>PC do B</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6187</th>
      <td>2018</td>
      <td>SC</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PC do B</td>
      <td>AQUI É TRABALHO</td>
      <td>PSD</td>
      <td>PRB</td>
      <td>PDT</td>
      <td>PSB</td>
      <td>...</td>
      <td>PC do B</td>
      <td>PHS</td>
      <td>PP</td>
      <td>DEM</td>
      <td>PRP</td>
      <td>PPL</td>
      <td>PV</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6188</th>
      <td>2018</td>
      <td>MG</td>
      <td>1º SUPLENTE</td>
      <td>PARTIDO ISOLADO</td>
      <td>NOVO</td>
      <td>#NULO#</td>
      <td>NOVO</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6189</th>
      <td>2018</td>
      <td>MG</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PODE</td>
      <td>#MinasTemJeito</td>
      <td>PDT</td>
      <td>PODE</td>
      <td>MDB</td>
      <td>PROS</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6190</th>
      <td>2018</td>
      <td>PI</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PODE</td>
      <td>RESISTÊNCIA PELO PIAUÍ</td>
      <td>PODE</td>
      <td>AVANTE</td>
      <td>PATRI</td>
      <td>REDE</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6191</th>
      <td>2018</td>
      <td>AP</td>
      <td>GOVERNADOR</td>
      <td>PARTIDO ISOLADO</td>
      <td>PSTU</td>
      <td>#NULO#</td>
      <td>PSTU</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6192</th>
      <td>2018</td>
      <td>AP</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PSB</td>
      <td>COM O POVO PRA AVANÇAR</td>
      <td>PT</td>
      <td>PSB</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6193</th>
      <td>2018</td>
      <td>DF</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PSB</td>
      <td>Brasília de Mãos Limpas</td>
      <td>PSB</td>
      <td>PV</td>
      <td>PC do B</td>
      <td>PDT</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6194</th>
      <td>2018</td>
      <td>PR</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>PMN</td>
      <td>FIRME E FORTE, UNIDOS PELO PARANA</td>
      <td>PROS</td>
      <td>PMB</td>
      <td>PMN</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6195</th>
      <td>2018</td>
      <td>SC</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>AVANTE</td>
      <td>SANTA CATARINA QUER MAIS</td>
      <td>MDB</td>
      <td>AVANTE</td>
      <td>PSDB</td>
      <td>PTB</td>
      <td>...</td>
      <td>PPS</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6196</th>
      <td>2018</td>
      <td>MA</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>DEM</td>
      <td>TODOS PELO MARANHÃO</td>
      <td>PC do B</td>
      <td>PRB</td>
      <td>PDT</td>
      <td>PPS</td>
      <td>...</td>
      <td>PROS</td>
      <td>PT</td>
      <td>PTB</td>
      <td>PATRI</td>
      <td>PTC</td>
      <td>SOLIDARIEDADE</td>
      <td>PPL</td>
      <td>AVANTE</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6197</th>
      <td>2018</td>
      <td>SC</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>DEM</td>
      <td>AQUI TEM TRABALHO</td>
      <td>DEM</td>
      <td>PROS</td>
      <td>PPL</td>
      <td>PRP</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6198</th>
      <td>2018</td>
      <td>PB</td>
      <td>DEPUTADO FEDERAL</td>
      <td>COLIGACAO</td>
      <td>PV</td>
      <td>FORÇA DA ESPERANÇA I</td>
      <td>PV</td>
      <td>PSDB</td>
      <td>PSD</td>
      <td>PSC</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6199</th>
      <td>2018</td>
      <td>ES</td>
      <td>2º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PV</td>
      <td>ESPIRITO SANTO MAIS IGUAL</td>
      <td>PSB</td>
      <td>PHS</td>
      <td>PROS</td>
      <td>PV</td>
      <td>...</td>
      <td>PSDB</td>
      <td>DEM</td>
      <td>PDT</td>
      <td>PP</td>
      <td>PC do B</td>
      <td>PPL</td>
      <td>DC</td>
      <td>SOLIDARIEDADE</td>
      <td>PRP</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>6200</th>
      <td>2018</td>
      <td>TO</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>AVANTE</td>
      <td>TOCANTINS DE OPORTUNIDADES 1</td>
      <td>PHS</td>
      <td>PROS</td>
      <td>PP</td>
      <td>DEM</td>
      <td>...</td>
      <td>PTC</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6201</th>
      <td>2018</td>
      <td>RO</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>PSOL</td>
      <td>SEM MEDO DE SER FELIZ</td>
      <td>PT</td>
      <td>PSOL</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6202</th>
      <td>2018</td>
      <td>SC</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PRP</td>
      <td>AQUI É TRABALHO</td>
      <td>PSD</td>
      <td>PRB</td>
      <td>PDT</td>
      <td>PSB</td>
      <td>...</td>
      <td>PC do B</td>
      <td>PHS</td>
      <td>PP</td>
      <td>DEM</td>
      <td>PRP</td>
      <td>PPL</td>
      <td>PV</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6203</th>
      <td>2018</td>
      <td>MT</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>PSB</td>
      <td>Segue em frente Mato Grosso III</td>
      <td>PSB</td>
      <td>PPS</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6204</th>
      <td>2018</td>
      <td>MG</td>
      <td>1º SUPLENTE</td>
      <td>COLIGACAO</td>
      <td>PTB</td>
      <td>RECONSTRUIR MINAS</td>
      <td>PSDB</td>
      <td>PSD</td>
      <td>SOLIDARIEDADE</td>
      <td>PTB</td>
      <td>...</td>
      <td>PP</td>
      <td>PTC</td>
      <td>PATRI</td>
      <td>PMB</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6205</th>
      <td>2018</td>
      <td>RR</td>
      <td>DEPUTADO ESTADUAL</td>
      <td>COLIGACAO</td>
      <td>PTB</td>
      <td>SOMOS TODOS RORAIMA</td>
      <td>PTB</td>
      <td>REDE</td>
      <td>PT</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6206</th>
      <td>2018</td>
      <td>RJ</td>
      <td>VICE-GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PODE</td>
      <td>A FORÇA QUE VEM DO POVO</td>
      <td>PODE</td>
      <td>PR</td>
      <td>REDE</td>
      <td>PPL</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6207</th>
      <td>2018</td>
      <td>GO</td>
      <td>GOVERNADOR</td>
      <td>COLIGACAO</td>
      <td>PRB</td>
      <td>NOVAS IDEIAS NOVO GOIÁS</td>
      <td>MDB</td>
      <td>PRB</td>
      <td>PHS</td>
      <td>PP</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6208</th>
      <td>2018</td>
      <td>PR</td>
      <td>SENADOR</td>
      <td>COLIGACAO</td>
      <td>PRTB</td>
      <td>UNIDOS PELO PARANÁ</td>
      <td>PRTB</td>
      <td>PRP</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>6209 rows × 24 columns</p>
</div>




```python
# Init empty lists:
VERTICES = [] 
EDGES = [] 

# Building "VERTICES" list
# Creating "dataV" dataframe with columns that we need to vertices and excluding duplicate rows:
dataV = data[['SG_PARTIDO','NR_PARTIDO','NM_PARTIDO']].drop_duplicates()

# Iterating into "dataV" and append addV command into "VERTICE" list:
for row in dataV.itertuples(index=True, name='Pandas'):
    VERTICES.append('g.addV(\'PARTIDO\').property(\'id\',\''  + str(getattr(row, "NR_PARTIDO")) + '\').property(\'sigla\',\'' + getattr(row, "SG_PARTIDO") + '\').property(\'nome\',\'' + getattr(row, "NM_PARTIDO") + '\')')
    
    
VERTICES    
```




    ["g.addV('PARTIDO').property('id','90').property('sigla','PROS').property('nome','PARTIDO REPUBLICANO DA ORDEM SOCIAL')",
     "g.addV('PARTIDO').property('id','55').property('sigla','PSD').property('nome','PARTIDO SOCIAL DEMOCRÁTICO')",
     "g.addV('PARTIDO').property('id','20').property('sigla','PSC').property('nome','PARTIDO SOCIAL CRISTÃO')",
     "g.addV('PARTIDO').property('id','23').property('sigla','PPS').property('nome','PARTIDO POPULAR SOCIALISTA')",
     "g.addV('PARTIDO').property('id','43').property('sigla','PV').property('nome','PARTIDO VERDE')",
     "g.addV('PARTIDO').property('id','10').property('sigla','PRB').property('nome','PARTIDO REPUBLICANO BRASILEIRO')",
     "g.addV('PARTIDO').property('id','21').property('sigla','PCB').property('nome','PARTIDO COMUNISTA BRASILEIRO')",
     "g.addV('PARTIDO').property('id','22').property('sigla','PR').property('nome','PARTIDO DA REPÚBLICA')",
     "g.addV('PARTIDO').property('id','65').property('sigla','PC do B').property('nome','PARTIDO COMUNISTA DO BRASIL')",
     "g.addV('PARTIDO').property('id','15').property('sigla','MDB').property('nome','MOVIMENTO DEMOCRÁTICO BRASILEIRO')",
     "g.addV('PARTIDO').property('id','45').property('sigla','PSDB').property('nome','PARTIDO DA SOCIAL DEMOCRACIA BRASILEIRA')",
     "g.addV('PARTIDO').property('id','33').property('sigla','PMN').property('nome','PARTIDO DA MOBILIZAÇÃO NACIONAL')",
     "g.addV('PARTIDO').property('id','35').property('sigla','PMB').property('nome','PARTIDO DA MULHER BRASILEIRA')",
     "g.addV('PARTIDO').property('id','11').property('sigla','PP').property('nome','PARTIDO PROGRESSISTA')",
     "g.addV('PARTIDO').property('id','14').property('sigla','PTB').property('nome','PARTIDO TRABALHISTA BRASILEIRO')",
     "g.addV('PARTIDO').property('id','31').property('sigla','PHS').property('nome','PARTIDO HUMANISTA DA SOLIDARIEDADE')",
     "g.addV('PARTIDO').property('id','18').property('sigla','REDE').property('nome','REDE SUSTENTABILIDADE')",
     "g.addV('PARTIDO').property('id','13').property('sigla','PT').property('nome','PARTIDO DOS TRABALHADORES')",
     "g.addV('PARTIDO').property('id','36').property('sigla','PTC').property('nome','PARTIDO TRABALHISTA CRISTÃO')",
     "g.addV('PARTIDO').property('id','16').property('sigla','PSTU').property('nome','PARTIDO SOCIALISTA DOS TRABALHADORES UNIFICADO')",
     "g.addV('PARTIDO').property('id','30').property('sigla','NOVO').property('nome','PARTIDO NOVO')",
     "g.addV('PARTIDO').property('id','51').property('sigla','PATRI').property('nome','PATRIOTA')",
     "g.addV('PARTIDO').property('id','70').property('sigla','AVANTE').property('nome','AVANTE')",
     "g.addV('PARTIDO').property('id','77').property('sigla','SOLIDARIEDADE').property('nome','SOLIDARIEDADE')",
     "g.addV('PARTIDO').property('id','17').property('sigla','PSL').property('nome','PARTIDO SOCIAL LIBERAL')",
     "g.addV('PARTIDO').property('id','25').property('sigla','DEM').property('nome','DEMOCRATAS')",
     "g.addV('PARTIDO').property('id','50').property('sigla','PSOL').property('nome','PARTIDO SOCIALISMO E LIBERDADE')",
     "g.addV('PARTIDO').property('id','44').property('sigla','PRP').property('nome','PARTIDO REPUBLICANO PROGRESSISTA')",
     "g.addV('PARTIDO').property('id','28').property('sigla','PRTB').property('nome','PARTIDO RENOVADOR TRABALHISTA BRASILEIRO')",
     "g.addV('PARTIDO').property('id','54').property('sigla','PPL').property('nome','PARTIDO PÁTRIA LIVRE')",
     "g.addV('PARTIDO').property('id','19').property('sigla','PODE').property('nome','PODEMOS')",
     "g.addV('PARTIDO').property('id','40').property('sigla','PSB').property('nome','PARTIDO SOCIALISTA BRASILEIRO')",
     "g.addV('PARTIDO').property('id','29').property('sigla','PCO').property('nome','PARTIDO DA CAUSA OPERÁRIA')",
     "g.addV('PARTIDO').property('id','12').property('sigla','PDT').property('nome','PARTIDO DEMOCRÁTICO TRABALHISTA')",
     "g.addV('PARTIDO').property('id','27').property('sigla','DC').property('nome','DEMOCRACIA CRISTÃ')"]




```python
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

dataE
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>partido</th>
      <th>coligado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PROS</td>
      <td>PT</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PSD</td>
      <td>PSDB</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PSC</td>
      <td>MDB</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PPS</td>
      <td>PC do B</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PV</td>
      <td>REDE</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PRB</td>
      <td>PMN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PRB</td>
      <td>PR</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PCB</td>
      <td>PSOL</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PR</td>
      <td>MDB</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PC do B</td>
      <td>PT</td>
    </tr>
    <tr>
      <th>10</th>
      <td>MDB</td>
      <td>PSB</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PSDB</td>
      <td>DEM</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PR</td>
      <td>PC do B</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PMN</td>
      <td>PT</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PMB</td>
      <td>PMB</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PP</td>
      <td>PC do B</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PTB</td>
      <td>PTB</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PP</td>
      <td>PHS</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PHS</td>
      <td>PODE</td>
    </tr>
    <tr>
      <th>19</th>
      <td>REDE</td>
      <td>PODE</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PMN</td>
      <td>PODE</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PT</td>
      <td>PT</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PTC</td>
      <td>PRP</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PV</td>
      <td>MDB</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PSTU</td>
      <td>PSTU</td>
    </tr>
    <tr>
      <th>25</th>
      <td>NOVO</td>
      <td>NOVO</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PR</td>
      <td>PR</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PMB</td>
      <td>PATRI</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PTC</td>
      <td>MDB</td>
    </tr>
    <tr>
      <th>32</th>
      <td>PP</td>
      <td>PSB</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>41</th>
      <td>SOLIDARIEDADE</td>
      <td>None</td>
    </tr>
    <tr>
      <th>43</th>
      <td>PSL</td>
      <td>None</td>
    </tr>
    <tr>
      <th>44</th>
      <td>DEM</td>
      <td>None</td>
    </tr>
    <tr>
      <th>47</th>
      <td>PSOL</td>
      <td>None</td>
    </tr>
    <tr>
      <th>48</th>
      <td>PRP</td>
      <td>None</td>
    </tr>
    <tr>
      <th>51</th>
      <td>PRTB</td>
      <td>None</td>
    </tr>
    <tr>
      <th>52</th>
      <td>PPL</td>
      <td>None</td>
    </tr>
    <tr>
      <th>60</th>
      <td>PODE</td>
      <td>None</td>
    </tr>
    <tr>
      <th>61</th>
      <td>PSB</td>
      <td>None</td>
    </tr>
    <tr>
      <th>63</th>
      <td>PCO</td>
      <td>None</td>
    </tr>
    <tr>
      <th>75</th>
      <td>PDT</td>
      <td>None</td>
    </tr>
    <tr>
      <th>139</th>
      <td>DC</td>
      <td>None</td>
    </tr>
    <tr>
      <th>140</th>
      <td>DC</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>175</th>
      <td>PPS</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>221</th>
      <td>PSD</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>293</th>
      <td>AVANTE</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>571</th>
      <td>PHS</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>708</th>
      <td>PPL</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>751</th>
      <td>PC do B</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>812</th>
      <td>SOLIDARIEDADE</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>849</th>
      <td>PSDB</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>1159</th>
      <td>PRP</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>1309</th>
      <td>PTC</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>PP</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>PROS</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>1641</th>
      <td>DEM</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>2115</th>
      <td>PSB</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>2525</th>
      <td>PSC</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>2716</th>
      <td>PDT</td>
      <td>PSD</td>
    </tr>
    <tr>
      <th>3455</th>
      <td>PV</td>
      <td>PSD</td>
    </tr>
  </tbody>
</table>
<p>6621 rows × 2 columns</p>
</div>




```python
# Removing null values (expected in cases with less than 18 coalitions) and dropping duplicates
dataE = dataE[dataE['coligado'].notnull()]
dataE = dataE.drop_duplicates()

# Iterating into "dataE" and append addE command into "EDGES" list:
for row in dataE.itertuples(index=True, name='Pandas'):
    EDGES.append('g.V().has(\'sigla\',\'' + getattr(row, "partido") +   '\').addE(\'coligado\').to(g.V().has(\'sigla\',\'' + getattr(row, "coligado") + '\'))')

EDGES
```




    ["g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PCB').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PSTU').addE('coligado').to(g.V().has('sigla','PSTU'))",
     "g.V().has('sigla','NOVO').addE('coligado').to(g.V().has('sigla','NOVO'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PCO').addE('coligado').to(g.V().has('sigla','PCO'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PCB').addE('coligado').to(g.V().has('sigla','PCB'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PSTU').addE('coligado').to(g.V().has('sigla','PCB'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PCB'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PSTU').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PCB').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PDT'))",
     "g.V().has('sigla','PATRI').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','AVANTE').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PTC').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PCB'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PRB'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PV'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PCB').addE('coligado').to(g.V().has('sigla','PSTU'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PT'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PSTU'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PSC').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PPS').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PPS'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PR'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PTB'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PSC'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PTB').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PP').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PODE').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','MDB'))",
     "g.V().has('sigla','PSL').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','DEM').addE('coligado').to(g.V().has('sigla','PODE'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','DEM'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PMN').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PSD'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PV').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PRP').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','REDE').addE('coligado').to(g.V().has('sigla','PP'))",
     "g.V().has('sigla','MDB').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PMN'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','REDE'))",
     "g.V().has('sigla','PR').addE('coligado').to(g.V().has('sigla','PROS'))",
     "g.V().has('sigla','PMB').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','SOLIDARIEDADE').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','AVANTE'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PRP'))",
     "g.V().has('sigla','PPL').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PSB'))",
     "g.V().has('sigla','PSD').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PMB'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PSL'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PTC'))",
     "g.V().has('sigla','PRTB').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','DC').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PRB').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PSDB'))",
     "g.V().has('sigla','PSB').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PDT').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PHS').addE('coligado').to(g.V().has('sigla','PSOL'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PHS'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PATRI'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PROS').addE('coligado').to(g.V().has('sigla','PRTB'))",
     "g.V().has('sigla','PC do B').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PSOL').addE('coligado').to(g.V().has('sigla','DC'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','PPL'))",
     "g.V().has('sigla','PSDB').addE('coligado').to(g.V().has('sigla','PC do B'))",
     "g.V().has('sigla','PT').addE('coligado').to(g.V().has('sigla','SOLIDARIEDADE'))"]


