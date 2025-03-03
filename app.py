import streamlit as st
import joblib
import nltk
from nltk.corpus import stopwords
import string
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the saved model and vectorizer
model = joblib.load(os.path.join(script_dir, 'spam_model.pkl'))
vectorizer = joblib.load(os.path.join(script_dir, 'tfidf_vectorizer.pkl'))

# Download stopwords from NLTK (only needs to run once)
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Function to clean text (same as in training)
def clean_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# Streamlit app interface
st.title("SMS Scam Checker")
st.write("Type an SMS below to see if it’s fishy!")

# Text input from user
sms_input = st.text_area("Enter your SMS here")

# Button to check the SMS
if st.button("Check"):
    if sms_input:
        # Clean the input text
        cleaned_sms = clean_text(sms_input)
        # Transform it into TF-IDF features
        sms_vector = vectorizer.transform([cleaned_sms])
        # Predict using the model
        prediction = model.predict(sms_vector)[0]
        # Display result
        result = "Scam" if prediction == 1 else "Likely Not a Scam"
        st.write(f"Result: **{result}**")
    else:
        st.write("Please enter an SMS!")