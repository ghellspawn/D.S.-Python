import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

base = pd.read_csv('dados/mt_cars.csv')
base = base.drop(['Unnamed: 0'], axis = 1)

X = base.iloc[:, 2].values
Y = base.iloc[:, 0].values
correlacao = np.corrcoef(X, Y)
X = X.reshape(-1, 1)

modelo = LinearRegression()
modelo.fit(X, Y)
modelo.intercept_
modelo.coef_
modelo.score(X, Y)

previsoes = modelo.predict(X)
modelo_ajustado = sm.ols(formula = "mpg ~ disp", data = base)
modelo_treinado = modelo_ajustado.fit()
modelo_treinado.summary()

plt.scatter(X, Y)
plt.plot(X, previsoes, color = 'red')

modelo.predict([[200]])

X1 = base.iloc[:, 1:4].values
Y1 = base.iloc[:, 0].values
modelo2 = LinearRegression()
modelo2.fit(X1, Y1)

modelo2.score(X1, Y1)
modelo_ajustado2 = sm.ols(formula = "mpg ~ cyl + disp + hp", data = base)
modelo_treinado2 = modelo_ajustado2.fit()
modelo_treinado2.summary()

novo = np.array([4, 200, 100])
novo = novo.reshape(1, -1)
modelo2.predict(novo)
