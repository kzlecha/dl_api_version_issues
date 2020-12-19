'''
Determinant of Quality

---
There are a lot
- time
- score
- user answer acceptance
- bounty

----
In the reading 
An Empirical Study of Obsolete Answers on Stack Overflow - number of obsolete answers
Determinants of quality, latency, and amount of Stack Overflow answers about recent Android APIs - ** find related work - question_score/view_count
Discovering, Explaining and Summarizing Controversial Discussions in Community Q&A Sites - controversial
Investigating the Quality Aspects of Crowd-Sourced Developer Forum: A Case Study of Stack Overflow- the reproducibility of issues can
Reading Answers on Stack Overflow: Not Enough! - comments

----
We will use both the score, view_count, and the score of the answer
quality = (question_score + answer_score) / view_count

---
Models:
Random lm: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomlmRegressor.html

Future Model Ideas:
- ANN that includes the TOPIC involved, calculated via LDA
'''

from pandas import read_csv, to_datetime, to_timedelta, concat
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from datetime import timedelta

from matplotlib import pyplot
import joblib


def clean_data(df):
    '''
    Modify columns so usable
    '''
    df["question_date"] = to_datetime(df["question_date"])
    df["answer_date"] = to_datetime(df["answer_date"])

    # find our metric of quality
    df["quality"] = (df["question_score"] + df["answer_score"])/df["view_count"]

    # i can't figure out how ot convert this to an integer
    df["time_until_answer"] = to_timedelta(df["answer_date"] - df["question_date"])
    return df



files = ["deprecated_libraries", "explicit_mention"]


df_lib = read_csv("data/filtered/deprecated_libraries.csv").dropna(subset=["answer_id"])
df_key = read_csv("data/filtered/explicit_mention.csv")

df = concat([df_lib, df_key], ignore_index=True)

df = clean_data(df)


# set if explict or not
df["is_explicit"] = 0
df["is_explicit"].loc[df.index > len(df_lib)] = 1


features = ['question_score', "view_count", "answer_count", "answer_score", "question_comment_count", "answer_comment_count", "is_explicit"]
df_train = df[features]

lm = LinearRegression()
lm = lm.fit(df_train, df["quality"])

r2 = lm.score(df_train, df["quality"])
print(r2)

# save the model
filename = 'models/regression_lm.sav'
joblib.dump(lm, filename)

importance = lm.coef_
# summarize feature importance
for i,v in enumerate(importance):
    print('Feature: %s, Score: %.5f' % (features[i],v))

# plot feature importance
pyplot.figure(figsize=(14,7), dpi=150)
pyplot.grid(color="#2E282A", alpha=0.5)
pyplot.bar(features, importance)
pyplot.title("Feature Importance", fontsize=14, color='#2E282A')
pyplot.xlabel("Feaure", fontsize=12, color='#2E282A')
pyplot.ylabel("importance", fontsize=12, color='#2E282A')
pyplot.savefig("plots/regression/feaure_importance_lm.png")
pyplot.show()

    
