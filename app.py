import streamlit as st
import requests
import os
from dotenv import load_dotenv
from textblob import TextBlob

# --- 1. CONFIGURATION & SECRETS ---
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY") # Looks for your key in the .env file
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"

st.set_page_config(page_title="CineAI Dashboard", page_icon="🎬", layout="wide")
st.title("🎬 CineAI: Intelligent Movie Hub")
st.write("An advanced engine offering live recommendations, real-time multimedia embeds, and AI-powered text analysis.")

# Fallback check if .env isn't loaded correctly
if not API_KEY or API_KEY == "YOUR_TMDB_API_KEY_HERE":
    st.error("Missing TMDB_API_KEY! Ensure it is set up correctly in your local .env file.")
    st.stop()

# Initialize Persistent Session Watchlist
if "watchlist" not in st.session_state:
    st.session_state.watchlist = []


# --- 2. ADVANCED API FETCHERS ---
@st.cache_data
def fetch_genres():
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    return {genre['name']: genre['id'] for genre in requests.get(url).json().get('genres', [])}

def search_movies_by_genre(genre_id):
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&sort_by=popularity.desc&language=en-US"
    return requests.get(url).json().get('results', [])

def search_movie_by_title(title):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={title}&language=en-US"
    return requests.get(url).json().get('results', [])

def get_live_recommendations(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}/recommendations?api_key={API_KEY}&language=en-US"
    return requests.get(url).json().get('results', [])

def get_movie_trailer(movie_id):
    """Fetches the official YouTube trailer key for a movie."""
    url = f"{BASE_URL}/movie/{movie_id}/videos?api_key={API_KEY}&language=en-US"
    video_results = requests.get(url).json().get('results', [])
    for video in video_results:
        if video['type'] == 'Trailer' and video['site'] == 'YouTube':
            return video['key']
    return None

def get_movie_reviews(movie_id):
    """Fetches text reviews written by audiences for NLP evaluation."""
    url = f"{BASE_URL}/movie/{movie_id}/reviews?api_key={API_KEY}&language=en-US"
    return requests.get(url).json().get('results', [])


# --- 3. UI FILTERS & SIDEBAR ---
genres_dict = fetch_genres()
st.sidebar.header("🎯 Discovery Setup")
selected_genre = st.sidebar.selectbox("Filter Starter Options By Genre:", ["Trending/Popular"] + list(genres_dict.keys()))

if selected_genre != "Trending/Popular":
    movie_list_raw = search_movies_by_genre(genres_dict[selected_genre])
else:
    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US"
    movie_list_raw = requests.get(url).json().get('results', [])

movie_titles = [movie['title'] for movie in movie_list_raw]


# --- 4. DATA MATCHING SELECTION ---
col1, col2 = st.columns([2, 1])
with col1:
    selected_movie_title = st.selectbox("Select from list:", movie_titles)
with col2:
    custom_search = st.text_input("Or query any movie globally:")

target_movie_id = None
display_title = ""

if custom_search:
    search_results = search_movie_by_title(custom_search)
    if search_results:
        target_movie_id = search_results[0]['id']
        display_title = search_results[0]['title']
    else:
        st.warning("Movie not identified. Double-check your spelling!")
elif selected_movie_title:
    for m in movie_list_raw:
        if m['title'] == selected_movie_title:
            target_movie_id = m['id']
            display_title = m['title']


