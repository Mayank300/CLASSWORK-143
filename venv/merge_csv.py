import csv 

with open('movie.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    header = data[0]

header.append('poster_link')

with open('movie_links.csv') as f:
    reader = csv.reader(f)
    data  = list(reader)
    all_links = data[1:]

with open('final.csv', 'a+') as f:
    writer = csv.writer(f)
    writer.writerow(header)

for i in all_movies:
    poster_found = any(i[8] in movie_link_item for movie_link_item in all_links)
    if poster_found:
        for movie_link_item in all_links:
            if i[8] == movie_link_item[0]:
                i.append(movie_link_item[1])
                if len(i) == 28:
                    with open('final.csv', 'a+') as f:
                        writer = csv.writer(f)
                        writer.writerow(i)