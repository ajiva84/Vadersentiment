import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create an instance of the Vader sentiment analyzer
sia = SentimentIntensityAnalyzer()



# Define the Streamlit app

st.title("Sentiment Analysis with Vader")
    
# Allow the user to input text
text = st.text_area("Enter some text to analyze")
    
# If the user has entered text, analyze it with Vader
if text:
# Get the sentiment scores for the text
    scores = sia.polarity_scores(text)
        
# Display the sentiment scores to the user
    st.subheader("Sentiment Scores")
    st.write("Positive:", scores["pos"])
    st.write("Neutral:", scores["neu"])
    st.write("Negative:", scores["neg"])
    st.write("Compound:", scores["compound"])
