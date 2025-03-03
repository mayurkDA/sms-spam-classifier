SMS Spam Classifier 📩

A simple machine learning model that classifies SMS messages as Spam or Not Spam using TF-IDF vectorization and Naïve Bayes. This project includes an interactive Streamlit web app for real-time classification.

🚀 Features

Machine Learning Model: Trained using TF-IDF and Complement Naïve Bayes.

Web App: Built with Streamlit for easy SMS classification.

Real-time Predictions: Users can enter an SMS to see if it's a scam.

📂 Project Structure

📁 sms-spam-classifier
│── 📁 models              # Contains trained spam model & vectorizer
│── 📁 src                 # Source code (cleaning, preprocessing, predictions)
│── app.py                 # Streamlit web app
│── requirements.txt       # Dependencies
│── README.md              # Documentation
│── LICENSE                # Open-source license

🛠️ Installation & Usage

1. Clone the Repository

git clone https://github.com/yourusername/sms-spam-classifier.git
cd sms-spam-classifier

2. Install Dependencies

pip install -r requirements.txt

3. Run the Streamlit App

streamlit run app.py

4. Usage

Enter your SMS in the text box.

Click the "Check" button.

See if the SMS is Spam or Not Spam.

📊 Model Performance

Accuracy: ~97% on the UCI SMS Spam Dataset.

Algorithms Used: TF-IDF + Complement Naïve Bayes.

📜 License

This project is licensed under the MIT License.
