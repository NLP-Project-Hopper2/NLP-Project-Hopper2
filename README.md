# Using Classification To Predict Programming Language

Team Members: Alejandro Velasquez, Daniel Northcutt, Lori Ainslie, Stephanie Jones

## Table of Contents

1. [Project Planning / About The Project](#project-planning--about-the-project)

2. [Acquisition](#acquisition)

3. [Preparation](#preparation)

4. [Exploration](#exploration)

5. [Modeling](#modeling)

6. [Delivery / Conclusion](#delivery--conclusion)

## Project Planning / About The Project

### Project Goal

* To build a classification model that can predict the programming language of a repository, given the text of the README file

### Project Description

For this project, we scraped data from GitHub repositories about Bots and built models to predict the programming language based on the README contents.

Why is this project important?

### Initial Hypotheses/Questions

* Question/Hypothesis

* Question/Hypothesis

* Question/Hypothesis

* Question/Hypothesis

### Data dictionary

|   Column_Name   | dtype | Description      |
|   -----------   | ----------- | ---------- |
| repository | object | repository link |
| language   | object | programming language used for the project  |

[Trello Board](https://trello.com/b/KFt1reNg/githublanguage-prediction)


## Acquisition

* Deliverable: acquire.py module
* Create function for scraping github, caching, and reading in data
* Save functions to an acquire.py for importing
* Test functions


## Preparation

* Deliverable: prepare.py module
* Create function that cleans data
  * Drop nulls and remove results in languages other than English
  * Lowercase all letters
  * Normalize text
  * Create columns for stemmed data and lemmatized data 
  * Remove stopwords
* Create function that splits data into train, validate, and test samples
  * Split 20% (test), 24% (validate), and 56% (train)???????
* Save functions to a prepare.py for importing
* Test functions

## Exploration

* Ask questions/form hypotheses
  * Question/Hypothesis
  * Question/Hypothesis
  * Question/Hypothesis
  * Question/Hypothesis
* Explore using visualizations
  * Create wordclouds
  * Explore term frequencies
  * Explore ngrams
* Use statistical tests to test hypotheses
* Document answers to questions and takeaways
  * Answer
  * Answer
  * Answer
  * Answer
  * Key takeaway is:

## Modeling

* Establish a baseline
* Determine evaluation metric
* Build, fit and use models to make predictions
* Compute evaluation metrics to evaluate models' performance
* Select best model and use and evaluate on test dataset
* Document takeaways

## Delivery / Conclusion

* Create Google Slides presentation
* Create final notebook
* Present via Zoom
* Audience will be a general audience

### Recommendations and Next Steps

* Recommendation
* Recommendation

* With more time and resources, .....

### Steps to Recreate:

* Make a github personal access token.
  1. Go here and generate a personal access token https://github.com/settings/tokens (don't need to select any scopes)
  2. Create an env.py file in your working directory 
  3. Save it in your env.py file under the variable `github_token`
  4. Add your github username to your env.py file under the variable `github_username`
* Create a gitignore and add your env file to prevent your credentials from getting pushed to Github
* Download the aquire.py and prepare.py files to your working directory
* Download the ????_final notebook to your working directory
* Read this README.md
* Run the ?????_final.ipynb notebook

### ALL STAR TEAM REPRESENT!!!
