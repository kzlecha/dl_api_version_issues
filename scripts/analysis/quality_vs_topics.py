'''
References:
- https://www.kaggle.com/ktattan/lda-and-document-similarity
- http://www.cse.chalmers.se/~richajo/dit862/L13/LDA%20with%20gensim%20(small%20example).html

LDA Model: https://radimrehurek.com/gensim/models/ldamodel.html
'''

from pandas import read_pickle, read_csv
from numpy import array, arange, linspace

from gensim.models import LdaModel
from gensim import corpora, similarities


from matplotlib import pyplot


# https://coolors.co/ef476f-ffd166-06d6a0-118ab2-073b4c-7b415e
colors = ["#ef476f", "#ffd166", "#06d6a0", "#118ab2", "#073b4c", "#7B415E"]



def plot_quality_dist(df, filename):
    pyplot.figure(figsize=(14,7), dpi=150)
    pyplot.grid(color="#2E282A", alpha=0.5)

    for i in range(0,20):
        mask = df["main_topic"] == i
        df["temp"] = i
        pyplot.scatter(df["temp"].loc[mask], df["quality"].loc[mask], alpha=0.75, color=colors[i%6], label=str(i))
    df = df.drop(["temp"], axis=1)

    pyplot.title("Quality Across Topics", fontsize=14, color='#2E282A')
    pyplot.xlabel('Topic ID', fontsize=12, color='#2E282A')
    pyplot.ylabel("Calculated Quality", fontsize=12, color='#2E282A')
    pyplot.xlim(0, 20)
    pyplot.legend()

    filename = "plots/lda/"+filename+"_topic_quality.png"
    pyplot.savefig(filename)

    pyplot.show()



files = ["deprecated_libraries", "explicit_mention"]

quality_comparision = []
topic_comparision = []

for filename in files:
    # read in the data
    filepath = "data/filtered/tokenized/"+filename+"_lda.pkl" 
    df = read_pickle(filepath).dropna(subset=["answer_id"])
    
    model_name = "models/"+filename+"_ldamodel"
    model = LdaModel.load(model_name)

    dictionary = corpora.Dictionary(df['tokenized'])

    df["quality"] = (df["question_score"] + df["answer_score"])/df["view_count"]

    topics = []
    words = []

    for i in df.index:
        row = df.loc[i]

        bow = dictionary.doc2bow(row.loc["tokenized"])
        doc_topics = model.get_document_topics(bow=bow)
        doc_distribution = array([tup[1] for tup in doc_topics])

        # print the top contributing topic and their words
        for j in doc_distribution.argsort()[-1:][::-1]:
            topics.append(j)

    df["main_topic"] = topics

    df["main_topic"].to_csv("data/filtered/lda_topic_label/"+filename+".csv", index=False)

    plot_quality_dist(df, filename)

    print("\n", filename)
    print(df.corr())

    print(df.groupby(["main_topic"])["quality"].mean())

    
