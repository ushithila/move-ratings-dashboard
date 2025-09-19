import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('data/movie_ratings.csv')


print(df.head())


#1. 
st.bar_chart(df['genres'].value_counts().sort_index())