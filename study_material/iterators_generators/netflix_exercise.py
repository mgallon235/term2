# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv('netflix_data.csv')

#Creating a subset
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']

netflix_movies = netflix_subset[['title','country','genre','release_year','duration']]

#filter netflix_movies to find movies shorter than 60 minutes
short_movies = netflix_movies[netflix_movies['duration']<60]

freq_table = short_movies.groupby('genre')['title'].count().reset_index()
freq_table = freq_table.sort_values('title',ascending = False)

# assign colours to genres
colors = []
for i in netflix_movies['genre']:
    if i == 'Children':
        colors.append('blue')
    elif i == 'Documentaries':
        colors.append('yellow')
    elif i == 'Stand-Up':
        colors.append('red')
    else:
        colors.append('green')
        
netflix_movies['colors'] = colors

fig = plt.scatter(netflix_movies['release_year'],netflix_movies['duration'],c= netflix_movies['colors'])
plt.title('Movie Duration by Year of Release')
plt.show()

answer = 'maybe'