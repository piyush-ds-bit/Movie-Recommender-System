# 🎬 Movie Recommender System

This is an intelligent **Movie Recommender System** built using **Machine Learning** and **Content-Based Filtering**.  
It suggests movies based on your favorite title by analyzing similarity across features like genres, keywords, cast, and more.

---

## 🎯 Motivation

As an aspiring **Data Scientist**, I built this project to:
- Understand how real-world recommender systems work
- Explore **natural language processing** and **similarity metrics**
- Practice working with structured + text-heavy datasets
- Build something that movie lovers (like me!) can actually use

---

## 🛠️ Technologies & Tools Used

- **Python**
- **Pandas / NumPy** – data manipulation
- **Scikit-learn** – TF-IDF, CountVectorizer, Cosine Similarity
- **NLTK / re** – text cleaning
- **Streamlit** – for building the interactive app
- **TMDB API** – to fetch movie posters and metadata
- **Jupyter Notebook** – for model development
- **GitHub** – for version control and collaboration

---

## 💡 How It Works

1. **Data Collection:**  
   - Dataset: Movies metadata (from TMDB / Kaggle)
   - Features used: Title, Genres, Overview, Cast, Crew

2. **Preprocessing:**  
   - Cleaned and combined text features into a single "tags" column
   - Used `CountVectorizer` to convert text to vectors

3. **Similarity Calculation:**  
   - Applied **Cosine Similarity** on movie vectors
   - For each input movie, we find top N most similar ones

4. **Poster Retrieval:**  
   - Integrated **TMDB API** to fetch movie posters dynamically

5. **Frontend:**  
   - Built with **Streamlit** – clean, fast, interactive

---

## 🎥 Sample Screenshot


---

## 🧪 Challenges I Faced

  - Extracting meaningful features from cast/crew JSON

  - Merging NLP with structured data

  - Optimizing model size for better performance

  - Dynamically showing posters using external APIs

---

## 🧠 Learnings

  - Through this project, I explored:

  - The foundations of recommendation engines

  - Importance of feature engineering

  - Building an end-to-end ML product from data to deployment

---

📬 Contact
Piyush Kumar Singh
🌐 Portfolio Website
📧 piyushjuly04@gmail.com

---

⭐️ If You Like It
If you found this useful or inspiring, feel free to ⭐️ the repo and share it with your friends who love tech and movies!

"Recommending the right movie is an art — powered by data."







