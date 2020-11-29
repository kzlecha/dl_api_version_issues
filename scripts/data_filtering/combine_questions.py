from pandas import DataFrame, read_csv, concat, notnull


source_data = []

# read in all data
lib_names = ["caffe", "keras", "pyspark", "pytorch", "tensorflow", "tesseract", "theano"]
for lib_name in lib_names:
    filepath = "data/unfiltered/source/"+lib_name+".csv"
    source_data.append(read_csv(filepath))

# combine the data into one large dataframe
df = concat(source_data, ignore_index=True)

# drop any duplicates - check for the same question_id and answer_id
df = df.drop_duplicates(subset=["Id", "Id.1"])

# rename the columns to be easier to understand
df.columns = ["question_id", "question_date", "question_score", "view_count", "question_body", "question_title", "tags", "answer_count", "question_comment_count", "closed_date", "answer_id", "answer_date", "answer_score", "answer_body", "answer_comment_count"]

# set NaN in answer_body to None
df.loc[:,"answer_body"] = df.loc[:,"answer_body"].where(notnull(df.loc[:,"answer_body"]), None)

df.to_csv("data/unfiltered/all_questions.csv", index=False)
