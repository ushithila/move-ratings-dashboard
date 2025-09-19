import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('data/movie_ratings.csv')



#1 Breakdown of Genres Rated
st.title('Genres Rated')
df["genres"] = df["genres"].str.split('|')
df_explode = df.explode('genres')
st.bar_chart(df_explode['genres'].value_counts().sort_values(ascending=True))

#2 Genres with the Highest Ratings 
st.title('Genres with the Highest Ratings')
genre_rating = df_explode.groupby('genres')['rating'].mean().reset_index().sort_values("rating", ascending=False)
st.bar_chart(genre_rating.set_index('genres'))