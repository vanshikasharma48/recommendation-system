import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# dataset
data = {
    "Movie": [
        "Inception", "Interstellar", "The Dark Knight",
        "Titanic", "The Notebook", "La La Land",
        "Avengers", "Iron Man", "Thor",
        "Frozen", "Moana", "Coco"
    ],
    
    "Genre": [
        "Sci-Fi", "Sci-Fi", "Action",
        "Romance", "Romance", "Romance",
        "Action", "Action", "Action",
        "Animation", "Animation", "Animation"
    ]
}

df = pd.DataFrame(data)

# vectorization
cv = CountVectorizer()
matrix = cv.fit_transform(df["Genre"])

# similarity
similarity = cosine_similarity(matrix)

# recommendation function
def recommend(movie):
    idx = df[df["Movie"] == movie].index[0]
    distances = similarity[idx]
    
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:4]
    
    return [df.iloc[i[0]].Movie for i in movies_list]

# UI
st.title("🎬 Movie Recommendation System")

movie_name = st.selectbox("Select a Movie", df["Movie"].values)

if st.button("Recommend"):
    recommendations = recommend(movie_name)
    
    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write("👉", movie)