import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """
    A function to load raw data.
    :param messages_filepath: Filepath for CSV-file with messages
    :param categories_filepath: Filepath for CSV-file with categories
    :return: messages (DataFrame) and categories (DataFrame)
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    df = messages.merge(categories, on='id', how='left')

    return df


def clean_data(df):
    """
    A function to clean and prepare data for machine learning.
    :param df: DataFrame with labels and features.
    :return: DataFrame that can be used in ML pipeline
    """

    # Create a dataframe of the individual category columns
    categories = df.categories.str.split(';', expand=True)

    # Select the first row of the categories dataframe
    categories_list = df.categories[0].split(';')

    # Extract a list of new column names for categories.
    category_colnames = []
    for cat in categories_list:
        category_colnames.append(cat.split('-')[0])

    # Rename the columns of 'categories'
    categories.columns = category_colnames

    # Keep only the last character of the value (e.g. For example, 'related-0' becomes '0').
    for column in categories:
        # Set each value to be the last character of the string
        categories[column] = categories[column].apply(lambda x: x.split('-')[1])

    # Sonvert column values from string to numeric
    for column in categories:
        categories[column] = categories[column].astype('int64')

    # Drop the original 'categories' column from 'df'
    df = df.drop('categories', axis=1)

    # Concatenate the original DataFrame with the new 'categories' DataFrame
    df = pd.concat([df, categories], axis=1)

    # Drop duplicates
    df = df.drop_duplicates()

    return df


def save_data(df, database_filename):
    """
    A function to safe the DataFrame to a SQL database.
    :param df: DataFrame that should be stored in SQL database.
    :param database_filename: Specify database
    :return: None
    """
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('database_table', engine, index=False, if_exists='replace')


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
