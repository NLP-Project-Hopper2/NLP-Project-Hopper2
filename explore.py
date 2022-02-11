import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import prepare

def new_features(train, validate, test):
    '''
    This function takes in the train, validate, and test dfs and adds columns for character and word counts.
    '''

    # adding character count column
    train = train.assign(char_count= train.lemmatized.str.len())
    validate = validate.assign(char_count= validate.lemmatized.str.len())
    test = test.assign(char_count= test.lemmatized.str.len())

    # adding word count column
    train['word_count'] = train.lemmatized.str.split().apply(len)
    validate['word_count'] = validate.lemmatized.str.split().apply(len)
    test['word_count'] = test.lemmatized.str.split().apply(len)

    return train, validate, test

def language_count(train):
    '''
    This function takes in the train data and does a value_counts for the languages, plotting
    a bar plot with the top language highlighted in 
    '''
    # creating language freq barplot (horizontal)
    train.language.value_counts(ascending = True, normalize = True).plot.barh(color = \
                                                    ['#b7b7b7ff', '#b7b7b7ff', '#b7b7b7ff', '#b7b7b7ff', \
                                                    '#f3993aff'], figsize = (12, 7))
    # adding title
    plt.title('Python Makes up Almost Half of Programming Languages\n')
    plt.show();