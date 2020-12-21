'''
'''

from pandas import read_csv

df_deprecated_lib = read_csv("data/filtered/deprecated_libraries.csv").dropna(subset=["answer_id"]).drop(["question_id", "answer_id"], axis=1)
df_explicit = read_csv("data/filtered/explicit_mention.csv").drop(["question_id", "answer_id"], axis=1)

frameworks = ["tensorflow", "keras", "theano", "caffe", "tessaract", "pytorch", "pyspark"]

framework_list = []

for i in df_deprecated_lib.index:
    tags = df_deprecated_lib.loc[i, "tags"]

    found = False
    for framework in frameworks:
        if framework in tags.lower():
            framework_list.append(framework)
            found = True
            break
    if not found:
        framework_list.append(None)
        

df_deprecated_lib["framework"] = framework_list


framework_list = []

for i in df_explicit.index:
    tags = df_explicit.loc[i, "tags"]

    found = False
    for framework in frameworks:
        if framework in tags.lower():
            framework_list.append(framework)
            found = True
            break
    if not found:
        framework_list.append(None)

df_explicit["framework"] = framework_list

df_deprecated_lib["quality"] = (df_deprecated_lib["question_score"] + df_deprecated_lib["answer_score"])/df_deprecated_lib["view_count"]
df_explicit["quality"] = (df_explicit["question_score"] + df_explicit["answer_score"])/df_explicit["view_count"]


print("Deprecated API:")
print(df_deprecated_lib.groupby(["framework"])["quality"].mean())
print(df_deprecated_lib.groupby(["framework"]).count().max(axis=1))

print("\nExplicit Reference:")
print(df_explicit.groupby(["framework"])["quality"].mean())
print(df_explicit.groupby(["framework"]).count().max(axis=1))

