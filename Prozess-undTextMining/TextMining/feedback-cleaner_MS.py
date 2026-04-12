import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# 1. Vorbereitung (Stelle sicher, dass diese geladen sind) 
# nltk.download('punkt_tab') 
# nltk.download('stopwords') 
# Die Rohdaten 
feedbacks = [ 
   "Die App ist einfach SUPER!!! Aber das Design ist echt hässlich.", 
   "Ich liebe die neue Suchfunktion, sie ist schnell und effizient.", 
   "Schrecklicher Support... ich warte seit Tagen auf eine Antwort!", 
   "Installation war okay, aber die App stürzt ständig ab." 
] 
 
def clean_feedback(text_list): 
   german_stops = set(stopwords.words('german')) 
   cleaned_results = []
   
   for text in text_list: 
       # DEINE AUFGABE HIER: 
       # A) Tokenisiere den Text 
       tokens = word_tokenize(text,language='german')
       # B) Wandle alles in Kleinschreibung um 
       # C) Entferne Stopwörter UND Satzzeichen (nutze .isalnum())
       saubere_tokens = [w.lower() for w in tokens if w.lower() not in german_stops and w.isalnum()]#         
       cleaned_results.append(saubere_tokens)

   return cleaned_results
 
# Teste deine Funktion 
ergebnisse = clean_feedback(feedbacks) 
for i, res in enumerate(ergebnisse): 
   print(f"Feedback {i+1} Schlagworte: {res}")

############################################
### Sentiment Analyse ###
print("######## Sentiment English ########")
from nltk.sentiment import SentimentIntensityAnalyzer

# nltk.download("vader_lexicon")   #einmalige download


sia = SentimentIntensityAnalyzer()  #für Englisch Texte verwendet!!!

for text in feedbacks:
    print("Text:", text)

    score = sia.polarity_scores(text)

    for kategorie, wert in score.items():
        print(f" - {kategorie}: {wert}")
    print("-"*30)

### Sentiment für Deutsche Texte ###
print("######## Sentiment Deutsch ########")
#1.Translate with google translator
#pip install deep_translator
print("----Google translator into English----")
from deep_translator import GoogleTranslator

for text in feedbacks:
    print("Text:", text)
    # translate into Englisch
    text_en = GoogleTranslator(source='auto', target='en').translate(text)
    score = sia.polarity_scores(text_en)
    for kategorie, wert in score.items():
            print(f" - {kategorie}: {wert}")
    print("-"*30)


#2. With transformers
print("----Mithilfe transformers----")
#pip install transformers
#pip install torch

from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="oliverguhr/german-sentiment-bert")

for text in feedbacks:
    print("\nText:", text)
    score = classifier(text)
    print(score)

# ###### 3. With textblob_de ##########
# #pip install textblob-de
# print("----Mithilfe textblob_de----")

# from textblob_de import TextBlobDE as TextBlob

# for text in feedbacks:
#     print("\nText:", text)
#     score = TextBlob(text)
#     print(score.sentiment)

