#Formacao Cientista de Dados - Fernando Amaral
import pandas as pd

dataset = pd.read_csv('credit.csv')
dt = dataset.iloc[:,[1,4,7]]

from sklearn.preprocessing import StandardScaler, MinMaxScaler
sc = StandardScaler()
x = sc.fit_transform(dt)

sc = MinMaxScaler()
y = sc.fit_transform(dt)
