'''
Reference: https://machinelearningmastery.com/time-series-data-visualization-with-python/
'''

from pandas import read_csv, concat, to_datetime, to_timedelta

from scripts.regression_models.regression_topics import clean_data
from scripts.graphing import scatter_two


def main():
    df_lib = read_csv("data/filtered/deprecated_libraries.csv")
    df_key = read_csv("data/filtered/explicit_mention.csv")

    df = concat([df_lib, df_key], ignore_index=True)

    df = clean_data(df)


    # set if explict or not
    df["is_explicit"] = 0
    df["is_explicit"].loc[df.index > len(df_lib)] = 1

    quality_columns = ["question_score", "view_count", "answer_count", "question_comment_count", "answer_score", "answer_comment_count", "quality"]
    # time_columns = ["question_date", "answer_date", "time_until_answer"]
    time_columns = ["question_date", "answer_date"]

    mask = df["is_explicit"] == 1
    for quality_column in quality_columns:
        for time_column in time_columns:

            filename = "plots/time_series/"+time_column+"_vs_"+quality_column+".png"
            title = quality_column+" vs "+time_column

            try:
                scatter_two(df[time_column], df[quality_column], mask, title, filename, time_column, quality_column, "Explicit Deprecation", "Deprecated API")
            except TypeError:
                continue


if __name__ == "__main__":
    main()
