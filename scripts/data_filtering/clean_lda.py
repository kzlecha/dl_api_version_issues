'''
References:
- https://www.kaggle.com/ktattan/lda-and-document-similarity
- http://www.cse.chalmers.se/~richajo/dit862/L13/LDA%20with%20gensim%20(small%20example).html

'''
# download "punkt"
import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize
from nltk import FreqDist
from nltk.stem.porter import PorterStemmer
from re import sub

from pandas import read_csv


code_stopwords = ["arg", "kwarg", "args", "kwargs", "return", "def", "__init__", "__name__", "import", "from", "print", "super.__init__", "&lt", "&gt"]


def initial_clean(text):
    """
    clean the given string text
    """
    # (\w+[-\.]\w+)+ matches text code

    # remove less than and greater than
    text = sub("lt", ">", text)
    text = sub("gt", "<", text)

    # Set to only ne
    text = sub("[^a-zA-Z ._]", "", text).lower()

    # remove anything with more than 2 underscores or dots <- NOT PYTHON CODE
    # text = sub("___", "", text)
    # text = sub("..", "", text)
    

    # since the code is saved as 
    text = word_tokenize(text)
    return text


def remove_stop_words(text):
    """
    Function that removes all stopwords from text
    """
    return [word for word in text if (word not in stopwords.words('english')) and (word not in code_stopwords)]
    # return [word for word in text if (word not in stopwords.words('english'))]


def stem_words(text):
    """
    Function to stem words, so plural and singular are treated the same
    """
    stemmer = PorterStemmer()
    try:
        text = [stemmer.stem(word) for word in text]
        text = [word for word in text if len(word) > 1] # make sure we have no 1 letter words
    except IndexError: # the word "oed" broke this, so needed try except
        pass
    return text


def apply_all(text):
    """
    This function applies all the functions above into one
    """
    return stem_words(remove_stop_words(initial_clean(text)))


def keep_top_k_words(text):
    '''
    keep the top k words in the text
    '''
    return [word for word in text if word in top_k_words]


files = ["deprecated_libraries", "explicit_mention"]

for filename in files:
    # read the data
    filepath = "data/filtered/"+filename+".csv" 
    df = read_csv(filepath)

    # it will get confused by nans
    df["answer_body"] = df["answer_body"].fillna('')

    # clean text and title and create new column "tokenized"
    df['tokenized'] = df['question_body'].apply(apply_all) + df['answer_body'].apply(apply_all)
    # df['tokenized'] = df['question_body'].apply(apply_all)

    # use nltk fdist to get a frequency distribution of all words
    all_words = [word for item in list(df['tokenized']) for word in item]
    fdist = FreqDist(all_words)
    print(len(fdist)) # number of unique words

    # get the top 95%
    k = round(len(fdist)*.95)
    top_k_words,_ = zip(*fdist.most_common(k))
    top_k_words = set(top_k_words)

    # keep only the top k
    df['tokenized'] = df['tokenized'].apply(keep_top_k_words)

    df.to_pickle("data/filtered/tokenized/"+filename+"_token.pkl", protocol=4)

