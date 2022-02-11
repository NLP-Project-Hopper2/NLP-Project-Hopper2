import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats as stats
plt.style.use('seaborn-whitegrid')

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

############################# Q1.

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

############################# Q2.
def char_word_corr(train):
    '''
    This function takes in the train df and plots character count against word count in a scatter
    plot with a hue set to language.
    '''

    plt.figure(figsize = (12, 8))

    sns.scatterplot(data = train, x = 'word_count', y = 'char_count', hue = 'language', \
                palette = ['#b7b7b7ff', '#000000', '#f3993aff', '#4a86e8ff', 'grey'])
    plt.title('Positive Correlation Between Character and Word Count\n')
    plt.show()



############################# Q3.
def word_count(train):
    '''
    This function takes in the train df and creates and df of the average word count and freq per language.
    It the plots the language frequencies on a barplot and prints the results of the corresponding statistical 
    test.
    '''

    # creating dfs for word count and freq
    word_count = pd.DataFrame(train.groupby('language').word_count.mean().sort_values())
    word_count['freq'] = round(word_count.word_count / word_count.word_count.sum(), 3)

    # plotting viz
    word_count.freq.sort_values(ascending = False).plot.barh(color = ['#b7b7b7ff', '#b7b7b7ff', '#b7b7b7ff', \
                                                                    '#b7b7b7ff', '#4a86e8ff'], figsize = (12, 7))
    plt.title('Except for TypeScript, Most Languages Average ~20% of Total Word Count\n')
    plt.show()

    # stats test results
    import scipy.stats as stats

    # separate word count by language and conduct statistical testing
    p = train.word_count[train.language == 'Python']
    js = train.word_count[train.language == 'JavaScript']
    c = train.word_count[train.language == 'C#']
    j = train.word_count[train.language == 'Java']
    t = train.word_count[train.language == 'TypeScript']

    # set alph
    alpha = .05

    # compute statistics
    t, p = stats.kruskal(p, js, c, j, t)

    if p > alpha:
        print(f'With an alpha of {alpha}, a t-statistic of {round(t, 2)} and a p-value of {round(p, 2)}, we fail to reject the null hypothesis.')
    else:
        print(f'With an alpha of {alpha}, a t-statistic of {round(t, 2)} and a p-value of {round(p, 2)}, we reject the null hypothesis.')


def char_count(train):
    '''
    This function takes in the train df and creates and df of the average character count and freq per language.
    It the plots the language frequencies on a barplot and prints the results of the corresponding statistical 
    test.    
    '''

    # creating df for character count and freq
    char_count = pd.DataFrame(train.groupby('language').char_count.mean().sort_values())
    char_count['freq'] = round(char_count.char_count / char_count.char_count.sum(), 3)

    # plotting viz
    char_count.freq.plot.barh(color = ['#b7b7b7ff', '#b7b7b7ff', '#b7b7b7ff', \
                                    '#b7b7b7ff', '#f3993aff'], figsize = (12, 7))
    plt.title('C# Has Almost a Quarter of Average Character Count Compared to Total Character Count Across All Languages\n')
    plt.show()

    # stats testing
    import scipy.stats as stats

    # separate word count by language and conduct statistical testing
    p = train.char_count[train.language == 'Python']
    js = train.char_count[train.language == 'JavaScript']
    c = train.char_count[train.language == 'C#']
    j = train.char_count[train.language == 'Java']
    t = train.char_count[train.language == 'TypeScript']

    # set alph
    alpha = .05

    # compute statistics
    t, p = stats.kruskal(p, js, c, j, t)

    if p > alpha:
        print(f'With an alpha of {alpha}, a t-statistic of {round(t, 2)} and a p-value of {round(p, 2)}, we fail to reject the null hypothesis.')
    else:
        print(f'With an alpha of {alpha}, a t-statistic of {round(t, 2)} and a p-value of {round(p, 2)}, we reject the null hypothesis.')

