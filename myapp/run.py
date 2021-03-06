import json
import sys
import os
import plotly
import pandas as pd
import pickle
from myapp import app

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier

from flask import Flask
from flask import render_template, request
from plotly.graph_objs import Bar
from plotly.graph_objs import Scatter
from sqlalchemy import create_engine

# Necessary to be able to import utils.tokenize from another folder
sys.path.append("..")
from functions.utils import tokenize

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

# load data
engine = create_engine('sqlite:///data/DisasterResponse.db')
df = pd.read_sql_table('database_table', engine)

# load model
model = pickle.load(open("./myapp/classifier.pkl", 'rb'))

# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # First plot: Visualize distribution of message genres.
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)

    # Second plot: Visualize length of messages for each genre.
    df['msg_length'] = df['message'].apply(lambda x: len(x))
    df_grouped = df.groupby('genre').msg_length.mean().reset_index()
    genre_length = df_grouped['msg_length']
    genre_length_names = df_grouped['genre']

    # Third plot: Visualize distribution of topics in messages.
    df_topics = df.drop(['id', 'message', 'original', 'genre', 'msg_length'], axis=1)
    df_topics_sum = df_topics.sum().reset_index()
    df_topics_sum.columns = ['Topic', 'Count']
    df_topics_sum = df_topics_sum.sort_values('Count', ascending=False)

    topics = df_topics_sum.Topic
    topics_count = df_topics_sum.Count

    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    graphs = [
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        },
        {
            'data': [
                Bar(
                    x=genre_length_names,
                    y=genre_length,
                    marker_color=['maroon'] * 3
                )
            ],

            'layout': {
                'title': 'Average length of text messages of different genres',
                'yaxis': {
                    'title': 'Length'
                },
                'xaxis': {
                    'title': 'Genre'
                }
            }
        },
        {
            'data': [
                Scatter(
                    x=topics,
                    y=topics_count,
                    mode='markers',
                    marker_color=['navy'] * 36
                )
            ],

            'layout': {
                'title': 'Topics in disaster messages training set',
                'yaxis': {
                    'title': 'Count'
                },
                'xaxis': {
                    'title': 'Topic'
                }
            }
        }
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
