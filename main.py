import pandas as pd

df = pd.read_csv("top_rated_9000_movies_on_TMDB.csv")

print(df.head())
print(df.info())
print(df.describe())

df_dz = pd.read_csv("dz.csv")
print(f"{df_dz}\n")

df_dz.fillna(value=0, inplace=True)
print(f"{df_dz}\n")

group = df_dz.groupby('City')['Salary'].mean()
print(group)