import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import nltk.sentiment
from wordcloud import WordCloud
pd.set_option('display.max_colwidth', -1)
import re
from time import strftime
import unicodedata
import json
from pprint import pprint
from PIL import Image
import acquire 
import prepare
###############

### Gathering Data from CSV and splitting
df = pd.read_csv('NLP.csv')
df = df.reset_index().drop(columns = 'index')
train, validate, test = prepare.split_data(df)


##########
# combining the text strings for each language
# creating dfs

#creating word strings

python_words = ''.join(str(train[train.language == 'Python'].lemmatized))
javascript_words = ''.join(str(train[train.language == 'JavaScript'].lemmatized))
c_words = ''.join(str(train[train.language == 'C#'].lemmatized))
java_words = ''.join(str(train[train.language == 'Java'].lemmatized))
typescript_words = ''.join(str(train[train.language == 'TypeScript'].lemmatized))

# generating text strings for each df
python_words = pd.Series(python_words.split()).value_counts()
javascript_words = pd.Series(javascript_words.split()).value_counts()
c_words = pd.Series(c_words.split()).value_counts()
java_words = pd.Series(java_words.split()).value_counts()
typescript_words = pd.Series(typescript_words.split()).value_counts()

####### creating into a DataFrame and adding word counts as 'all_words' within the row
word_counts = pd.concat([python_words, javascript_words, c_words, java_words, typescript_words], axis=1).fillna(0).astype(int)
word_counts.columns = ['python_words', 'javascript_words', 'c_words', 'java_words', 'typescript_words']
word_counts['all_words'] = word_counts.sum(axis=1)

####### The above code settles the data needed for the input to word clouds

### The Following Functions import an image representing the language and creates a word cloud for the top words within them ###

def git_logo():
    ''' The function pushes a word cloud with the gitlogo as the background'''
    plt.figure(figsize=(16,9))
    mask = np.array(Image.open("images/github_logo.png"))
    wc = WordCloud(background_color="white", width=800, height=400, contour_width=1, contour_color='black',mask=mask)
    # generate word cloud
    wc.generate_from_frequencies(word_counts['all_words'])

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    return


#################

def python_logo():
    ''' The function pushes a word cloud with the python logo as the background'''
    plt.figure(figsize=(16,9))
    mask = np.array(Image.open("images/python_inv.png"))
    wc = WordCloud(background_color="white", width=800, height=400, contour_width=1, contour_color='black',mask=mask)
    # generate word cloud
    wc.generate_from_frequencies(word_counts['python_words'])

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    return

#################

def js_logo():
    ''' The function pushes a word cloud with the js logo as the background'''

    plt.figure(figsize=(16,9))
    mask = np.array(Image.open("images/js_logo.png"))

    wc = WordCloud(background_color="white", width=800, height=400, contour_width=2, contour_color='black',mask=mask)
    # generate word cloud
    wc.generate_from_frequencies(word_counts['javascript_words'])

    # show
    plt.imshow(wc,)
    plt.axis("off")
    plt.show()

    return

    #################
def java_logo():
    ''' The function pushes a word cloud with the java logo as the background'''
    plt.figure(figsize=(16,9))
    mask = np.array(Image.open("images/java_logo2.png"))

    wc = WordCloud(background_color="white",width=800, height=400, contour_width=2, contour_color='black',mask=mask)
    # generate word cloud
    wc.generate_from_frequencies(word_counts['java_words'])

    # show
    plt.imshow(wc,)
    plt.axis("off")
    plt.show()   

    return

    #################
def c_logo():
    ''' The function pushes a word cloud with the C# logo as the background'''

    plt.figure(figsize=(16,9))
    mask = np.array(Image.open("images/c_logo_in.png"))

    wc = WordCloud(background_color="white", width=800, height=400, contour_width=15, contour_color='black',mask=mask)
    # generate word cloud
    wc.generate_from_frequencies(word_counts['c_words'])

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    return
    #################

def c_logo2():
    ''' The function pushes a word cloud with the C# logo as the background'''

    plt.figure(figsize=(16,9))
    mask = np.array(Image.open("images/c_inv.png"))

    wc = WordCloud(background_color="white", width=800, height=400, contour_width=2, contour_color='black',mask=mask)
    # generate word cloud
    wc.generate_from_frequencies(word_counts['c_words'])

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    return


    #################
def ts_logo():
    ''' The function pushes a word cloud with the TypeScript logo as the background'''

    plt.figure(figsize=(16,9))
    mask = np.array(Image.open("images/image (1).png"))
    wc = WordCloud(background_color="white", width=800, height=400, contour_width=3, contour_color='black',mask=mask)
    # generate word cloud
    wc.generate_from_frequencies(word_counts['typescript_words'])

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    return 