
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
import numpy as np
import re



#AUFGABE 1
#Text normalisieren und zeichenweise numerisch codieren
  

CHAR_MAP = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, ' ': 10,
        'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15,
        'f': 16, 'g': 17, 'h': 18, 'i': 19, 'j': 20,
        'k': 21, 'l': 22, 'm': 23, 'n': 24, 'o': 25,
        'p': 26, 'q': 27, 'r': 28, 's': 29, 't': 30,
        'u': 31, 'v': 32, 'w': 33, 'x': 34, 'y': 35,
        'z': 36, 'ä': 37, 'ö': 38, 'ü': 39, 'ß': 40
    }
EXCLUDE = re.compile('[^0-9 a-zäüöß]+')
BLANKS = re.compile(' +')

def normalize(text):
    # Kleinschreibung
    text = text.lower()
    # Sonderzeichen ersetzen
    text = EXCLUDE.sub(' ', text)
    text = text.strip(' ')
    # Mehrere Leerzeichen durch eins ersetzen
    text = BLANKS.sub(' ', text)
    return text

def process(text):
    text = normalize(text)
    result = [CHAR_MAP[char] for char in text]
    return result
    
def stats(text):
    chars = process(text)
    result = [0 for _ in range(0, 41)]
    for code in chars:
        result[code] += 1
    return result
    
  
text = '''
    "Machine Learning benötigt saubere Daten!"
    '''
x = normalize(text)
print(f"Normalisierter Text:\n{x}")
y = process(text)
print(f"Bearbeiteter Text:\n{y}")
print('Vergleich(len(x) vs len(y)):', len(x), len(y))
z  = stats(text)
print(f"Anzahl der Treffen jeder Zeichnen:\n{z}")
print(f"Zeichen insgesamt: {sum(z)}\n")



#AUFGABE 2
#Bag of Words mit CountVectorizer
print("Aufgabe 2")

texts = ["Machine Learning mit Python",
 "Python wird für Data Science genutzt",
 "Learning Algorithmen benötigen Daten"
]
# Bag of Words erstellen

string_data = np.array(texts)
print("\nString Data:")
print(string_data)
vectorizer = CountVectorizer()
bag_of_words = vectorizer.fit_transform(string_data)
print("\nBag of Words:")
print(bag_of_words)

# Matrix in array umwandeln (Bag of Words Format)
bag_arr = bag_of_words.toarray()
print(f"\nMatrix:\n{bag_arr}")


# Liste der unterschiedlichen Wörter
print("\nBag of Words mit stop words")
print(vectorizer.get_feature_names_out())

# Stopwords für deutschen Text
stop = ["mit", "für", "wird"]
vectorizer2 = CountVectorizer(stop_words = stop)
bag_of_words = vectorizer2.fit_transform(string_data)
print(f"\nMatrix OHNE stop words:\n{bag_of_words.toarray()}")

# Liste der unterschiedlichen Wörter
print("\nBag of Words OHNE stop words")
print(vectorizer2.get_feature_names_out())



#Aufgabe 3 
# #Bigramme erzeugen
# #Zusammenhängende Wortfolgen (N-Gramme) analysieren
print("\nAufgabe 3")

# vectorizer4 = CountVectorizer(stop_words = stop, ngram_range = (3, 3)) # Trigramme
vectorizer4 = CountVectorizer(stop_words = stop, ngram_range = (2, 2)) # Bigramme 
#vectorizer4 = CountVectorizer(stop_words = stop, ngram_range = (4, 4)) # 4-Gramme --> Fehler!!
bigrams = vectorizer4.fit_transform(string_data)
print(bigrams)
print("\nMatrix der Bigramme:")
print(bigrams.toarray())

# print(list(enumerate(vectorizer4.get_feature_names_out())))
print("\nFeature Namen der Bigramme:")
print(vectorizer4.get_feature_names_out())


#Aufgabe 4 
# #Große Texte mit HashingVectorizer komprimieren

texts = ["""
Machine Learning mit Python, Python wird für Data Science genutzt, Learning Algorithmen benötigen Daten
"""]

text_data = np.array(texts)
hv = HashingVectorizer(n_features = 10, stop_words=stop)
features = hv.transform(text_data)
print(f"\nMatrix:\n{features}")
print(f"\nMatrix to array:\n{features.toarray()}")
