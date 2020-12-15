from pandas import read_csv


df_all = read_csv("data/unfiltered/all_questions.csv")

print("All Questions")
print(df_all.count())
print(df_all.mean())
print(df_all.std())

df_all = None

df_libraries = read_csv("data/filtered/deprecated_libraries.csv")
df_keywords = read_csv("data/filtered/explicit_mention.csv")


print("/nDeprecated Libraries")
print(df_libraries.count())
print(df_libraries.mean())
print(df_libraries.std())


print("/nExplicit Mention")
print(df_keywords.count())
print(df_keywords.mean())
print(df_keywords.std())


# split of the libraries
libraries = {"pytorch":0, "tensorflow":0, "keras":0, "tesseract":0, "pyspark":0, "caffe":0, "theano":0}

for i in df_libraries.index:
    row = df_libraries.loc[i]
    for library in libraries.keys():
        # check for questions
        if library in row["question_body"].lower():
            libraries[library] += 1
        elif type(row["answer_body"]) == "string" and row["answer_body"] is not None and library in row["answer_body"].lower():
            libraries[library] += 1
print(libraries)

libraries = {"pytorch":0, "tensorflow":0, "keras":0, "tesseract":0, "pyspark":0, "caffe":0, "theano":0}

for i in df_keywords.index:
    row = df_keywords.loc[i]
    for library in libraries.keys():
        # check for questions
        if library in row["question_body"].lower():
            libraries[library] += 1
        elif type(row["answer_body"]) == "string" and row["answer_body"] is not None and library in row["answer_body"].lower():
            libraries[library] += 1
print(libraries)
