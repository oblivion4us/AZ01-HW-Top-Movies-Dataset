import pandas as pd

df = pd.read_csv("top_rated_9000_movies_on_TMDB.csv")

print(df.head())
print(df.info())
print(df.describe())