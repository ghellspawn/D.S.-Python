###################        Aula 1        #####################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

notas = pd.read_csv("ratings.csv")

notas.head()
notas.shape
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
notas.head()

notas['nota'].unique()
notas['nota'].value_counts()
notas['nota'].mean()

###################        Aula 2        #####################################

notas.nota.head()

notas.nota.plot(kind = 'hist')

notas.nota.median()

print("Media =", notas.nota.mean())
print("Mediana =", notas.nota.median())

notas.nota.describe()
sns.boxplot(notas.nota)

###################        Aula 3        #####################################

filmes = pd.read_csv("movies.csv")

filmes.columns = ["filmeId", "titulo", "generos"]
filmes.head()

notas.query("filmeId == 1").nota.mean()
notas.query("filmeId == 2").nota.mean()

medias_por_filme = notas.groupby("filmeId").mean().nota
medias_por_filme.head()

medias_por_filme.plot(kind = 'hist')
sns.boxplot(medias_por_filme)

medias_por_filme.describe()

plt.hist(medias_por_filme)
plt.title("Histograma das médias dos filmes")

###################        Aula 4        #####################################

tmdb = pd.read_csv("tmdb_5000_movies.csv")
tmdb.head()

tmdb.original_language.unique()

###################        Aula 5        #####################################

contagem_de_lingua = tmdb.original_language.value_counts().to_frame().reset_index()
contagem_de_lingua.columns = ["original_language", "total"]
contagem_de_lingua.head()

sns.barplot(x = "original_language", y = "total", data = contagem_de_lingua)
sns.catplot(x = "original_language", kind = "count", data = tmdb)

###################        Aula 5        #####################################

plt.pie(contagem_de_lingua["total"], labels = contagem_de_lingua["original_language"])

total_por_lingua = tmdb.original_language.value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc["en"]
total_do_resto = total_geral - total_de_ingles

dados = {
            'lingua' : ['Ingles', 'Outros'],
            'total' : [total_de_ingles, total_do_resto]
        }

pd.DataFrame(dados)

sns.barplot(x = "lingua", y = "total", data = dados)

plt.pie(dados["total"], labels = dados["lingua"])

total_por_lingua_de_outros_filmes = tmdb.query("original_language != 'en'").original_language.value_counts()

###################        Aula 6 e 7      ###################################

filmes_sem_lingua_original_em_ingles = tmdb.query("original_language != 'en'")
sns.catplot(x = "original_language", kind = "count", data = filmes_sem_lingua_original_em_ingles,
            aspect = 2,
            palette = "GnBu_d",
            order = total_por_lingua_de_outros_filmes.index)

###################        Aula 8        #####################################

filmes.head(2)

notas_do_toy_story = notas.query("filmeId == 1")
notas_do_jumanji = notas.query("filmeId == 2")

print(len(notas_do_toy_story), len(notas_do_jumanji))

print("Nota média do Toy Story = %.2f" % notas_do_toy_story.nota.mean())
print("Nota média do Jumanji = %.2f" % notas_do_jumanji.nota.mean())

print("Nota mediana do Toy Story = %.2f" % notas_do_toy_story.nota.median())
print("Nota mediana do Jumanji = %.2f" % notas_do_jumanji.nota.median())

filme1 = np.append(np.array([2.5] * 10), np.array([3.5] * 10)) # np.median e np.std são importantes também
filme2 = np.append(np.array([5] * 10), np.array([1] * 10))

sns.boxplot(x = "filmeId", y = "nota", data = notas.query("filmeId in [1, 2]"))

print(notas_do_toy_story.nota.std(), notas_do_jumanji.nota.std()) # Desvio padrão