# --- 5. TABBED DASHBOARD EXPERIENCE ---
if target_movie_id:
    st.markdown("---")
    
    # Structural separation using tabs
    tab1, tab2, tab3 = st.tabs(["🎯 Smart Recommendations", "📊 AI Sentiment Review", "💾 My Watchlist"])
    
    # --- TAB 1: RECOMMENDATIONS & VIDEOS ---
    with tab1:
        st.subheader(f"Recommended Movies matching: **{display_title}**")
        recommendations = get_live_recommendations(target_movie_id)
        
        if recommendations:
            top_5 = recommendations[:5]
            cols = st.columns(5)
            
            for index, movie in enumerate(top_5):
                m_id = movie['id']
                m_title = movie['title']
                
                with cols[index]:
                    if movie.get('poster_path'):
                        st.image(IMAGE_URL + movie['poster_path'], use_container_width=True)
                    else:
                        st.image("https://via.placeholder.com/500x750?text=No+Poster", use_container_width=True)
                    
                    st.markdown(f"#### {m_title}")
                    st.caption(f"⭐ Rating: {movie.get('vote_average', 0)}/10")
                    
                    # Collapsible section to keep layout neat and show text context cleanly
                    with st.expander("Details & Action"):
                        st.write(movie.get('overview', 'No overview provided.')[:100] + "...")
                        
                        # Dynamic YouTube Trailer Embed Button
                        trailer_key = get_movie_trailer(m_id)
                        if trailer_key:
                            st.link_button("📺 Watch Trailer", f"https://www.youtube.com/watch?v={trailer_key}")
                        else:
                            st.caption("No trailer available")
                        
                        # Interactive Watchlist Button
                        if st.button("➕ Watchlist", key=f"wl_{m_id}"):
                            if m_title not in st.session_state.watchlist:
                                st.session_state.watchlist.append(m_title)
                                st.toast(f"Added {m_title} to watchlist!")
        else:
            st.info("No explicit matches discovered for this title context.")

    # --- TAB 2: NATURAL LANGUAGE PROCESSING ENGINE ---
    with tab2:
        st.subheader(f"AI Sentiment Breakdown for: **{display_title}**")
        reviews = get_movie_reviews(target_movie_id)
        
        if reviews:
            total_polarity = 0
            positive_count = 0
            negative_count = 0
            neutral_count = 0
            
            cleaned_reviews_data = []
            
            # Analyze each user block mathematically
            for r in reviews:
                text_content = r.get('content', '')
                author = r.get('author', 'Anonymous')
                
                # Apply TextBlob sentiment metrics
                blob = TextBlob(text_content)
                polarity = blob.sentiment.polarity  # Range: -1.0 (negative) to +1.0 (positive)
                
                total_polarity += polarity
                
                if polarity > 0.1:
                    status = "Positive 🟢"
                    positive_count += 1
                elif polarity < -0.1:
                    status = "Negative 🔴"
                    negative_count += 1
                else:
                    status = "Neutral 🟡"
                    neutral_count += 1
                
                cleaned_reviews_data.append({"author": author, "content": text_content, "status": status, "polarity": round(polarity, 2)})
            
            # Summary Metrics Display
            avg_polarity = total_polarity / len(reviews)
            
            if avg_polarity > 0.1:
                verdict = "Highly Recommended / Positive Audience Consensus"
            elif avg_polarity < -0.1:
                verdict = "Mixed or Critically Panned Audience Consensus"
            else:
                verdict = "Generally Neutral / Division of Opinion"
                
            m_col1, m_col2, m_col3 = st.columns(3)
            m_col1.metric("Total Reviews Evaluated", len(reviews))
            m_col2.metric("Average Sentiment Velocity Score", f"{round(avg_polarity, 2)}")
            m_col3.metric("AI General Summary Verdict", "Positive 👍" if avg_polarity > 0.1 else "Mixed 👥")
            
            st.info(f"🧠 **AI Core Insights Analytical Verdict:** {verdict}")
            st.markdown("---")
            
            # Display Raw Text Snippets With Calculated Labels
            st.write("#### Detailed Audience Sentiment Breakdown Ledger:")
            for index, item in enumerate(cleaned_reviews_data[:3]): # Show top 3 samples safely
                st.markdown(f"**Critic/User:** {item['author']} | **Sentiment Label:** {item['status']} *(Polarity: {item['polarity']})*")
                st.write(f"\"{item['content'][:250]}...\"")
                st.markdown("---")
        else:
            st.warning("Insufficient community review data available on live servers to generate custom AI metrics.")

    # --- TAB 3: WATCHLIST DASHBOARD CONTAINER ---
    with tab3:
        st.subheader("Your Custom Saved Watchlist Collection")
        if st.session_state.watchlist:
            for item in st.session_state.watchlist:
                st.markdown(f"🍿 **{item}**")
            if st.button("🧹 Clear Watchlist Grid"):
                st.session_state.watchlist = []
                st.rerun()
        else:
            st.write("Your watchlist registry is currently empty. Click '➕ Watchlist' under details to populate titles!")