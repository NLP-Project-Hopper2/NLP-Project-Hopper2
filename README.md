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
  * Change data type for total_charges from object to float
  * Drop monthly_charges null values where customers have less than a month of tenure therefore no opportunity to churn
  * Replace all instances of 'No internet service' as that information is in internet_service_type column and doing so simplifies encoding by creating binary values for many of the colums
  * Create dummy variables for columns with object datatype
  * Drop columns that contain duplicate information or are unnecessary
  * Rename columns 
* Create function that splits data into train, validate, and test samples
  * Split 20% (test), 24% (validate), and 56% (train)
* Create prepare.py to save these functions for importing
* Test functions
* 

**Exploration**
* Ask questions/form hypotheses
  * Question/Hypothesis
  * Question/Hypothesis
  * Question/Hypothesis
  * Question/Hypothesis
* Create visualizations
* Use statistical tests to test hypotheses
* Document answers to questions and takeaways
  * Answer
  * Answer
  * Answer
  * Answer
  * Key takeaway is:

**Modeling**
* Train model
* Make predictions
* Evaluate model
* Compute accuracy
* 

**Delivery**
* Report will be in Notebook
* Present via Zoom
* Audience will be direct manager and their manager

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
