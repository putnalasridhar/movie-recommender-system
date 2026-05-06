import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open('similarity.pkl','rb') as f:
    similarity = pickle.load(f)

df = pd.read_csv('tmdbdf.csv')
df = df.head(5000)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000; /* solid black background */
    }
    .movie-title {
        text-align: center;
        font-weight: bold;
        font-size: 18px;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #E50914; /* Netflix red */
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #f40612;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image('image.jpg ',use_container_width=False)


st.markdown("<h1 style='text-align:center; color:white;'>Netflix Movie Recommendation</h1>", unsafe_allow_html=True)


movie = st.selectbox('Select the Movie to Watch', df['title'].values)

base_url = 'https://image.tmdb.org/t/p/w500/'


def recommend(movie):
    idx = df[df['title'] == movie].index[0]
    movie_list = np.argsort(similarity[idx])[::-1][1:6]

    recommend_movie = []
    recommend_poster = []
    for mov in movie_list:
        poster = df.iloc[mov]['poster_path']
        recommend_movie.append(df.iloc[mov].title)
        recommend_poster.append(base_url + poster)
    return recommend_poster, recommend_movie


if st.button('Click here for Getting Similar Movies'):
    poster, name = recommend(movie)

    cols = st.columns([1,1,1,1,1])

    for idx, col in enumerate(cols):
        with col:
            st.image(poster[idx], width=250)
            st.markdown(f"<p class='movie-title'>{name[idx]}</p>", unsafe_allow_html=True)
