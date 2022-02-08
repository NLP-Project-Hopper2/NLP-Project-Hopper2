# Predicting 

## About the project

### Project Goal

* To build a classification model that can predict the programming language of a repository, given the text of the README file

### Project Description

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


### Project Planning

**Planning**

* Deliverable: Trello Board
* Define goals
* Determine audience and delivery format
* What is my MVP?
* Ask questions/formulate hypotheses


**Acquisition**

* Deliverable: acquire.py module
* Create function for scraping github, caching, and reading in data
* Create acquire.py to save these functions for importing
* Test functions


**Preparation**

* Deliverable: prepare.py module
* Create function that cleans data
  * Drop nulls and remove results in languages other than English
  * Lowercase all letters
  * Normalize text
  * Create columns for stemmed data and lemmatized data 
  * Remove stopwords
* Create function that splits data into train, validate, and test samples
  * Split 20% (test), 24% (validate), and 56% (train)???????
* Create prepare.py to save these functions for importing
* Test functions

**Exploration**
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

**Modeling**
* Establish a baseline
* Determine evaluation metric
* Build, fit and use models to make predictions
* Compute evaluation metrics to evaluate models' performance
* Select best model and use and evaluate on test dataset

**Delivery**
* Create Google Slides presentation
* Create final notebook
* Present via Zoom
* Audience will be a general audience

### To Recreate This Project:
* You will need an env file with your database credentials (user, password, hostname) saved to your working directory
* Create a gitignore and add your env file to prevent your credentials from getting pushed to Github
* Download the aquire.py and prepare.py files to your working directory
* Download the telco_classification_project_final notebook to your working directory
* Read this README.md
* Run the telco_classification_project_final.ipynb notebook

### Recommendations and Next Steps
* Reduce monthly price for fiber optic internet service

* Send out quarterly customer satisfaction surveys for better insights

* With more time and resources, would like to collect and explore customer satisfaction data


### ALL START TEAM REPRESENT!!!

https://trello.com/b/KFt1reNg/githublanguage-prediction
