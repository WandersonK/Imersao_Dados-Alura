import pandas as pd
import matplotlib

url = 'https://gist.githubusercontent.com/tgcsantos/3bdb29eba6ce391e90df2b72205ba891/raw/22fa920e80c9fa209a9fccc8b52d74cc95d1599b/dados_imoveis.csv'

dados = pd.read_csv(url)

dados.head() # Mostra as 5 primeiras linhas
dados.head(10) # Mostra as 10 primeiras linhas
dados.sample() # Apresenta uma linha aleatória
dados.sample(10) # Apresenta 10 linhas aleatórias do conjunto de dados, pode alterar a quantidade

type(dados)

dados["Bairro"] # Apresenta somente os dados da coluna Bairro
dados["Bairro"][4] # Apresenta o item da coluna Bairro no indice 4
dados.Bairro # Outra forma de trazer somente uma coluna
dados.Bairro[4] # Apresentando o item do indice 4 na coluna Bairro

# dados.info() # Informa o tipo de dados que as colunas possuem

dados.Metragem.mean() # Informa a média da coluna metragem
dados["Metragem"].mean()
dados.Metragem.max() # Informa o maior valor da coluna metragem
dados["Metragem"].max()
dados.Metragem.min() # Informa o menor valor da coluna metragem
dados["Metragem"].min()

dados["Bairro"] == "Vila Mariana" # Conferindo se existe algum bairro chamado Vila Mariana
sum(dados["Bairro"] == "Vila Mariana") # Apresenta a soma dos valores verdadeiros, ou seja se existem bairros com nome Vila Mariana

tem_imoveis_vila = (dados["Bairro"] == "Vila Mariana") # Armazena em uma variável com True ou False, as linhas dos bairros que podem ou não conter Vila Mariana

imoveis_vila_mariana = dados[tem_imoveis_vila] # Traz de dados somente as linhas que forem True na variável tem_imoveis_vila

imoveis_vila_mariana["Metragem"].mean() # Aqui apresenta a média da metragem dos imóveis do bairro Vila Mariana

n_imoveis_bairro = dados["Bairro"].value_counts() # Faz uma contagem de quantos imóveis (valores) existem em cada bairro

n_imoveis_bairro.plot.bar() # Apresenta os dados da variável n_imoveis_bairro em um gráfico de barras
n_imoveis_bairro.head(10).plot.bar() # Apresenta os 10 primeiros dados da variável n_imoveis_bairro em um gráfico de barras