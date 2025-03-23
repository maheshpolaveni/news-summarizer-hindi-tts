from utils import summarize_text, analyze_sentiment, extract_topics

def generate_report(company_name):
    # Example news sources — these URLs get summarized
    urls = [
        f"https://www.moneycontrol.com/news/business/{company_name}-news-1.html",
        f"https://economictimes.indiatimes.com/topic/{company_name}"
    ]

    articles = []
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for url in urls:
        summary = summarize_text(url)
        sentiment = analyze_sentiment(summary)
        topics = extract_topics(summary)

        sentiment_counts[sentiment] += 1

        articles.append({
            "Title": f"News about {company_name}",
            "Summary": summary,
            "Sentiment": sentiment,
            "Topics": topics
        })

    # Final sentiment decision
    if sentiment_counts["Positive"] > sentiment_counts["Negative"]:
        final_sentiment = "Overall sentiment is mostly Positive"
    elif sentiment_counts["Negative"] > sentiment_counts["Positive"]:
        final_sentiment = "Overall sentiment is mostly Negative"
    else:
        final_sentiment = "Overall sentiment is Neutral"

    report = {
        "Company": company_name,
        "Articles": articles,
        "Comparative Sentiment Score": {
            "Sentiment Distribution": sentiment_counts,
            "Coverage Insight": f"Out of {len(articles)} articles: {sentiment_counts}"
        },
        "Final Sentiment Analysis": final_sentiment
    }

    return report
