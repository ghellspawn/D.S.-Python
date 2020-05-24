import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

base = pd.read_csv('dados/cars.csv')
base = base.drop(['Unnamed: 0'], axis = 1)

X = base.iloc[:, 1].values
X = X.reshape(-1, 1)
Y = base.iloc[:, 0].values
correlacao = np.corrcoef(X, Y)

modelo = LinearRegression()
modelo.fit(X, Y)

modelo.intercept_
modelo.coef_

plt.scatter(X, Y)
plt.plot(X, modelo.predict(X), color = 'red')

# distância 22 pés, velocidade = ?
modelo.intercept_ + modelo.coef_ * 22

modelo.predict([[22]])

modelo._residues

visualizador = ResidualsPlot(modelo)
visualizador.fit(X, Y)
visualizador.poof()