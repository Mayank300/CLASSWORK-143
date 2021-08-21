import csv 

all_movies = []

with open('final.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies.append(data[1:])


liked_movies = []
disliked_movies = []
unwatched_movies = []

