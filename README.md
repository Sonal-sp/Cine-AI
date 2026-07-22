# 🎬 CineAI – Intelligent Movie Discovery & Sentiment Hub

CineAI is an AI-powered movie discovery platform that helps users explore films through personalized recommendations, trailer previews, and sentiment analysis of audience reviews. Built using Python and Streamlit, the application combines live movie data from **The Movie Database (TMDB)** with Natural Language Processing (NLP) to deliver a richer movie exploration experience.

Whether you're searching for your next favorite film or analyzing audience opinions, CineAI provides everything in one intuitive interface.

---

## 🌐 Live Demo

**Try it here:**
https://cine-ai-5gtq7kducedualejubnk9i.streamlit.app/

---

## ✨ Features

### 🔍 Smart Movie Search

* Search from thousands of movies using the live TMDB database.
* Instantly retrieve movie information, posters, ratings, and metadata.

### 🎯 Personalized Recommendations

* Receive relevant movie suggestions based on your selected title.
* Powered by TMDB metadata and recommendation endpoints.

### 🧠 AI Sentiment Analysis

* Analyze audience reviews using Natural Language Processing.
* Automatically classify review sentiment as positive, negative, or neutral.
* Built using the TextBlob NLP library.

### 🎥 Trailer Integration

* Watch official movie trailers directly within the application.
* Embedded multimedia experience without leaving the platform.

### ❤️ Persistent Watchlist

* Save movies to your watchlist during your session.
* Session state management ensures your selections remain available without unnecessary page refreshes.

---

## 🛠️ Tech Stack

| Category               | Technologies  |
| ---------------------- | ------------- |
| Language               | Python 3      |
| Framework              | Streamlit     |
| NLP                    | TextBlob      |
| API                    | TMDB REST API |
| HTTP Requests          | Requests      |
| Environment Management | python-dotenv |
| Version Control        | Git & GitHub  |

---

## 🚀 Getting Started

### Clone the Repository

```bash id="vw2m1g"
git clone https://github.com/Sonal-sp/Cine-AI.git
cd Cine-AI
```

---

### Create a Virtual Environment

**Windows**

```bash id="g67l5o"
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**

```bash id="ibib7k"
python3 -m venv .venv
source .venv/bin/activate
```

---

### Install Dependencies

```bash id="9ajxry"
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file in the project root.

```env id="sd5zcd"
TMDB_API_KEY=your_tmdb_api_key
```

---

### Run the Application

```bash id="fq6ppc"
streamlit run app.py
```

The application will launch locally in your browser.

---

## 📊 How It Works

1. Search for any movie.
2. The application fetches live movie details from the TMDB API.
3. Audience reviews are processed using TextBlob to determine overall sentiment.
4. Similar movie recommendations are generated using TMDB's recommendation endpoints.
5. Users can watch trailers and maintain a temporary watchlist during their session.

---

## 🎯 Use Cases

* Discover movies based on similar titles.
* Understand audience opinions through AI-powered sentiment analysis.
* Explore trailers before deciding what to watch.
* Learn how NLP can be integrated into real-world applications.
* Demonstrate API integration and data processing techniques.

---

## 🚧 Future Improvements

Planned enhancements include:

* User authentication
* Permanent cloud-based watchlists
* Genre-based recommendation engine
* Advanced recommendation models using machine learning
* Movie popularity trends and analytics
* Personalized user profiles
* Review summarization using Large Language Models (LLMs)
* Dark mode support

---

## 📖 About the Project

CineAI was built as a portfolio project to demonstrate the integration of AI, Natural Language Processing, and real-time APIs into an interactive web application. The project showcases how modern Python tools can be combined to create an engaging and practical movie discovery platform.

---

## ⚖️ TMDB Attribution

This product uses the **TMDB API** but is **not endorsed or certified by TMDB**.

Movie information, posters, ratings, trailers, and recommendations are provided by **The Movie Database (TMDB)**.

---

## 💬 Feedback

Suggestions, feature requests, and contributions are always welcome. Feel free to open an issue or submit a pull request.

---

