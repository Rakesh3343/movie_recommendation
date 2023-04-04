import streamlit as st
import pandas as pd
import numpy as np
import pickle as pk
df_dict=pk.load(open('frame_dict_pickle.pkl','rb'))
similarity=pk.load(open('similarity.pkl','rb'))
df=pd.DataFrame(df_dict)      
movies_list=df['title'].values
st.title("I can Recommend similar movies")
selected_movie=st.selectbox('choose the movie',movies_list)
def recommend_movie(movie_name):
    ind=df[df['title']==movie_name].index
    movie_ind=np.argsort(similarity[ind])[0][-1:-16:-1]
    for i in movie_ind:
        st.write(df['title'].iloc[i])
if st.button('Recommend similar movies'):
    recommend_movie(selected_movie)

