from pandas import DataFrame, read_csv


'''
This filtering is based on the study "An Empirical Study of Obsolete Answers on
Stack Overflow" by Haoxiang Zhang et. al. In this study, the following list of
keywords were used to find obsolete answers as pointed out by commentors.

We will use a similar approach in reference to RQ2: Do users discuss the API
versioning for the selected frameworks explicitly?

'''


def explicit_mention(df):
    '''
    find all of the explicti references to deprecation in the dataset
    ---
    Inputs
        @param df: a dataframe
    Outputs
        a dataframe that is a subset of df with only the explict refrence to deprecation
        num_keywords: the split between reference found in question and answer
    ---
    Filter Used
    Used tested filter from "An Empirical Study of Obsolete Answers on Stack Overflow"

    Known false negatives:
        - nightly builds
        - does not support
        - newer v2 API
        - convert to new/old version
    Other possible considered filters:
        - version (falsely collects "inversion" and "conversion")
    ---
    Example:
        df2 = explicit_mention(df1)
        df.to_csv(filepath)
    '''
    keywords = ["deprecate", "deprecation", "out of date", "outdated", "obsolete"]
    num_keywords = {"question":0, "answer":0}

    df_keywords = []

    for i in df.index:
        row = df.loc[i]
        for keyword in keywords:
            # check for questions
            if keyword in row["question_body"].lower():
                num_keywords["question"] += 1
                df_keywords.append(row.values)
            elif type(row["answer_body"]) == "string" and row["answer_body"] is not None and keyword in row["answer_body"].lower():
                num_keywords["answer"] += 1
                df_keywords.append(row.values)

    return DataFrame(df_keywords, columns=df.columns), num_keywords

# read in data
df = read_csv("data/unfiltered/all_questions.csv")

# display explicit words
df_keywords, num_keywords = explicit_mention(df)

# remove questions without answer
df_keywords.dropna(subset=['answer_id'], inplace=True)
df_keywords.to_csv("data/filtered/explicit_mention.csv", index=False)

# show the split
print(df_keywords.count())
print(num_keywords)
