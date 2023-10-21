import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

x = "It is a charming and beautiful product"
y = "It was a horrible experience!"
z = "I have nothing to say. Normal so far"

resultados = sia.polarity_scores(z)
print(resultados)