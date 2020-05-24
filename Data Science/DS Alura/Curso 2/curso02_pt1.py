## Aula 1 e 2

import pandas as pd

dados = pd.read_csv('aluguel.csv', sep = ';')

dados.info()
dados.head()
dados.dtypes

tipos_de_dados = pd.DataFrame(dados.dtypes, columns = ['Tipos de Dados'])
tipos_de_dados.columns.name = 'Variáveis'

print('A base de dados apresenta {} registros (imóveis) e {} variáveis.'.format(dados.shape[0], dados.shape[1]))

## Extra 1

json = open('extras01/dados/aluguel.json')
print(json.read())

df_json = pd.read_json('extras01/dados/aluguel.json')
df_txt = pd.read_table('extras01/dados/aluguel.txt')
df_xlsx = pd.read_excel('extras01/dados/aluguel.xlsx')
df_html = pd.read_html('extras01/dados/dados_html_1.html')
df_html2 = pd.read_html('extras01/dados/dados_html_2.html')

## Aula 3

tipo_de_imovel = dados['Tipo']

tipo_de_imovel.drop_duplicates(inplace = True) ## Tira as duplicatas e já substitui na variável
tipo_de_imovel.unique() ## Método alternativo

## Aula 4

tipo_de_imovel = pd.DataFrame(tipo_de_imovel)

tipo_de_imovel.index
tipo_de_imovel.shape[0]

tipo_de_imovel.index = range(tipo_de_imovel.shape[0]) ## Reconfigurando o indice
tipo_de_imovel.index = range(len(tipo_de_imovel)) ## Jeito alternativo
tipo_de_imovel.columns.name = 'Id'

## Extra 2

data = [1, 2, 3, 4, 5]
s = pd.Series(data)

index = ['Linha ' + str(i) for i in range(5)]
s = pd.Series(data = data, index = index)

data = {'Linha ' + str(i) : i + 1 for i in range(5)}
s = pd.Series(data)

## Extra 3

data = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]

index = ['Linha ' + str(i) for i in range(3)]
columns = ['Coluna ' + str(i) for i in range(3)]
df1 = pd.DataFrame(data = data, index = index, columns = columns)

data = {'Coluna 0': {'Linha 0': 1, 'Linha 1': 4, 'Linha 2': 7},
        'Coluna 1': {'Linha 0': 2, 'Linha 1': 5, 'Linha 2': 8},
        'Coluna 2': {'Linha 0': 3, 'Linha 1': 6, 'Linha 2': 9}} ## Dicionário

df2 = pd.DataFrame(data)

data = [(1, 2, 3), 
        (4, 5, 6), 
        (7, 8, 9)] ## Tupla

df3 = pd.DataFrame(data = data, index = index, columns = columns)

df1[df1 > 0] = 'A'
df2[df2 > 0] = 'B'
df3[df3 > 0] = 'C'

df4 = pd.concat([df1, df2, df3]) ## Concatenação Horizontal
df4 = pd.concat([df1, df2, df3], axis = 1) ## Concatenação Vertical

## Aula 5

dados = pd.read_csv('aluguel.csv', sep = ';')

residencial = list(dados['Tipo'].drop_duplicates())

residencial = ['Quitinete',
               'Casa', 
               'Apartamento', 
               'Casa de Condomínio', 
               'Casa de Vila']

selecao = dados['Tipo'].isin(residencial) ## Deixando no DataFrame só o que eu quero

dados_residencial = dados[selecao]

list(dados_residencial['Tipo'].drop_duplicates()) ## Verificando se deu certo

dados_residencial.shape[0]
dados.shape[0]

dados_residencial.index = range(len(dados_residencial))
dados_residencial.index = range(dados_residencial.shape[0])

## Aula 6

dados_residencial.to_csv('aluguel_residencial.csv', sep = ';', index = False) ## Transformando um DataFrame em um CSV

dados_residencial_2 = pd.read_csv('aluguel_residencial.csv', sep =';')

## Extra 4

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list('321')

df = pd.DataFrame(data, list('321'), list('ZYX'))

df.sort_index(inplace = True)               ## Organizando o índice
df.sort_index(inplace = True, axis = 1)     ## Organizando a coluna

df.sort_values() ## Outra maneira de organizar o DataFrame


