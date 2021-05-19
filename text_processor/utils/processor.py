from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer


def remove_stop_words(data):
    new_data = ""
    for words in data:
        if words not in stopwords:
            new_data += words
    
def remove_punctuation(text):
    text_p = "".join([char for char in text if char not in string.punctuation])

def word_tokenize(text_p):
    words = word_tokenize(text_p)

def word_stemming(filtered_words):
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in filtered_words]
    

def text_preprocessor(data):
    data = remove_stop_words(data)
    data = remove_punctuation(data)
    data = word_stemming(data)
    data = word_tokenize(data)