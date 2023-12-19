import streamlit as st
import pickle
import requests

movies = pickle.load(open('movies_list.pk1', 'wb'))
similarity = pickle.load(open("similarity.pk1", 'rb'))
movies_list=movies['title'].values

st.header("Movie Recommeder System")
selectvalue=st.selectbox("Select movie from dropdown", movies_list)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "https://api.themoviedb.org/nj01hspawPof0mJmlgfjuLyJuRN.jpg"+poster_path
    return full_path


def recommand(movie):
    index=movies[movies['title']==movies].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommand_movie=[]
    recommand_poster=[]
    for i in distance[1:6]:
        recommand_movie.append(movies.iloc[i[0]].title)
        recommand_poster.append(fetch_poster(movies_id))
    return recommand_movie ,recommand_poster




if st.button("Show Recommand"):
    movie_name, movie_poster = recommand(selectvalue)
    col1,col2,col3,col4,col5=st.st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1]) 
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2]) 
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4]) 
        st.image(movie_poster[4])