📺 YouTube Comment Sentiment Analysis Web App
📌 Project Overview
This project transforms YouTube video comments into actionable insights using sentiment analysis. Starting from a basic Colab script, it now features a modern Flask web app with a beautiful dark-mode interface. The app fetches comments, analyzes sentiment (positive, neutral, negative), provides tailored suggestions, and visualizes results with charts.

📂 Data Source
Comments are fetched live from YouTube videos via the YouTube Data API v3.

Users can analyze comments from one or more videos by entering their video IDs.

🧹 Text Preprocessing
Lowercasing all text

Removing special characters and punctuation

Sentiment analysis powered by TextBlob

📈 Features & Visualization
Sentiment Detection: Classifies comments as Positive, Negative, or Neutral.

Smart Suggestions: Gives tailored feedback for each sentiment.

Visualization: Users can select Bar, Pie, or Count charts to view sentiment distribution (matplotlib/seaborn).

Modern UI: All elements are centered, with oval input boxes and a sleek, dark-mode design.

🛠️ How to Use
Clone the repository:
Install dependencies:

bash
pip install -r requirements.txt
Get your own YouTube Data API key:

Visit Google Cloud Console.

Create a project, enable the YouTube Data API v3, and generate an API key.

Add your API key:

Open app.py and replace:

python
API_KEY = "YOUR_API_KEY"
with your actual API key.

Run the app:

bash
python app.py
Open http://localhost:5000 in your browser.

Analyze away!

Enter YouTube video IDs (comma separated), select your chart type, and click "Analyze" to see results and charts.

📊 Example Output
Sentiment Table: Shows each comment, its sentiment, and a tailored suggestion.

Charts: Visualizes the overall distribution of sentiments.

🚀 Conclusion
This project demonstrates how to combine real-time data fetching, NLP, and web development for insightful sentiment analysis of YouTube comments—all in a modern, user-friendly app!
Try it out, star the repo, and share your feedback!
