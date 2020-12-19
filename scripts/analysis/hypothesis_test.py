'''
This class is used for Hypothesis Testing
'''
from pandas import read_csv
from scipy.stats import ttest_rel, wilcoxon
from numpy import log


def log_t_test(population_1, population_2):
    '''
    conduct a log t test on the two populations
    ---
    Inputs
        @param popualtion_1: an array (assumed lognormal distribution)
        @param population_2: an array (assumed lognormal distribution)
    Outputs
        pvalue: the probablity of observing the difference observed assuming both
        populations have the same mean
    ---
    Example
        p = t_test(data["a"], data["b"])
    '''
    if population_1.min() < 0:
        population_1 = log(population_1 + 1 - population_1.min())
    else:
        population_1 = log(population_1 + 1)
    
    if population_2.min() < 0:
        population_2 = log(population_2 + 1 - population_2.min())
    else:
        population_2 = log(population_2 + 1)

    statistic, pvalue = ttest_rel(population_1, population_2, nan_policy="omit")
    return pvalue


def wilcoxon_test(population_1, population_2):
    '''
    Conduct an wilcoxon test on the two populations against the alternative
    hypothesis that population_1 > population_2
    ---
    Inputs
        @param popualtion_1: an array
        @param population_2: an array
    Outputs
        pvalue: the probablity of observing the difference observed assuming both
        populations have the same mean
    ---
        p = man_whitney(data["a"], data["b"])
    '''
    statistic, pvalue = wilcoxon(population_1, population_2, alternative="greater", correction=True)
    return pvalue


# Compare the two libraries - note population 2 is smallere
# df_1 = read_csv("data/unfiltered/all_questions.csv")
# df_2 = read_csv("data/filtered/deprecated_libraries.csv")
df_1 = read_csv("data/filtered/deprecated_libraries.csv")
df_2 = read_csv("data/filtered/explicit_mention.csv")

# in order to compare, neither can be missing answers
df_1 = df_1.dropna(subset=['answer_id'])
df_2 = df_2.dropna(subset=['answer_id'])


df_1["quality"] = (df_1["question_score"] + df_1["answer_score"])/df_1["view_count"]
df_2["quality"] = (df_2["question_score"] + df_2["answer_score"])/df_2["view_count"]

# We will be assessing the following columns to access the quality of the answers
quality_columns = ["question_score", "view_count", "answer_count", "question_comment_count", "answer_score", "answer_comment_count", "quality"]


# log-t-test comparision
print("T Tests")

for column in quality_columns:
    population_1 = df_1[column]
    population_2 = df_2[column]

    # cut off top quantile because the data is extremely heavy tailed
    population_1 = population_1[population_1 < population_1.quantile(q=0.95)]
    population_2 = population_2[population_2 < population_2.quantile(q=0.95)]

    n = min(population_1.count(), population_2.count())

    p = log_t_test(population_1.sample(n=n), population_2.sample(n=n))

    print(column, ":", p*100, "%")

print("\n======")
print("Log T Tests")

for column in quality_columns:
    population_1 = df_1[column]
    population_2 = df_2[column]    

    n = min(population_1.count(), population_2.count())


    p = log_t_test(population_1.sample(n=n), population_2.sample(n=n))

    print(column, ":", p*100, "%")



# Since the dataset is extremely heavy tailed, we will also conduct a ManWhitney u test
print("\n======")
print("Wilcoxon Test")

for column in quality_columns:
    population_1 = df_1[column]
    population_2 = df_2[column]   

    n = min(population_1.count(), population_2.count())

    p = wilcoxon_test(population_1.sample(n=n), population_2.sample(n=n))

    print(column, ":", p*100, "%")

