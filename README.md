YouTube Comment Sentiment Analysis Web App
This project is a modern, dark-themed Flask web application for analyzing the sentiment of YouTube video comments. It started as a simple Colab script and was transformed into a full-featured, user-friendly web app with a beautiful interface.

🚀 Project Overview
Fetches comments from YouTube videos using the YouTube Data API v3.

Analyzes sentiment (positive, neutral, negative) for each comment using TextBlob.

Provides tailored suggestions for each comment based on its sentiment.

Visualizes sentiment distribution with interactive bar, pie, or count charts (matplotlib/seaborn).

Features a modern, dark-mode web interface built with Flask, HTML, and custom CSS.

🌟 Key Features
Multiple video support: Analyze comments from one or more YouTube videos at once.

Custom chart selection: Choose between bar, pie, or count plots for sentiment visualization.

Smart feedback: Each comment receives a sentiment label and a personalized suggestion.

Responsive design: All elements are centered, with oval input boxes and a sleek, modern look.

🛠️ How to Use
Clone the repository:

bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
Install dependencies:

bash
pip install -r requirements.txt
Get your own YouTube Data API key:

Create a project and API key at Google Cloud Console.

Enable the YouTube Data API v3.

Add your API key:

Open app.py and replace:

python
API_KEY = "YOUR_API_KEY"
with your actual API key.

Run the app:

bash
python app.py
Open http://localhost:5000 in your browser.

Use the web interface:

Enter YouTube video IDs (comma separated).

Choose your preferred chart type.

Click "Analyze" to view results and charts.

