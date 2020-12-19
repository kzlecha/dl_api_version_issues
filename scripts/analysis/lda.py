'''
References:
- https://www.kaggle.com/ktattan/lda-and-document-similarity
- http://www.cse.chalmers.se/~richajo/dit862/L13/LDA%20with%20gensim%20(small%20example).html

LDA Model: https://radimrehurek.com/gensim/models/ldamodel.html
'''

from gensim.models import LdaModel
from gensim.corpora import Dictionary

from pandas import read_pickle


files = ["deprecated_libraries", "explicit_mention"]

for filename in files:
    # read in the data
    filepath = "data/filtered/tokenized/"+filename+"_lda.pkl" 
    df = read_pickle(filepath)

    num_topics = 20
    chunksize = 300
    dictionary = Dictionary(df['tokenized'])
    corpus = [dictionary.doc2bow(doc) for doc in df['tokenized']]
    # low alpha means each document is only represented by a small number of topics, and vice versa
    # low eta means each topic is only represented by a small number of words, and vice versa
    model = LdaModel(corpus=corpus, num_topics=num_topics, id2word=dictionary,
                    alpha=1e-2, eta=0.5e-2, chunksize=chunksize, passes=5)

    # save the model
    model_name = "models/"+filename+"_ldamodel"
    model.save(model_name)

    print("\n====\n")
    print(filename.upper())

    for topic_id in range(model.num_topics):
        topic = model.show_topic(topic_id, 10)
        topic_words = [ w for w, _ in topic ]
        
        print('{}: {}'.format(topic_id, ' '.join(topic_words)))

