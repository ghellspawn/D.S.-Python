from scipy.stats import t

# Média de salário dos cientistas de dados = R$ 75,00 por hora
# Amostras com 9 funcionários e desvio padrão = 10

# Qual a probabilidade de selecionar um cientista de dados e o salário
# ser menor que R$ 80,00 por hora?
t.cdf(1.5, 8)

# Qual a probabilidade do salário ser maior que R$ 80,00?
t.sf(1.5, 8)