############################# Q4.
def top_25_freq(train):
    '''
    This function takes in the train dataframe and splits the data by language, creating a df of the top 
    25 words in each language, along with their counts and frequencies. It then plots the frequencies of each
    word that appears across the top 25 words for each language.
    '''

    # combining the text strings for each language

    # creating dfs
    df_python = train[train.language == 'Python']
    df_js = train[train.language == 'JavaScript']
    df_java = train[train.language == 'Java']
    df_c = train[train.language == 'C#']
    df_type = train[train.language == 'TypeScript']

    # generating text strings for each df
    all_words = ' '.join(train.lemmatized.astype(str))
    python_words = ' '.join(df_python.lemmatized.astype(str))
    js_words = ' '.join(df_js.lemmatized.astype(str))
    java_words = ' '.join(df_java.lemmatized.astype(str))
    c_words = ' '.join(df_c.lemmatized.astype(str))
    type_words = ' '.join(df_type.lemmatized.astype(str))

    # creating a df for the word count and frequency
    # word count
    df_all_count = pd.DataFrame(pd.Series(all_words.split()).value_counts(), columns = ['all_word_cnt']).head(25)

    # word frequency
    df_all_count['all_word_freq'] = pd.Series(all_words.split()).value_counts(normalize = True).head(25)

    ############################################

    # creating a df for the word count and frequency
    # word count
    df_python_count = pd.DataFrame(pd.Series(python_words.split()).value_counts(), columns = ['python_word_cnt']).head(25)

    # word frequency
    df_python_count['python_word_freq'] = pd.Series(python_words.split()).value_counts(normalize = True).head(25)

    ############################################

    # creating a df for the word count and frequency
    # word count
    df_js_count = pd.DataFrame(pd.Series(js_words.split()).value_counts(), columns = ['js_word_cnt']).head(25)

    # word frequency
    df_js_count['js_word_freq'] = pd.Series(js_words.split()).value_counts(normalize = True).head(25)

    ############################################

    # creating a df for the word count and frequency
    # word count
    df_java_count = pd.DataFrame(pd.Series(java_words.split()).value_counts(), columns = ['java_word_cnt']).head(25)

    # word frequency
    df_java_count['java_word_freq'] = pd.Series(java_words.split()).value_counts(normalize = True).head(25)

    ############################################

    # creating a df for the word count and frequency
    # word count
    df_c_count = pd.DataFrame(pd.Series(c_words.split()).value_counts(), columns = ['c_word_cnt']).head(25)

    # word frequency
    df_c_count['c_word_freq'] = pd.Series(c_words.split()).value_counts(normalize = True).head(25)

    ############################################

    # creating a df for the word count and frequency
    # word count
    df_type_count = pd.DataFrame(pd.Series(type_words.split()).value_counts(), columns = ['type_word_cnt']).head(25)

    # word frequency
    df_type_count['type_word_freq'] = pd.Series(type_words.split()).value_counts(normalize = True).head(25)

    ###########################################################################

    # creating df of top 50 word frequencies for each language
    df_word_counts = pd.concat([df_all_count.all_word_freq, df_python_count.python_word_freq,\
          df_js_count.js_word_freq, df_java_count.java_word_freq,\
          df_c_count.c_word_freq, df_type_count.type_word_freq], axis = 1).fillna(0)

    # creating a df with the words that appear in the top 25 words for all languages
    df_word_counts[(df_word_counts.python_word_freq > 0) & (df_word_counts.js_word_freq > 0)\
                & (df_word_counts.java_word_freq > 0) & (df_word_counts.c_word_freq > 0)\
                & (df_word_counts.type_word_freq > 0)].sort_values(by = 'all_word_freq').plot.\
                            barh(figsize = (14, 6), stacked = True, \
                                                color = ['black', '#f3993aff', '#b7b7b7ff', '#A865C9', \
                                                        '#4a86e8ff', 'grey'])

    plt.title('Bot, Use, and Using Commonly Used Across All Languages\n')
    plt.show()
    
###########################################################    
def post_explore_info(train, validate, test):
    """
    Function displays information on data after explore functioas are applied
    and datat is explit into `train`, `validate` and `test`
    """
    print(f"Records in Train data set    =  {train.shape[0]}")
    print(f"Records in Validate data set =  {validate.shape[0]}")
    print(f"Records in Test data set     =  {test.shape[0]}")
    print('------------------------------------')
    print('------------ Data Info -------------')
    return train.info()    
