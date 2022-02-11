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
    raw_data = acquire.scrape_github_data()
    train, validate, test = prepare.split_data()


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
    raw_data = acquire.scrape_github_data()
    train, validate, test = prepare.split_data()
    
    return print(f'Baseline Accuracy: {round(max(train.language.value_counts()) / train.shape[0] *100,2)}%')

#######################################
def logistic_regression_tfidf():
    
    raw_data = acquire.scrape_github_data()
    train, validate, test = prepare.split_data()
    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(train.lemmatized)
    y = train.language
    X_train, y_train, X_validate, y_validate, X_test, y_test = X_train_split(X, y)
    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))

    lm = LogisticRegression().fit(X_train, y_train)

    #form predictions
    train['predicted'] = lm.predict(X_train)
    validate['predicted'] = lm.predict(X_validate)
    test['predicted'] = lm.predict(X_test)
    print('Train Accuracy: {:.2%}'.format(accuracy_score(train.actual, train.predicted)))
    print('---')
    print('Confusion Matrix')
    print(pd.crosstab(train.predicted, train.actual))
    print('---')
    print(classification_report(train.actual, train.predicted))
    print('----------------------------------------------')
    print('Validate Accuracy: {:.2%}'.format(accuracy_score(validate.actual, validate.predicted)))
    print('---')
    print('Confusion Matrix')
    print(pd.crosstab(validate.predicted, validate.actual))
    print('---')
    print(classification_report(validate.actual, validate.predicted))


#######################################
raw_data = acquire.scrape_github_data()
train, validate, test = prepare.split_data()

# Count Vectorizer using bag of words - defining X & y variables
cv = CountVectorizer()
X = cv.fit_transform(train.lemmatized)
y = train.language

# function as above
X_train, y_train, X_validate, y_validate, X_test, y_test = X_train_split(X, y)

def BoW_Decision_tree():
    
    raw_data = acquire.scrape_github_data()
    train, validate, test = prepare.split_data()

    # Count Vectorizer using bag of words - defining X & y variables
    cv = CountVectorizer()
    X = cv.fit_transform(train.lemmatized)
    y = train.language

    # function as above
    X_train, y_train, X_validate, y_validate, X_test, y_test = X_train_split(X, y)
    
    
    
    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))


    tree = DecisionTreeClassifier(max_depth=5).fit(X_train, y_train)
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

#######
def BoW_Random_Forest():
        
    raw_data = acquire.scrape_github_data()
    train, validate, test = prepare.split_data()

    # Count Vectorizer using bag of words - defining X & y variables
    cv = CountVectorizer()
    X = cv.fit_transform(train.lemmatized)
    y = train.language

    # function as above
    X_train, y_train, X_validate, y_validate, X_test, y_test = X_train_split(X, y)
    
    
    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))


    forest = RandomForestClassifier(min_samples_leaf = 1, max_depth = 8, random_state= 123).fit(X_train, y_train)



    train['forest_predicted'] = forest.predict(X_train)
    validate['forest_predicted'] = forest.predict(X_validate)
    test['forest_predicted'] = forest.predict(X_test)

    print('Accuracy: {:.2%}'.format(accuracy_score(train.actual, train.forest_predicted)))
    print('---')
    print('Confusion Matrix')
    print(pd.crosstab(train.forest_predicted, train.actual))
    print('---')
    print(classification_report(train.actual, train.forest_predicted))
    print('----------------------------------------------')
    print('Validate Performance: {:.2%}'.format(accuracy_score(validate.actual, validate.forest_predicted)))
    print('---')
    print('Confusion Matrix')
    print(pd.crosstab(validate.forest_predicted, validate.actual))
    print('---')
    print(classification_report(validate.actual, validate.forest_predicted))


    #######################################



    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))


    tree = DecisionTreeClassifier(max_depth=4).fit(X_train, y_train)
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

def test_model_rf():
            
    raw_data = acquire.scrape_github_data()
    train, validate, test = prepare.split_data()

    # Count Vectorizer using bag of words - defining X & y variables
    cv = CountVectorizer()
    X = cv.fit_transform(train.lemmatized)
    y = train.language

    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))


    tree = DecisionTreeClassifier(max_depth=5).fit(X_train, y_train)
    train['tree_predicted'] = tree.predict(X_train)
    validate['tree_predicted'] = tree.predict(X_validate)
    test['tree_predicted'] = tree.predict(X_test)

    print('Accuracy: {:.2%}'.format(accuracy_score(test.actual, test.tree_predicted)))
    print('---')
    print('Confusion Matrix')
    print(pd.crosstab(test.tree_predicted, test.actual))
    print('---')
    print(classification_report(test.actual, test.tree_predicted))

