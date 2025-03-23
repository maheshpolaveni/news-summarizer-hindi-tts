import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gtts import gTTS  # ✅ Using gTTS for Hindi TTS

# Scrape and extract text from a news article
def summarize_text(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([para.get_text() for para in paragraphs])
        return text[:1000] if text else "No content found."
    except:
        return "Failed to fetch content."

# Perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

# Extract basic topics (top 5 words)
def extract_topics(text):
    words = text.split()
    return list(set(words[:5]))

# ✅ Generate Hindi audio using gTTS
def generate_hindi_tts(text, output_path="output.mp3"):
    # gTTS will translate the English summary into Hindi speech
    tts = gTTS(text=text, lang='hi')
    tts.save(output_path)
    return output_path
