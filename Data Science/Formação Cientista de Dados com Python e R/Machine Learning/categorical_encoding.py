import pandas as pd

dataset = pd.read_csv('dados/credit.csv')

x = dataset.iloc[:, 8:10].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer

labelencoder = LabelEncoder()
x[:, 0] = labelencoder.fit_transform(x[:, 0])

onehotencorder = make_column_transformer((OneHotEncoder(categories = 'auto', sparse = False), [1]), remainder = 'passthrough')
x = onehotencorder.fit_transform(x)
