import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Turn off pink boxes for demo
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


import acquire 
import prepare


#######################################
### function for further splitting has stratify

def X_train_split(X_data, y_data):
    ''' Further splitting for X & y train,validate,test
    '''
    #pull csv
    df = pd.read_csv('NLP.csv')
    #cleaning
    df = df.reset_index().drop(columns = 'index')
    df = prepare.filter_data(df)

    ### dropping these columns & splitting data
    columns_drop = ['readme_contents', 'clean', 'stemmed']
    df = df.drop(columns_drop, 1)
    train, validate, test = prepare.split_data(df)
    ###

    # Count Vectorizer using bag of words - defining X & y variables
    cv = CountVectorizer()
    X_bag_of_words = cv.fit_transform(train.lemmatized)
    y = train.language




    X_train_validate, X_test, y_train_validate, y_test = train_test_split(X_data, y_data, 
                                                                        stratify = y_data, 
                                                                        test_size=.2, random_state=123)
    
    X_train, X_validate, y_train, y_validate = train_test_split(X_train_validate, y_train_validate, 
                                                                stratify = y_train_validate, 
                                                                test_size=.3, 
                                                                random_state=123)
    
    return X_train, y_train, X_validate, y_validate, X_test, y_test


#######################################

def baseline_accuracy():
    df = pd.read_csv('NLP.csv')
    df = df.reset_index().drop(columns = 'index')
    df = prepare.filter_data(df)
    train, validate, test = prepare.split_data(df)
    return print(f'Baseline Accuracy: {round(max(train.language.value_counts()) / train.shape[0] *100,2)}%')

#######################################







#######################################
#pull csv
df = pd.read_csv('NLP.csv')

#cleaning
df = df.reset_index().drop(columns = 'index')
df = prepare.filter_data(df)


### dropping these columns & splitting data
columns_drop = ['readme_contents', 'clean', 'stemmed']
df = df.drop(columns_drop, 1)
train, validate, test = prepare.split_data(df)
###

# Count Vectorizer using bag of words - defining X & y variables
cv = CountVectorizer()
X = cv.fit_transform(train.lemmatized)
y = train.language

# function as above
X_train, y_train, X_validate, y_validate, X_test, y_test = X_train_split(X, y)

def BoW_Decision_tree(X_train, y_train, X_validate, y_validate, X_test, y_test):
    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))


    tree = DecisionTreeClassifier(max_depth=6).fit(X_train, y_train)
    train['tree_predicted'] = tree.predict(X_train)
    validate['tree_predicted'] = tree.predict(X_validate)
    test['tree_predicted'] = tree.predict(X_test)

    print('Accuracy: {:.2%}'.format(accuracy_score(train.actual, train.tree_predicted)))
    print('---')
    print('Confusion Matrix')
    print(pd.crosstab(train.tree_predicted, train.actual))
    print('---')
    print(classification_report(train.actual, train.tree_predicted))
    print('----------------------------------------------')
    print('Validate Accuracy: {:.2%}'.format(accuracy_score(validate.actual, validate.tree_predicted)))
    print('---')
    print('Confusion Matrix')
    print(pd.crosstab(validate.tree_predicted, validate.actual))
    print('---')
    print(classification_report(validate.actual, validate.tree_predicted))

    #######################################

def test_model(X_train, y_train, X_validate, y_validate, X_test, y_test):
    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))


    tree = DecisionTreeClassifier(max_depth=6).fit(X_train, y_train)
    train['tree_predicted'] = tree.predict(X_train)
    validate['tree_predicted'] = tree.predict(X_validate)
    test['tree_predicted'] = tree.predict(X_test)

    print('Accuracy: {:.2%}'.format(accuracy_score(test.actual, test.tree_predicted)))
    print('---')
    print('Confusion Matrix')
    print(pd.crosstab(test.tree_predicted, test.actual))
    print('---')
    print(classification_report(test.actual, test.tree_predicted))

        #print('----------------------------------------------')
        #print('Validate Accuracy: {:.2%}'.format(accuracy_score(validate.actual, validate.tree_predicted)))
        #print('---')
        #print('Confusion Matrix')
        #print(pd.crosstab(validate.tree_predicted, validate.actual))
        #print('---')
        #print(classification_report(validate.actual, validate.tree_predicted))