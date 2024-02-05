# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 21:46:35 2024

@author: megan
"""

# Assignment 1 

import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("C:/Users/megan/css assignment/movie_dataset.csv", index_col=0)

print(df)
print(df.describe())
print(df.info())

df.columns = df.columns.str.replace('Runtime (Minutes)', 'Runtime(Minutes)')
df.columns = df.columns.str.replace('Revenue (Millions)', 'Revenue(Millions)')
df.columns

pd.set_option('display.max_rows', None)
print(df)

x = df["Revenue(Millions)"].mean()
df["Revenue(Millions)"].fillna(x, inplace = True)

y = df["Metascore"].mean()
df["Metascore"].fillna(y, inplace = True)

df.to_csv("C:/Users/megan/css assignment/Output/movie_dataset_cleaned.csv")

df = pd.read_csv("C:/Users/megan/css assignment/Output/movie_dataset_cleaned.csv", index_col=0)

# Question 1 - highest rated movie = The Dark Knight

print(df['Rating'].max())

df[(df['Rating'] == 9.0)]

# Question 2 - average revenue of all movies - 82.95 Mil

print(df['Revenue(Millions)'].mean())

# Question 3 - average revenue from 2015 to 2017 - 68.06 Mil

df[(df['Year'] >= 2015) & (df['Year'] <= 2017)][['Revenue(Millions)']].mean()

# Question 4 - number of movies released in 2016 - 297

movies_2016 = df[df['Year'] == 2016].shape[0]
print("The number of movies release in 2016 is:", movies_2016)

# Question 5 - number of movies directed by Christopher Nolan - 5

C_Nolan_movies = df[df['Director'] == 'Christopher Nolan'].shape[0]
print("The number of movies directed by Christopher Nolan is:", C_Nolan_movies)

# Question 6 - number of movies with rating >= 8.0 = 78

rating_greater_than_8 = df[(df['Rating'] >= 8)].shape[0]
print("The number of movies with a rating of 8 and higher is:", rating_greater_than_8)

# Question 7 - median rating of Christopher Nolan movies -8.6

median_rating_C_Nolan = df[(df['Director'] == "Christopher Nolan")][['Rating']].median()
print("The median rating of Christopher Nolan movies is:", median_rating_C_Nolan)

# Question 8 - year with highest average rating = 2006

year_with_highest_average_rating = df.groupby('Year')[['Rating']].mean()
print(year_with_highest_average_rating)

# Question 9 - % increase in number of movies between 2006 and 2016 - 575
titles_2006 = df[df['Year'] == 2006].shape[0]
titles_2016 = df[df['Year'] == 2016].shape[0]

percent_increase_2006_2016 = ((titles_2016 - titles_2006)/titles_2006)*100
print("The percent increase in movies from 2006 to 2016 is:", percent_increase_2006_2016)

# Question 10 - most common actor - Mark Wahlberg

actors = [actor.strip() for actors_list in df['Actors'].str.split(',') for actor in actors_list]
number_of_actors = Counter(actors)
most_common_actor = number_of_actors.most_common(1)[0][0]
print("The most common actor is:", most_common_actor)

# Question 11 - number of unique genres - 20

unique_genres_set = set()
for genres_cell in df['Genre']: unique_genres_set.update(genre.strip() for genre in genres_cell.split(','))
number_of_unique_genres = len(unique_genres_set)

print("The number of unique genres is:", number_of_unique_genres)

# Question 12 - correlation of numerical features + how to produce better movies

variables = ['Year', 'Runtime(Minutes)', 'Rating', 'Votes', 'Revenue(Millions)', 'Metascore']
sns.pairplot(df[variables])
plt.show()

import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("C:/Users/megan/css assignment/Output/movie_dataset_cleaned.csv", index_col=0)
profile = ProfileReport(df, title = "Profiling Report")
profile.to_file("your_report.html")
