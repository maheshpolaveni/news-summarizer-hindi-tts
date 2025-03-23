import streamlit as st
import api
from utils import generate_hindi_tts
from googletrans import Translator

st.title("📢 News Summarization and Hindi TTS App")
company_name = st.text_input("Enter the Company Name:", "Reliance")

if st.button("Generate Report"):
    report = api.generate_report(company_name)

    st.success("✅ Report Generated!")
    st.json(report)

    # Prepare English summary text
    summary_text = f"Company name {report['Company']}. "
    for article in report["Articles"]:
        summary_text += f"Title: {article['Title']}. Summary: {article['Summary']}. Sentiment: {article['Sentiment']}. "
    summary_text += f"Final sentiment analysis: {report['Final Sentiment Analysis']}."

    # Translate the summary to Hindi before TTS
    translator = Translator()
    translation = translator.translate(summary_text, src='en', dest='hi')
    translated_summary=translation.text

    # Generate Hindi TTS (audio will be in Hindi)
    audio_path = generate_hindi_tts(translated_summary)

    st.audio(audio_path)
