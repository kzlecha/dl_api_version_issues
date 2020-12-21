from pandas import read_csv, read_pickle, to_datetime, to_timedelta, concat
from sklearn.ensemble import RandomForestRegressor

from datetime import timedelta
from matplotlib import pyplot
import joblib


# https://coolors.co/ef476f-ffd166-06d6a0-118ab2-073b4c-7b415e


def clean_data(df):
    '''
    Modify columns so usable
    '''
    df["question_date"] = to_datetime(df["question_date"])
    df["answer_date"] = to_datetime(df["answer_date"])

    # find our metric of quality
    df["quality"] = (df["question_score"] + df["answer_score"])/df["view_count"]

    # i can't figure out how ot convert this to an integer
    df["time_until_answer"] = df["answer_date"] - df["question_date"]
    return df


def plot_features(features, importance):
    pyplot.figure(figsize=(14,7), dpi=150)
    pyplot.grid(color="#2E282A", alpha=0.5)
    pyplot.bar(features, importance, color="#073B4C")
    pyplot.title("Feature Importance", fontsize=14, color='#2E282A')
    pyplot.xlabel("Feaure", fontsize=12, color='#2E282A')
    pyplot.ylabel("importance", fontsize=12, color='#2E282A')
    pyplot.savefig("plots/regression/feaure_importance_forest_topics.png")
    pyplot.show()


def main():

    df_lib = read_pickle("data/filtered/tokenized/deprecated_libraries_lda.pkl").dropna(subset=["answer_id"])
    df_key = read_pickle("data/filtered/tokenized/explicit_mention_lda.pkl")

    df = concat([df_lib, df_key], ignore_index=True)

    df = clean_data(df)


    # set if explict or not
    df["is_explicit"] = 0
    df["is_explicit"].loc[df.index > len(df_lib)] = 1

    topics = []
    topic_labels = read_csv('data/filtered/lda_topic_label/deprecated_libraries.csv')
    topics.extend(topic_labels.values)
    topic_labels = read_csv('data/filtered/lda_topic_label/explicit_mention.csv') + 20
    topics.extend(topic_labels.values)
    df["topics"] = topics
    print(df["topics"])

    # features = ['question_score', "view_count", "answer_count", "answer_score", "question_comment_count", "answer_comment_count", "is_explicit", "topics"]
    features = ['question_score', "answer_count", "answer_score", "question_comment_count", "answer_comment_count", "is_explicit", "topics"]
    df_train = df[features]

    forest = RandomForestRegressor(max_features="sqrt", oob_score="True")
    forest = forest.fit(df_train, df["quality"])

    r2 = forest.score(df_train, df["quality"])
    print("OOB:", r2)


    # save the model
    filename = 'models/topics_forest.sav'
    joblib.dump(forest, filename)

    importance = forest.feature_importances_
    # summarize feature importance
    for i,v in enumerate(importance):
        print('Feature: %s, Score: %.5f' % (features[i],v))

    # plot feature importance
    plot_features(features, importance)


if __name__ == "__main__":
    main()

    
