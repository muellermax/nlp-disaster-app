# Disaster Response Pipeline Project: webapp

## Index

1. [About the project](#about)
2. [Data](#data)
3. [File descriptions](#file-description)
4. [How to interact](#interact)
5. [Acknowledgements](#thx)
6. [Author](#author)
7. [License](#license)


## <a class="anchor" id = "about">About the project</a>
A Natural Language Processing (NLP) project to classify the context of messages that were sent during disasters. This project was part of my Udacity Data Scientist Nanodegree. 

This repo is about the webapp, which was online on Heroku until end of 2022. Currently I have no other deployment online and development here is paused. 

Furthermore, there is [another repository](https://github.com/muellermax/Disaster-Response), which can be cloned and deployed on another server. 


## <a class="anchor" id = "data">Data</a>
The data was proviced by [Figure Eight](https://appen.com/). You can have a look at it [here](https://github.com/muellermax/nlp-disaster-app/tree/main/data). 

It consists mainly of text messages and the categorization of the corresponding catastrophe (e.g. strom, fire, earthquake, etc.). This data can be used to train a text classifier. 


## <a class="anchor" id="file-description">File description</a>
* app: Folder that contains the necessary files for deployment:
    * run.py: Python script that starts the app and loads the ML-model as well as the plotly visualizations. 
    * train_classifier.py: Script to train the classifer (not essential for the webapp)
    * classifier.pkl: The pickle file of the classifier. 
    * templates => master.html: The "index"-page of this dashboard. 
    * templates => go.html: Shows the classification of the given text message. 
* data: Folder that includes the data (stored in CSV and a database) and the python file that prepares the data. 
    * process_data.py: Python script that includes an ETL pipeline to extract, transform and load the data in a database. 
    * Two CSV-files: Containing disaster messages and their categories. 
    * Database-files: SQL database
* models: Folder that includes train_classifier.py to train a classifier as well as the ready pkl-file. 


## <a class="anchor" id="interact">How to interact</a>
Every contribution is welcome. I think there are many possibilities to improve the performance of the ML-model. 
I am currently working with KNeighbors, which performs slightly better that MultinomialNB and without extended GridSearch. As you can see on the information about the
training set, some categories (like aid_related or weather_related) do appear more often than other categories (like 
hospitals or fire). The precision of the classifier could be improved by taking away the "over-represented" categories
or other data engineering. 


## <a class="anchor" id="thx">Acknowledgements</a>
Thanks to Figure Eight for providing the data for us students. Also thanks to the Udacity team for all the instructions. 

Deployment to Heroku was a bit tricky, I had several AttributeErrors and "module not found" errors. So just like so many times, Stackoverflow finally helped me [here](https://stackoverflow.com/questions/9383014/cant-import-my-own-modules-in-python). 


## <a class="anchor" id="author">Author</a>
Maximilian Müller, Senior Business Development Manager in the Renewable Energy sector. Now diving into the field of Data Science. 


## <a class="anchor" id="license">License</a>
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
