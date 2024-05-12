import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']
    

def recommend(movie):
    movie_index =movies[movies['title']== movie].index[0]
    distance =similarity[movie_index]
    movies_list =sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movie=[]
    recommended_movie_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie,recommended_movie_poster
movies_dict = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies =pd.DataFrame(movies_dict)
st.title("Movie Recommeded System")
selected_movie_name = st.selectbox(
    "Enter Movie Name?",movies['title'].values)

#st.button("Recommeded", type="primary")
if st.button('Recommend'):
   name ,poster =recommend(selected_movie_name)
   col1, col2, col3, col4, col5 = st.columns(5)
   with col1:
        st.text(name[0])
        st.image(poster[0])
   with col2:
        st.text(name[1])
        st.image(poster[1])
   with col3:
        st.text(name[2])
        st.image(poster[2])
   with col4:
        st.text(name[3])
        st.image(poster[3])
   with col5:
        st.text(name[4])
        st.image(poster[4])