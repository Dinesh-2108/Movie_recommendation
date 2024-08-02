import streamlit as st
import pandas as pd
import ast

# Load CSV file
csv_file = 'movies.csv'  # replace with your CSV file path
df = pd.read_csv("mdb.csv")

# Title of the web app
st.title('Keywords & Overview')

# Collect all unique genres
unique_genres = set()
for index, row in df.iterrows():
    if isinstance(row['genres'], str):  # Check if the value is a string
        genres = row['genres'].split(',')
        for genre in genres:
            unique_genres.add(genre.strip())
with st.container(border =True):
    st.subheader("Genres")
    st.write(list(unique_genres))
# Display the data as a glossary
for index, row in df.iterrows():
    with st.expander(row['title']):# Movie Title
        st.write(f"{row['keywords']}")
        st.divider()
        st.write(f"{row['overview']}")




