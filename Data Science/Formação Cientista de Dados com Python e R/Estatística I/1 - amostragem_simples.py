import pandas as pd
import numpy as np

base = pd.read_csv('dados/iris.csv')

amostra = np.random.choice(a = [0, 1], size = 150, replace = True, p = [0.5, 0.5])

len(amostra)
len(amostra[amostra == 1])
len(amostra[amostra == 0])

## Obs: np.random.seed(n) é usado para manter um resutado do random.
