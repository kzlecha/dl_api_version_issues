'''
This class is used for Hypothesis Testing
'''
from pandas import read_csv
from scipy.stats import ttest_rel, wilcoxon


def t_test(population_1, population_2):
    '''
    conduct a t test on the two populations
    ---
    Inputs
        @param popualtion_1: an array
        @param population_2: an array
    Outputs
        pvalue: the probablity of observing the difference observed assuming both
        populations have the same mean
    ---
    Example
        p = t_test(data["a"], data["b"])
    '''
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
df_1 = read_csv("data/filtered/deprecated_libraries.csv")
df_2 = read_csv("data/filtered/explicit_mention.csv")

# in order to compare, neither can be missing answers
df_1 = df_1.dropna(subset=['answer_id'])

# We will be assessing the following columns to access the quality of the answers
quality_columns = ["question_score", "view_count", "answer_count", "question_comment_count", "answer_score", "answer_comment_count"]


# t-test comparision
print("T Tests")

for column in quality_columns:
    population_1 = df_1[column]
    population_2 = df_2[column]    

    # since the dataset is extremely heavy tailed, we will cut off all outliers
    # more than two standard deviations from the mean - 95%
    threshold_1 = population_1.mean() + 2*population_1.std()
    threshold_2 = population_2.mean() + 2*population_2.std()

    population_1 = population_1[population_1 < threshold_1]
    population_2 = population_2[population_2 < threshold_2]

    p = t_test(population_1.sample(n=population_2.count()), population_2)

    print(column, ":", p*100, "%")



# Since the dataset is extremely heavy tailed, we will also conduct a ManWhitney u test
print("\n======")
print("Wilcoxon Test")

for column in quality_columns:
    population_1 = df_1[column]
    population_2 = df_2[column]    

    p = wilcoxon_test(population_1.sample(n=population_2.count()), population_2)

    print(column, ":", p*100, "%")
