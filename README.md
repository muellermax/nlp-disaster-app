# Disaster Response Pipeline Project

A Natural Language Processing (NLP) project to classify the context of messages that were sent during disasters. 

### Installation
For installation clone this repository and to read two CSV-files navigate to the data folder and run process_data.py:
````python
cd data
python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db
````
Where disaster_messages and disaster_categories and the features and labels for the machine learning model. DisasterResponse
is the DataBase where the table will be stored. 

After preparing the data, navigate to models and run train_classifier.py: 

````python
cd models
python train_classifier.py ../data/DisasterResponse.db classifier.pkl
````
Where ../data/DisasterResponse.db ist the path of your database and classifier.pkl the name for the pickle-file. 


To run the app navigate to myapp and python run.py. 
```python
cd myapp
python run.py
```

You should see the app on http://127.0.0.1:3002. 

Please note that I have not uploaded the last version of my classifier, as the pickle-file grew quite big. 

Packages in use: json plotly pandas pickle nltk flask sqlalchemy sys scikit-learn


### Project motivation
NLP is an exciting field and I am planing to implement it in my other projects (especially those about movies). 
This project is part of my Udacity Data Science course. 


### File descriptions
* app: Folder that contains the necessary files for deployment:
    * run.py: Python script that starts the app and loads the ML-model as well as the plotly visualizations. 
    * templates => master.html: The "index"-page of this dashboard. 
    * templates => go.html: Shows the classification of the given text message. 
* data: Folder that includes the data (stored in CSV and a database) and the python file that prepares the data. 
    * process_data.py: Python script that includes an ETL pipeline to extract, transform and load the data in a database. 
    * Two CSV-files: Containing disaster messages and their categories. 
    * Database-files: SQL database
* models: Folder that includes train_classifier.py to train a classifier as well as the ready pkl-file. 


### Data
The data was proviced by [Figure Eight](https://appen.com/). 


### How to interact
Every contribution is welcome. I think there are many possibilities to improve the performance of the ML-model. 
I am currently working with KNeighbors, which performs slightly better that MultinomialNB and without extended GridSearch. As you can see on the information about the
training set, some categories (like aid_related or weather_related) do appear more often than other categories (like 
hospitals or fire). The precision of the classifier could be improved by taking away the "over-represented" categories
or other data engineering. 


### Acknowledgments
Thanks to Figure Eight for providing the data for us students. Also thanks to the Udacity team for all the 
instructions. 


### Author
Maximilian Müller, Business Development Manager in the Renewable Energy sector. Now diving into the field of data analysis. 


### GitHub repository
Link to GitHub respository: https://github.com/muellermax/Disaster-Response


### License
Copyright 2020 Maximilian Müller

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the 
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit 
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

From opensource.org

