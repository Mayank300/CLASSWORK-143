from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df_data = pd.read_csv('final.csv')
df = df_data[df_data['soup'].notna()]

count = CountVectorizer(stop_words = 'english')
countMatrix = count.fit_transform(df['soup'])
cosine_sim_funtion = cosine_similarity(countMatrix, countMatrix)
df = df.reset_index()
indices = pd.Series(df.index, index=df_data['title'])

def getRecomendation(title):
  idx = indices[title]
  sim_score = list(enumerate(cosine_sim_funtion[idx]))
  sim_score = sorted(sim_score, key=lambda x:x[1], reverse=True)
  sim_score = sim_score[1:11]
  movie_indices = [i[0] for i in sim_score]
  return df[['title', 'poster_link', 'release_date', 'runtime', 'vote_average', 'overview']].iloc[movie_indices].values.tolist()