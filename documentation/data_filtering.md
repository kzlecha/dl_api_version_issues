# Data Filtering

This discribes how the data was collected and filtered for analysis.

## Data Collection
First the data was collected from Stack Overflow. Data relevant to each library
was collected separately. The queries used are listed in `scripts/queries.sql`.
All data collected at this stage can be found in the `data/unfiltered/source`
directory in csv form.

All questions were selected, both with and without answer. Furthermore, all answers
were selected, not just the Accepted Answer.

The query tool used is the [Stack Exchange Query Tool](https://data.stackexchange.com/stackoverflow/query/new)

## Data Filtering

This outlines the steps used to filter the data after all of the initial data had
been collected.

### Combining the Data

The data was combined by reading in each csv as a dataframe and concatinating them into
one large dataframe. Any duplicate question/answer pairs were dropped and the columns
were renamed for increased readablity.

The script used to filter is `scripts/data_filtering/combine_questions.py`.

### Filtering by Deprecated Libraries

A manual investigation was done to find deprecated API's within a library. This
collection was done primarily via the offical release notes on the appropriate
library's github or official documentation and supported via searching online
forums and blogs, notably stack overflow and github issues. These deprecations are
outlined in `documentation/relevant_libraries.md`.

Then the data was filtered by searching for references to any deprecated library
in the body of the question or in the answer to the question. Then, to ensure that
the question was relevant to deprecation, the questions were filtered by the questions
asked after the release date of the version that deprecated the API. In this way,
all questions that in `data/filtered/deprecated_libraries.csv` are referencing an
API that has been deprecated.

The relevant filtering can be found in `scripts/data_filtering/find_deprecated_lib.py`.

The average deprecations per release per library are depicted below:
- TENSORFLOW : 6.6
- KERAS : 10.0
- TESSERACT : 2.2
- PYTORCH : 5.090909090909091
- THEANO : 5.375
- CAFFE : 2.0
- PYSPARK : 5.142857142857143

### Filtering Explicit Reference to Deprecation

A separate filtering is done based on the study "An Empirical Study of Obsolete Answers on
Stack Overflow" by Haoxiang Zhang et. al. In this study, the following list of
keywords were used to find obsolete answers as pointed out by commentors.

The keywords used: `"deprecate", "deprecation", "out of date", "outdated", "obsolete"`.

To further narrow the results, only questions with answers were considered.

This filtering was done in the script `scripts/data_filtering/find_explicit.py`
and saved in `data/filtered/explicit_mention.csv`.

