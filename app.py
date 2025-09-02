import pickle
import streamlit as st
import requests


import gdown
import pickle
from pathlib import Path

# List of files to download (Google Drive File IDs and local paths)
FILES = {
    "similarity.pkl": "1iAfmm-z_tQN37mcypuVkjsALLhlA8sn4",
    "other_model.pkl": "1IdogJcB15vx4eqoYLLt-WT2zH28OZqVz"
}

ARTIFACTS_DIR = Path("artifacts")
ARTIFACTS_DIR.mkdir(exist_ok=True)

@st.cache_resource
def load_files():
    loaded = {}
    for filename, file_id in FILES.items():
        dest = ARTIFACTS_DIR / filename
        url = f"https://drive.google.com/uc?export=download&id={file_id}"
        if not dest.exists():
            st.write(f"📥 Downloading {filename}...")
            gdown.download(url, str(dest), quiet=False)
        with open(dest, "rb") as f:
            loaded[filename] = pickle.load(f)
    return loaded

models = load_files()

# Use the models
similarity = models["similarity.pkl"]
other_model = models["other_model.pkl"]

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
        
def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    
    return recommended_movies_name, recommended_movies_poster

    
        
st.write("✅ All files loaded successfully!")
st.header("Movies recommendation system using machine learning")
movies = pickle.load(open('artificats/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artificats/similarity.pkl', 'rb'))
movie_list = movies['title'].values
selected_movie = st.selectbox(
    'tap or select movie to get recommendation',
    movie_list
)

if st.button('Show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])
    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])
    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])
    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])        
    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])    