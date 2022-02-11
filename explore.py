import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats as stats

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
    plt.show()

def word_count(train):
    '''
    This function takes in the train df and creates and df of the average word count and freq per language.
    It the plots the language frequencies on a barplot.
    '''

    # creating dfs for word count and freq
    word_count = pd.DataFrame(train.groupby('language').word_count.mean().sort_values())
    word_count['freq'] = round(word_count.word_count / word_count.word_count.sum(), 3)

    # plotting viz
    word_count.freq.sort_values(ascending = False).plot.barh(color = ['#b7b7b7ff', '#b7b7b7ff', '#b7b7b7ff', \
                                                                    '#b7b7b7ff', '#4a86e8ff'], figsize = (12, 7))
    plt.title('Except for TypeScript, Most Languages Average ~20% of Total Word Count\n')
    plt.show()

def char_count(train):
    '''
    This function takes in the train df and creates and df of the average character count and freq per language.
    It the plots the language frequencies on a barplot.    
    '''

    # creating df for character count and freq
    char_count = pd.DataFrame(train.groupby('language').char_count.mean().sort_values())
    char_count['freq'] = round(char_count.char_count / char_count.char_count.sum(), 3)

    # plotting viz
    char_count.freq.plot.barh(color = ['#b7b7b7ff', '#b7b7b7ff', '#b7b7b7ff', \
                                    '#b7b7b7ff', '#f3993aff'], figsize = (12, 7))
    plt.title('C# Has Almost a Quarter of Average Character Count Compared to Total Character Count Across All Languages\n')
    plt.show()