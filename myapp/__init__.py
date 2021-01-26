from flask import Flask

app = Flask(__name__)

from myapp import run

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
