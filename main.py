import streamlit as st
import pickle
import pandas as pd
movie_dict=pickle.load(open('movie_name.pkl', 'rb'))
movies=pd.DataFrame(movie_dict)
st.title('Movie Recoomender System')
selected_movie=st.selectbox(
    'hi hello',
    movies['title'].values
)

if st.button('Recommend'):
    Recommend(selected_movie)
    st.write(selected_movie)