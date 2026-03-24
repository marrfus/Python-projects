import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.probability import FreqDist
# Nur einmal!!
# nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")

text = "Text Mining ist Cool. mit Python und NLTK macht es spaß!"

# In Sätze zerlegen
saetze = sent_tokenize(text,language="german")

print("Sätze:", saetze)

# In Wörter zerlegen
woerter = word_tokenize(text, language="german")
print("Wörte:", woerter)

# Deutsch Stopwörte laden
stop_words = set(stopwords.words("german"))

# Filtern
gefilterte_woerter = [w for w in woerter if w.lower() not in stop_words and w.isalnum()]

print("Ohne Stopwörter und Satzzeichen:", gefilterte_woerter)

# Stemming
stemmer = SnowballStemmer("german")

gestemmte_woerter = [stemmer.stem(w) for w in gefilterte_woerter]

print("Wortstämme:",gestemmte_woerter)

#Häufigkeitsanalyse

beispiel_text = "Python ist toll. Text Mining mit Python hilft bei der Analyse von Text."

tokens = word_tokenize(beispiel_text, language="german")

# Bereinigung
saubere_tokens = [w.lower() for w in tokens if w.lower() not in stop_words and w.isalnum()]

# Häufigkeit berechnen
fdist = FreqDist(saubere_tokens)

print("Die 3 häufigsten Wörter:", fdist.most_common(3))

##############

from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

texte = [
    "I absolutly love this product, it is amazing.",
    "This is the worst experience I have ever had. Terrible!",
    "The book is okay. Nothing special, but not bad.",
    "I am VERY HAPPY with the results!"
]

for text in texte:
    print("Text:", text)

    score = sia.polarity_scores(text)

    for kategorie, wert in score.items():
        print(f" - {kategorie}: {wert}")
    print("-"*30)