import unicodedata
import re
import json
import os

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd
import acquire
from time import strftime

from sklearn.model_selection import train_test_split


import warnings
warnings.filterwarnings('ignore')



def basic_clean(string):
    '''
    This function takes in a string and
    returns the string normalized.
    '''
    string = unicodedata.normalize('NFKD', string)\
            .encode('ascii', 'ignore')\
            .decode('utf-8', 'ignore')
    string = re.sub(r'[^\w\s]', '', string).lower()
    return string



def tokenize(string):
    '''
    This function takes in a string and
    returns a tokenized string.
    '''
    # Create tokenizer.
    tokenizer = nltk.tokenize.ToktokTokenizer()
    
    # Use tokenizer
    string = tokenizer.tokenize(string, return_str = True)
    
    return string




def stem(string):
    '''
    This function takes in a string and
    returns a string with words stemmed.
    '''
    # Create porter stemmer.
    ps = nltk.porter.PorterStemmer()
    
    # Use the stemmer to stem each word in the list of words we created by using split.
    stems = [ps.stem(word) for word in string.split()]
    
    # Join our lists of words into a string again and assign to a variable.
    string = ' '.join(stems)
    
    return string




def lemmatize(string):
    '''
    This function takes in string for and
    returns a string with words lemmatized.
    '''
    # Create the lemmatizer.
    wnl = nltk.stem.WordNetLemmatizer()
    
    # Use the lemmatizer on each word in the list of words we created by using split.
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    
    # Join our list of words into a string again and assign to a variable.
    string = ' '.join(lemmas)
    
    return string




def remove_stopwords(string, extra_words=[], exclude_words=[]):
    '''
    This function takes in a string, optional extra_words and exclude_words parameters
    with default empty lists and returns a string.
    '''
    # Create stopword_list.
    stopword_list = stopwords.words('english')
    
    # Remove 'exclude_words' from stopword_list to keep these in my text.
    stopword_list = set(stopword_list) - set(exclude_words)
    
    # Add in 'extra_words' to stopword_list.
    stopword_list = stopword_list.union(set(extra_words))

    # Split words in string.
    words = string.split()
    
    # Create a list of words from my string with stopwords removed and assign to variable.
    filtered_words = [word for word in words if word not in stopword_list]
    
    # Join words in the list back into strings and assign to a variable.
    string_without_stopwords = ' '.join(filtered_words)
    
    return string_without_stopwords



#### MAIN FUNCTION ####

def prep_article_data(extra_words=[], exclude_words=[]):
    '''
    This function take in a df and the string name for a text column with 
    option to pass lists for extra_words and exclude_words and
    returns a df with the text article title, original text, stemmed text,
    lemmatized text, cleaned, tokenized, & lemmatized text with stopwords removed.
    '''
    column = 'readme_contents'

    df = acquire.scrape_github_data()

    df['clean'] = df[column].astype(str).apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(remove_stopwords, 
                                extra_words=extra_words, 
                                exclude_words=exclude_words)
    
    # df['stemmed'] = df['clean'].apply(stem)
    df['lemmatized'] = df['clean'].apply(lemmatize)
    
    return df

#####

def isEnglish(s):
    '''This function filters out for just english words in readme_contents for github repos'''
    try:
        s.encode(encoding='utf-8').decode('ascii')
        
    except UnicodeDecodeError:
        return False
    else:
        return True

####

def get_top_5_languages(df):
    '''This function takes in a cleaned df and filters for just the top 5 
    languages, dropping the rest. This is a subfunction that will be added to the filter
    function which will produce the final prepared df, prior to splitting.'''

    top5_list = list(df.language.value_counts().head(5).index)
    mask = df.language.apply(lambda x: x in top5_list)
    df = df[mask]
    return df

#### Final Clean and Filter Data w/ Functions 
def clean_and_filter_data():
    '''
    This function checks for a local csv file with the cleaned and filtered data. If
    one exists, it reads it to a df and returns that df.
    
    It a local csv of cleaned and filtered data does not exist it takes the raw data
    (aquired from the acquire module) and calls the above functions to clean and filter
    the raw data, dropping null values, removing repos that are 
    not english, and removing repos in a language outside of the top 5 languages. It then 
    drops the duplicated index columns and caches the cleaned and filtered data to csv local
    csv file.
    '''
    if os.path.isfile('clean_data.csv'):
        df = pd.read_csv('clean_data.csv')

    else:
        df = prep_article_data()
        
        # drops nulls
        df = df.dropna()
        # drops repos that readme is not written in English
        df =df[df.readme_contents.apply(isEnglish) == True]
        # pulls top 5 languages
        df = get_top_5_languages(df)

        # dropping duplicated index columns
        df.drop(columns = ['Unnamed: 0', 'Unnamed: 0.1'], inplace = True)

        # caching
        df.to_csv('clean_data.csv')

    return df
    
###Splitzzy
def split_data(df):
    '''
    This function takes in fully cleaned, filtered and prepared data (in df) and splits
    data into train, validate and test dfs.
    '''

    # splitting
    train, test = train_test_split(df, test_size = .2, random_state = 123, stratify = df.language)
    train, validate = train_test_split(train, test_size = .3, random_state = 123)
    return train, validate, test


