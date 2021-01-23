# import libraries
import sys
from sqlalchemy import create_engine
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report
# from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier

import pandas as pd
import pickle

from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


def load_data(database_filepath):
    """
    Function to load SQL database.
    :param database_filepath: Filepath of SQL database
    :return: DataFrames X and Y for machine learning model.
    """
    engine = create_engine('sqlite:///{}'.format(database_filepath))

    df = pd.read_sql_query("SELECT * from database_table", engine)
    X = df['message']
    Y = df.drop(['id', 'message', 'original', 'genre'], axis=1)
    category_names = Y.columns

    return X, Y, category_names


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


def build_model():
    """
    A function to build a pipeline with CountVectorizer and TfidfTransfomer and to finally
    select the best parameters for the classifier. In the present case, I have chosen
    MultinomialNB classifier due to performance reasons.
    :return: machine learning model
    """
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(KNeighborsClassifier()))
    ])

    # specify parameters for grid search
    # MultinomailNB parameters = {'clf__estimator__alpha': [1]}

    parameters = {'clf__estimator__leaf_size': [5, 30],
                'clf__estimator__n_neighbors': [2, 5]}

    # create grid search object
    model = GridSearchCV(pipeline, param_grid=parameters)

    return model


def evaluate_model(model, X_test, Y_test, category_names):
    """
    A function to evalute the machine learning model.
    :param model: the machine learning model.
    :param X_test: DataFrame with X_test values
    :param Y_test: DataFrame with y_test values
    :param category_names: Names of the labels
    :return: SKlearn classification report.
    """
    y_pred = model.predict(X_test)
    for i in range(len(category_names)):
        print(category_names[i])
        print(classification_report(Y_test.iloc[i, :], y_pred[i]))
        print('----')

# Alternativ versuchen, category_names mit labels zu versehen.

def save_model(model, model_filepath):
    """
    Function to save model in pickle format.
    :param model: machine learning model before defined.
    :param model_filepath: Filepath of model
    :return: None.
    """
    filename = model_filepath
    pickle.dump(model, open(filename, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
