## Aula 7

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')

selecao = dados['Tipo'] == 'Apartamento'
n1 = dados[selecao].shape[0]

selecao2 = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila')
n2 = dados[selecao2].shape[0]

selecao3 = (dados['Area'] >= 60) & (dados['Area'] <= 100)
n3 = dados[selecao3].shape[0]

selecao4 = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
n4 = dados[selecao4].shape[0]

print("Nº de imóveis classificados com tipo 'Apartamento' -> {}" .format(n1))
print("Nº de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila' -> {}" .format(n2))
print("Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites -> {}" .format(n3))
print("Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 -> {}" .format(n4))

## Extra 5

data = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (9, 10, 11, 12),
        (13, 14, 15, 16)]

df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())

df['c1'] ## Selecionando colunas
df[['c3','c1']] ## Pode selecionar mais de uma coluna e se respeita a ordem

df[1:3] ## Selecionando linhas, detalhe: vai da linha 2 até a linha 3

df[1:][['c3', 'c1']]

df.loc['l3']         ## Seleciona a linha l3
df.loc[['l3', 'l2']] ## Seleciona a l3 e l2, nessa ordem
df.loc['l1', 'c2']   ## Há a possibilidade de fazer com linhas e colunas simultaneamente

df.loc[['l3', 'l1'], ['c4','c1']] ## Mesma cosia só que
df.iloc[[2,0],[3,0]]              ## escrito de maneiras diferentes.

## Aula 8

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')

dados.isnull()  ## Tratando o CSV
dados.info()

dados[dados['Valor'].isnull()]

A = dados.shape[0]
dados.dropna(subset = ['Valor'], inplace = True) ## Tirando os NaN
B = dados.shape[0]

dados[dados['Valor'].isnull()]

## Aula 9

dados[dados['Condominio'].isnull()].shape[0]

selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())
A = dados.shape[0]
dados = dados[~selecao] ## O '~' inverte a series booleana, o que é true vira false.
B = dados.shape[0]

dados = dados.fillna({'Condominio': 0, 'IPTU': 0}) ## O que era NaN virou 0.

dados.to_csv('aluguel_residencial.csv', sep = ';', index = False)

## Extra 6

data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)

s.fillna(method = 'ffill')
s.fillna(method = 'bfill')
s.fillna(s.mean())

s1 = s.fillna(method = 'ffill', limit = 1)
s1.fillna(method = 'bfill', limit = 1) ## Preencheu com o de baixo mantendo o já preenchido de cima.

## Aula 10

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')

dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']

dados['Valor M2'] = dados['Valor'] / dados['Area']
dados['Valor M2'] = dados['Valor M2'].round(2)

dados['Valor Bruto M2'] = (dados['Valor Bruto'] / dados['Area']).round(2)

casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']

## Executar uma ação em cada registro/linha do DataFrame
dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')

## Aula 11

dados_aux = pd.DataFrame(dados[['Tipo Agregado', 'Valor M2', 'Valor Bruto', 'Valor Bruto M2']])

del dados_aux['Valor Bruto']    ## Deletando um elemento do DataFrame
dados_aux.pop('Valor Bruto M2') ## Outra maneira de deletar

dados.drop(['Valor Bruto', 'Valor Bruto M2'], axis = 1, inplace = True) ## Melhor método de deletar

dados.to_csv('aluguel_residencial.csv', sep = ';', index = False)

## Extra 7

s = pd.Series(list('aassadawewwwwasdwed'))

s.unique()          ## !!! SUPER IMPORTANTE !!! ##
s.value_counts()    ## !!! SUPER IMPORTANTE !!! ##

dados = pd.read_csv('extras01/dados/aluguel.csv', sep = ';')

dados.Tipo.unique()

## Aula 12

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')

dados['Valor'].mean()

bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
selecao = dados['Bairro'].isin(bairros) ## Deixando só os bairros selecionados (os da linha acima) no DataFrame
dados = dados[selecao]
dados['Bairro'].unique() ## Verificando se deu certo

grupo_bairro = dados.groupby('Bairro')
grupo_bairro.groups

for bairro, data in grupo_bairro:
    print('{} -> {}'.format(bairro, data.Valor.mean()))
    
grupo_bairro['Valor'].mean().round(2) ## Opção mais simples de ver a média do bairro

## Aula 13

grupo_bairro['Valor'].describe().round(2)
grupo_bairro['Valor'].aggregate(['min', 'max', 'sum']).rename(columns = 
                                                              {'min' : 'Mínimo', 'max' : 'Máximo', 'sum' : 'Soma'})

fig = grupo_bairro['Valor'].mean().plot.bar(color = 'blue')
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor Médio do Aluguel por Bairro', {'fontsize':22})

## Extra 8

dados = pd.read_csv('extras01/dados/aluguel.csv', sep = ';')
dados.head(10)

classes = [0, 2, 4, 6, 100]
quartos = pd.cut(dados.Quartos, classes)
pd.value_counts(quartos)

labels = ['1 e 2 quartos', '3 e 4 quartos', '5 e 6 quartos', '7 quartos ou mais']
quartos = pd.cut(dados.Quartos, classes, labels = labels) ## Uso do 'pd.cut'
pd.value_counts(quartos)

labels = ['1 e 2 quartos', '3 e 4 quartos', '5 e 6 quartos', '7 quartos ou mais']
quartos = pd.cut(dados.Quartos, classes, labels = labels, include_lowest = True) ## Uso do 'pd.cut'
pd.value_counts(quartos)

## Aulas 13 e 14

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')

dados.boxplot(['Valor'])
dados[dados['Valor'] >= 500000]

valor = dados['Valor']

Q1 = valor.quantile(.25)
Q3 = valor.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ

selecao = (valor >= limite_inferior) & (valor <= limite_superior)
dados_new = dados[selecao]

dados_new.boxplot(['Valor'])
dados.boxplot(['Valor'], by = ['Tipo'])

grupo_tipo = dados.groupby('Tipo')['Valor']
## grupo_tipo.groups

Q1 = grupo_tipo.quantile(.25)
Q3 = grupo_tipo.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ

## limite_superior['Apartamento']

dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])
    
dados_new.boxplot(['Valor'], by = ['Tipo'])

dados_new.to_csv('aluguel.residencial_sem_outliers.csv', sep = ';')

## Extra 9

plt.rc('figure', figsize = (15,8))

dados = pd.read_csv('extras01/dados/aluguel.csv', sep = ';')
dados.head()

area = plt.figure()

g1 = area.add_subplot(2, 2, 1)
g2 = area.add_subplot(2, 2, 2)
g3 = area.add_subplot(2, 2, 3)
g4 = area.add_subplot(2, 2, 4)

g1.scatter(dados.Valor, dados.Area)
g1.set_title('Valor x Área')

g2.hist(dados.Valor)
g2.set_title('Histograma')

dados_g3 = dados.Valor.sample(100)
dados_g3.index = range(dados_g3.shape[0])
g3.plot(dados_g3)
g3.set_title('Amostra (Valor)')

grupo = dados.groupby('Tipo')['Valor']
label = grupo.mean().index
valores = grupo.mean().values
g4.bar(label, valores)
g4.set_title('Valor Médio por Tipo')

area.savefig('extras01/dados/grafico.png', dpi = 300, bbox_inches = 'tight')
