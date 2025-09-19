import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('data/movie_ratings.csv')



#1 Breakdown of Genres Rated
st.title('Genres Rated')
df["genres"] = df["genres"].str.split('|')
df_explode = df.explode('genres')
st.bar_chart(df_explode['genres'].value_counts().sort_index())