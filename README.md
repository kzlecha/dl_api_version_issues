# dl_api_version_issues

This is a repository for research on how deprecation of Deep Learning libraries 
and APIs affects the quality of answers given on Stack Overflow.

## Research Questions

1. What is the deprecation status of the deep learning libraries in our study?
2. Do users discuss the API versioning for the selected frameworks explicitly?
We manually select X samples of the collected data to investigate whether the users discuss the API versioning explicitly. 
3. What are the DL API versioning issues that are discussed on SO?
4. How do Deep Learning API versioning issues affect the quality of answers in SO?

### Future Studies
Do the users discuss the backward compatibility issues?
[REF: An Empirical Analysis of Backward Compatibility in Machine Learning Systems]

## Running the Code

Note that no relevant data has been included here at the instructions of the supervising
professor.

All scripts can be run in a Python3 virtual environment. Be sure to install all
required packages via: `pip install -r requirements.txt`.

## Directory Structure

* **`scripts`** contains the scripts used to run the analysis. Scripts are organized by use case in directories
* **`documentation`** contains the results of the analysis as of December 23, 2020.
* **`models`** contains the lda, random forest, and linear regression models
* **`plots`** contains any generated graphs

The datasets are not included in this repository.
