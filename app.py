import pickle
import pandas as pd
import streamlit as st
import requests
import base64



st.set_page_config(page_title="Movie Recommender System", layout="centered")

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

image_path = "assets/1c30e736-8f80-4ec1-aecf-107fde4e5aad.jpg"
image_base64 = get_base64(image_path)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{image_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

import streamlit as st



@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=925b497d9d5a08e9d4ab47e061ab579c&language=en-US"


    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except Exception as e:
        print("Error fetching poster:", e)
        return "https://via.placeholder.com/500x750?text=Error"



# Add 'poster_url' column once, save it to a new pickle
# movies['poster_url'] = movies['movie_id'].apply(fetch_poster)
# movies.to_pickle("movies_with_posters.pkl")


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies_dict = pickle.load(open('assets/movies_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list)

if st.button('Show Recommendation'):
    with st.spinner("Fetching recommendations..."):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])

                # View Details button (optional logic)
                st.button('View Details', key=f'details_{i}')


st.markdown(
    """
    <style>
    .made-in-bharat {
        position: fixed;
        left: 10px;
        bottom: 10px;
        font-size: 14px;
        color: #888888;
        z-index: 9999;
    }
    </style>
    <div class="made-in-bharat">Made in Bharat 🇮🇳</div>
    """,
    unsafe_allow_html=True
)
