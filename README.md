# CineAI: Intelligent Movie Discovery & Sentiment Hub 🎬

An advanced, responsive data science web application that provides real-time movie recommendations, live multimedia trailer integration, and automated AI-powered NLP sentiment analysis on audience reviews. Powered by the live global database of The Movie Database (TMDB).

---

## 🚀 Key Features
- **Live Vectorized Search:** Query any film in cinematic history instantly via direct integration with the global TMDB database.
- **Contextual Recommendation Engine:** Leverages structural cloud-calculated metadata endpoints to serve highly relevant recommendations across thousands of titles.
- **AI Sentiment Breakdown:** Utilizes Natural Language Processing (NLP) to calculate semantic polarity and analyze real-time user reviews.
- **Interactive Multimedia Elements:** Embeds dynamic streaming video trailer anchors directly into an expandable user dashboard interface.
- **State-Cached Watchlist:** Implements persistent session-state data arrays allowing real-time watchlist addition without page-refresh memory wipes.

---

## 🛠️ Tech Stack & Architecture
- **Language:** Python 3.10+
- **Framework:** Streamlit (Dynamic Web Frontend Container)
- **AI/NLP Engine:** TextBlob (Linguistic Polarity Scoring)
- **API Integration:** TMDB REST API v3 Hooks (Requests)
- **Environment Management:** Python-Dotenv / Os (Secure Credential Masking)

---

## ⚙️ Installation & Local Setup

Follow these precise steps to get a local instance of the application compiled and running safely inside an isolated virtual sandbox.

### 1. Clone the Repository

git clone [https://github.com/Sonal-sp/Cine-AI.git] (https://github.com/Sonal-sp/Cine-AI.git)
cd ai-movie-recommender

### 2. Configure the Virtual Environment (venv)
Create and isolate your python execution environment dependencies.

# Create sandbox
python -m venv .venv

# Activate environment (Windows)
.venv\Scripts\activate

# Activate environment (macOS/Linux)
source .venv/bin/activate

### 3. Install Package Dependencies
With your environment active, execute a bulk extraction install from the verified requirements directory:

pip install -r requirements.txt

### 4. Inject Environment Credentials (.env)
Create a file named exactly .env in the root folder directory and input your personal developer authorization key:

Code snippet
TMDB_API_KEY=your_alphanumeric_api_key_here

### 5. Boot Up the Application

streamlit run app.py

# ⚖️ TMDB Data Attribution & Compliance
This application relies entirely on data pipelines provided by the live servers of The Movie Database (TMDB).

### Compliance Statement:
This product uses the TMDB API but is not endorsed or certified by TMDB.

For more information on the dataset rules or to register for your own unique credential tracking keys, explore The Movie Database API Documentation.

### 👨‍💻 Author
Developed as an engineering portfolio project. Feel free to connect or drop feedback!