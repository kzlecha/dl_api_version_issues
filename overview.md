# Overview of Findings
## Methodology

### Libraries

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

The query was conducted using the [Stack Exchange Query Tool](https://data.stackexchange.com/stackoverflow/query/new)

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

#### Determining the Issues Discussed

This analysis used Latent Dirichlet allocation (LDA) to determine the primary topics discussed after an API has been deprecated. 
This served two purposes. First, this helps provide evidence for or against assumptions made about the topics of discussion on Stack Overflow. 
Second, while a question might mention deprecation, it is not necessarily primarily about deprecation. By extracting the topics of discussion, 
we are better able to represent the core component of a question and answer.

This was supplemented by a human evaluation of the questions with a 95% confidence sample.


#### Metric for Quality
In contrast to quality, creating a metric for the discussion of deprecation is more clear. We define two metrics for the discussion of deprecation:
1. an explicit mention of the root `"deprecate"`
2. the main topic of the question is deprecation

The keywords used to determine an explicit mention of the root *deprecate* are outlined in the methodology. However, since not all
questions that have these keywords will be explicitly about deprecation, it must be supplemented. LDA Topic Modeling was used to assess 
if the overall topic discussed in the question and answer is deprecation. This filter excludes any secondary topics discussed.

#### Hypothesis Testing

We conduct two-sided hypothesis tests on the quality of a population of questions about deprecation and the quality of a population
of questions that are not about deprecation. However, since the data is heavy tailed, it does not abide by the assumptions of a T-Test.

Three tests were used: a T test on 95% of the data, a log t-test, and a Wilcoxon Sign Rank Test.

#### Regression Model

A random forest regression model was used to extract the feature importance in predicting the quality of the question.
It is trained on both questions about question with an API post-deprecation and questions explicitly referencing deprecation.
A Boolean variable is created to state which dataset the question originates. The topics found for the question and answer
via LDA are input as a predictor variable for the model. The topics found in questions about a deprecated API are labeled by IDs
ranged `[0,19]` and topics for questions with an explicit reference to deprecation are labeled by their ID + 20, creating a labe
with range `[20, 39]`.

## Results
Numerical Results can be found in the `documentation` folder.

These results show that the questions about model training overall have higher quality than most other topics.
However, it is interesting to note, within questions that explicitly reference deprecation of APIs,
questions about Model Deprecation had higher quality than questions about model training.
Across both datasets, questions with a "main topic" related to deprecation had a lower quality than other questions in the same dataset.

On the other hand, questions explicitly about deprecation are more likely to have a positive quality. Questions about an API after 
it has been deprecated have higher variance and are more likely to be down-voted.

The most important features in the random forest model are the scores of the question and the answer. This is expected, as the subjective
community scores are used in the calculation of the quality. However, the third most important feature is the main topic discussed. To compare,
an explicit reference to deprecation is the least important determinant of quality. This suggests that while the topic of deprecation 
is a factor in assessing the quality, the quality questions with an explicit reference to deprecation but are not primarily about the deprecation 
is more dependent on the main topic than the reference.

## Conclusions
It was found that questions about a deep learning API after its deprecation, specifically training models using said API, were considered
higher quality than questions specifically about deprecation. Questions asked about an API after its deprecation were calculated to have 
a higher average quality than the average quality questions about the studied frameworks. This suggests that deprecation of an API tends 
to overlap with a higher question quality. By contrast, questions primarily about deprecation, by explicitly referencing deprecation or 
primary topic being deprecation, have a lower average quality than questions about the studied frameworks.

This shows that deprecation affects developers in many ways. Most developers ignore deprecation and do not adopt to the most recent version. 
This reflects in the metrics of quality. Since developers do not replace the API after it has been deprecated, questions about these APIs are 
of higher value to the community. By contrast, questions about deprecation are rated of lower value to the community because it is more rare 
that developers replace the API. As shown by the results of this study, deprecation leads to an increase in quality of answers on Stack Overflow.
