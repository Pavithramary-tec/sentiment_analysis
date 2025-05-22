from flask import Flask, render_template, request
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
from googleapiclient.discovery import build
import os

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"  # Replace with your actual API key

def get_youtube_comments(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )
    response = request.execute()
    comments = []
    for item in response.get('items', []):
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
    return comments

def analyze_sentiment_and_suggest(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity  # Sentiment polarity

    # Default values (in case none of the conditions are met)
    sentiment_label = "Neutral"
    suggestion = "Thanks for your feedback!"

    if sentiment > 0:
        sentiment_label = "Positive"
        # Suggestions for Positive Comments
        if "love" in text or "great" in text or "amazing" in text:
            suggestion = "We're thrilled you loved it! Your enthusiasm inspires us to keep going!"
        elif "awesome" in text or "fantastic" in text:
            suggestion = "Thank you for your awesome feedback! It means a lot to us!"
        elif "helpful" in text or "informative" in text:
            suggestion = "We’re so happy you found it helpful! We'll keep providing useful content."
        else:
            suggestion = "Thank you for your kind words! We appreciate the positive vibes."
    elif sentiment < 0:
        sentiment_label = "Negative"
        # Suggestions for Negative Comments
        if "hate" in text or "dislike" in text or "worst" in text:
            suggestion = "We’re sorry you didn’t like it! Could you share what you'd like to see improved?"
        elif "boring" in text or "slow" in text:
            suggestion = "Sorry to hear it was boring! Perhaps adding more exciting visuals or a faster pace could help."
        elif "confusing" in text or "hard to understand" in text:
            suggestion = "We apologize if it was confusing. Would breaking things down more clearly help?"
        elif "repetitive" in text or "stale" in text:
            suggestion = "Thanks for the feedback! We’ll try to add more variety to keep things fresh."
        else:
            suggestion = "Thank you for the feedback. We’re working hard to improve!"
    else:
        sentiment_label = "Neutral"
        # Suggestions for Neutral Comments
        if "okay" in text or "fine" in text:
            suggestion = "Thanks for your feedback! Could you tell us what you liked or didn’t like?"
        elif "interesting" in text or "normal" in text:
            suggestion = "Thanks for your comment! Let us know if there’s something specific you’d like to see more of!"
        elif "good" in text or "decent" in text:
            suggestion = "We appreciate your feedback! Let us know how we can improve it further."
        else:
            suggestion = "Thanks for your neutral feedback. We’d love to hear more details on what you think could improve."

    return sentiment_label, suggestion


@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    chart_url = None
    if request.method == 'POST':
        video_ids = request.form['video_ids'].split(',')
        chart_type = request.form['chart_type']
        all_comments = []
        for video_id in video_ids:
            comments = get_youtube_comments(video_id.strip(), API_KEY)
            all_comments.extend(comments)
        sentiments = []
        suggestions = []
        for comment in all_comments:
            sentiment, suggestion = analyze_sentiment_and_suggest(comment)
            sentiments.append(sentiment)
            suggestions.append(suggestion)
        df_sentiments = pd.DataFrame(sentiments, columns=["Sentiment"])
        # Generate and save chart
        plt.figure()
        if chart_type == 'bar':
            sentiment_counts = df_sentiments["Sentiment"].value_counts()
            sentiment_counts.plot(kind='bar', color=['blue', 'green', 'red'])
            plt.title("Sentiment Analysis Bar Chart")
            plt.xlabel("Sentiment")
            plt.ylabel("Count")
            plt.xticks(rotation=0)
        elif chart_type == 'pie':
            sentiment_counts = df_sentiments["Sentiment"].value_counts()
            sentiment_counts.plot(kind='pie', autopct='%1.1f%%', colors=['blue', 'green', 'red'])
            plt.title("Sentiment Analysis Pie Chart")
            plt.ylabel('')
        elif chart_type == 'count':
            sns.countplot(x="Sentiment", data=df_sentiments, palette="viridis")
            plt.title("Sentiment Analysis Count Plot")
            plt.xlabel("Sentiment")
            plt.ylabel("Count")
        else:
            return render_template('index.html', error="Invalid chart type. Please enter 'bar', 'pie', or 'count'.")
        plt.tight_layout()
        if not os.path.exists('static'):
            os.makedirs('static')
        plt.savefig('static/chart.png')
        plt.close()
        chart_url = '/static/chart.png'
        # Prepare results for display
        results = list(zip(all_comments[:90], sentiments[:90], suggestions[:90]))
    return render_template('index.html', results=results, chart_url=chart_url)
if __name__ == '__main__':
    app.run(debug=True)
