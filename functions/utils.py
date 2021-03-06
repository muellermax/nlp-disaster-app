# This module was necessary as after deployment to Heroku the tokenize function could not be found. 
# So train_classifier and run both access this file. 

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

import pickle

def tokenize(text):
    """
    Function to tokenize and lemmatize a given text.
    :param text: String that has to be tokenized and lemmatized.
    :return: List of tokenized words.
    """
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        if tok not in stopwords.words('english'):
            clean_tok = lemmatizer.lemmatize(tok).lower().strip()
            clean_tokens.append(clean_tok)

    return clean_tokens
