#Formacao Cientista de Dados - Fernando Amaral
import pandas as pd
dataset = pd.read_csv("Credit.csv")
X = dataset.iloc[:,8:10].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer

labelencoder = LabelEncoder()
X[:,0] = labelencoder.fit_transform(X[:,0])

onehotencoder = make_column_transformer((OneHotEncoder(categories='auto', sparse=False), [1]), remainder="passthrough")
X = onehotencoder.fit_transform(X)




