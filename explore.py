import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import prepare

def new_features(train):
    '''
    This function takes in the train df and add columns for character and word counts.
    '''

    # adding character count column
    train = train.assign(char_count= train.lemmatized.str.len())

    # adding word count column
    train['word_count'] = train.lemmatized.str.split().apply(len)

    return train