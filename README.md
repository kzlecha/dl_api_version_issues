# dl_api_version_issues

This is a repository for research on How deprecation of Deep Learning libraries 
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

## Methodology

### Libraries Studied

The libraries studied are Tensorflow, Keras, Pytorch, Tessaract, Caffe, Theano, 
and PySpark. These were chosen in reference to the paper [REF: The State of the ML-universe: 10 Years of Artificial Intelligence &
Machine Learning Software Development on GitHub]. In addition, PySpark was added because of it's comprehensive documentation in reference
to deprecated libraries.

### Data Collection

#### Question Data Points

The queries used are listed in `scripts/queries.sql`. All data collected at this
stage can be found in the `data/unfiltered/source` directory in csv form.

All questions and their answers pertaining to the libraries studied were collected,
without any data filtering at this step.

The query tool used is the [Stack Exchange Query Tool](https://data.stackexchange.com/stackoverflow/query/new)

#### Deprecated APIs

A manual investigation was done to find deprecated API's within a library. This
collection was done primarily via the offical release notes on the appropriate
library's github or official documentation and supported via searching online
forums and blogs, notably stack overflow and github issues. These deprecations are
outlined in `documentation/relevant_libraries.md`.

### Data Filtering

#### Deprecated Libraries

Using the deprecated APIs found in the manual investigation, the questions were
further filtered to select all references to a deprecated API after the release of
the relevant deprecation.

#### Explicit Reference to Deprecation

This filter was inspired by the related work "An Empirical Study of Obsolete Answers on
Stack Overflow". In this study, the following list of keywords were used to find
obsolete answers (answers that have become out-dated due to deprecation) as pointed
out by commentors.

The keywords used: `"deprecate", "deprecation", "out of date", "outdated", "obsolete"`.

Furthermore, only questions with answers were considered.

### Analysis

#### Metric for Quality
In contrast to quality, creating a metric for the discussion of deprecation is more clear. We define two metrics for the discussion of deprecation:
1. an explicit mention of the root \textit{deprecate}
2. the main topic of the question is deprecation

The keywords used to determine an explicit mention of the root *deprecate* are outlined in the methodology. However, since not all questions that have these keywords will be explicitly about deprecation, it must be supplemented. We apply LDA Topic Modeling to assess if the overall topic discussed in the question and answer is deprecation. This filter excludes any secondary topics discussed.

#### Determining the Issues Discussed

This analysis used Latent Dirichlet allocation (LDA) to determine the primary topics discussed after an API has been deprecated. This served two purposes. First, this helps provide evidence for or against assumptions made about the topics of discussion on Stack Overflow. Second, while a question might mention deprecation, it is not necessarily primarily about deprecation. By extracting the topics of discussion, we are better able to represent the core component of a question and answer.

This was supplemented by a human evaluation of the questions with a 95% confidence sample.

#### Hypothesis Testing

We conduct two-sided hypothesis tests on the quality of a population of questions about deprecation and the quality of a population of questions that are not about deprecation. However, since the data is heavy tailed, it does not abide by the assumptions of a T-Test.

Three tests were used: a T test on 95% of the data, a log t-test, and a Wilcoxon Sign Rank Test.

#### Regression Model

A random forest regression model was used to extract the feature importance in predicting the quality of the 

